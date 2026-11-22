#!/usr/bin/env python3
"""
Lessons library helper: search, transcript lookups and quote checks
===================================================================
The agents that mine and dedupe lessons need the same three helpers on every run.
Each run used to write its own, and a home-made search missed a duplicate, so this
script is the one shared version.

Usage (stdlib only, Python 3.9+, run from anywhere):
    python3 scripts/lessons.py search [-k N] [--json] QUERY [QUERY ...]
    python3 scripts/lessons.py from-transcript [--json] PATH [PATH ...]
    python3 scripts/lessons.py check-quotes FILE.json [FILE.json ...]

Every subcommand takes --root DIR, the folder holding lessons/ and transcripts/
(default: the repo this script sits in).

search ranks the active lessons under lessons/<category>/<slug>.md with BM25. The
slug counts twice, the title and TL;DR three times each, and everything after the
TL;DR heading once. The index is built in memory on every call (about a second for
2,000 lessons) and never cached to disk, so pass a batch of queries to one call
rather than making one call per query.

from-transcript lists the active lessons whose frontmatter `sources:` cite each
transcript, given repo-relative (transcripts/<creator>/<file>.txt).

check-quotes reads miner results, {"new_lessons": [{"id", "sources", "quote"}, ...]},
and fails a candidate unless its quote, with every whitespace run collapsed to one
space, is a substring of one of its cited transcripts treated the same way. It
exits 1 when any candidate failed, else 0.
"""

import argparse
import json
import math
import re
import signal
import sys
from collections import Counter
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
TLDR_CUT = 260

STOP = set(
    "a an the of to in on for and or with your you it is are be as at by from that this not do does "
    "into its so if then than when what which who how use using used can will just one each every any "
    "all more most only also via per up out no yes have has had get make them they their our we i".split()
)
WORD = re.compile(r"[a-z0-9][a-z0-9_.\-/]*")
SEPARATOR = re.compile(r"[-_./]")
TITLE = re.compile(r"^# (.+)$", re.MULTILINE)
TLDR = re.compile(r"## TL;DR\s*\n+(.*?)\n\s*\n##", re.DOTALL)
SPACES = re.compile(r"\s+")


# --- tokens -----------------------------------------------------------------

def stem(word):
    # A crude suffix strip, so "hooks" finds "hook"; the length floor stops it
    # mangling short words like "uses" or "bed".
    for suffix in ("ing", "ed", "es", "s"):
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            return word[: -len(suffix)]
    return word


_terms = {}


def terms(text):
    """Stemmed lowercase words, plus the parts of any word joined by - _ . or /.

    Keeping both the joined word and its parts lets "claude-code" match a query for
    "claude code" while an exact "claude-code" query still scores higher. Results are
    cached per word because tokenizing the library is most of a call's run time.
    """
    out = []
    for word in WORD.findall(text.lower()):
        got = _terms.get(word)
        if got is None:
            parts = [word] + SEPARATOR.split(word) if SEPARATOR.search(word) else [word]
            got = _terms[word] = [stem(p) for p in parts if len(p) > 1 and p not in STOP]
        out += got
    return out


def squash(text):
    """Collapse every whitespace run to one space, so a quote can wrap differently."""
    return SPACES.sub(" ", text).strip()


# --- the library ------------------------------------------------------------

def unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1]
    return value


def frontmatter(text):
    """The YAML frontmatter as a dict, list values as lists.

    Lesson frontmatter is flat (scalars and one-level lists), so this reads just
    that shape rather than pulling in a YAML parser.
    """
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    fields, key = {}, None
    for line in text[4:end].split("\n"):
        m = re.match(r"([A-Za-z_][\w-]*):(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            if value.startswith("[") and value.endswith("]"):
                fields[key] = [unquote(v) for v in value[1:-1].split(",") if v.strip()]
            else:
                fields[key] = unquote(value) if value else []
            continue
        m = re.match(r"\s*-\s+(.*)$", line)
        if m and isinstance(fields.get(key), list):
            fields[key].append(unquote(m.group(1)))
    return fields


def as_text(value):
    return value if isinstance(value, str) else ""


def load_lessons(root):
    """Every active lesson under root/lessons/<category>/<slug>.md, in path order."""
    lessons = []
    # Sort on the forward-slash path so tied scores rank the same on every OS.
    for path in sorted((root / "lessons").glob("*/*.md"), key=lambda p: p.parent.name + "/" + p.name):
        # utf-8-sig drops a byte order mark that would hide the opening "---".
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        fields = frontmatter(text)
        if fields.get("status") != "active":
            continue
        title = TITLE.search(text)
        tldr = TLDR.search(text)
        sources = fields.get("sources")
        lessons.append({
            "path": path.parent.name + "/" + path.stem,
            "slug": path.stem,
            "title": title.group(1).strip() if title else "",
            "tldr": tldr.group(1).strip().replace("\n", " ") if tldr else "",
            "created": as_text(fields.get("created")),
            "sources": [sources] if isinstance(sources, str) else (sources or []),
            "body": text.split("## TL;DR")[-1],
        })
    return lessons


def build_index(lessons):
    """Per lesson its weighted term counts and length, plus the document frequencies."""
    docs = []
    for lesson in lessons:
        weighted = (terms(lesson["slug"]) * 2 + terms(lesson["title"]) * 3
                    + terms(lesson["tldr"]) * 3 + terms(lesson["body"]))
        docs.append((lesson, Counter(weighted), len(weighted)))
    df = Counter()
    for _, counts, _ in docs:
        df.update(counts.keys())
    avg = (sum(n for _, _, n in docs) / len(docs) if docs else 0) or 1
    return docs, df, avg


def search(index, query, k):
    """The top k (score, lesson) pairs for one query, best first, BM25 with k1=1.5, b=0.75."""
    docs, df, avg = index
    total = len(docs)
    # Sorted so the float sums add up in the same order on every run.
    wanted = sorted(set(terms(query)))
    hits = []
    for lesson, counts, length in docs:
        score = 0.0
        for term in wanted:
            f = counts.get(term, 0)
            if f:
                idf = math.log(1 + (total - df[term] + 0.5) / (df[term] + 0.5))
                score += idf * f * 2.5 / (f + 1.5 * (0.25 + 0.75 * length / avg))
        if score:
            hits.append((score, lesson))
    # A stable sort keeps tied lessons in path order.
    hits.sort(key=lambda hit: -hit[0])
    return hits[:k]


def cited_form(root, path):
    """A transcript path the way lessons cite it: repo-relative, forward slashes."""
    p = Path(path)
    if p.is_absolute():
        try:
            path = str(p.resolve().relative_to(root.resolve()))
        except ValueError:
            pass
    path = path.replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


# --- subcommands --------------------------------------------------------------

def cmd_search(root, queries, k, as_json):
    index = build_index(load_lessons(root))
    results = [(q, search(index, q, k)) for q in queries]
    if as_json:
        print(json.dumps([
            {"query": q, "hits": [
                {"score": round(score, 3), "created": lesson["created"], "path": lesson["path"],
                 "title": lesson["title"], "tldr": lesson["tldr"]}
                for score, lesson in hits]}
            for q, hits in results], indent=1, ensure_ascii=False))
        return 0
    blocks = []
    for q, hits in results:
        lines = ["### " + q]
        for score, lesson in hits:
            tldr = lesson["tldr"]
            if len(tldr) > TLDR_CUT:
                tldr = tldr[:TLDR_CUT] + "..."
            lines += [f"  {score:5.1f} {lesson['created']} {lesson['path']}",
                      "        T: " + lesson["title"],
                      "        " + tldr]
        if not hits:
            lines.append("  (no matches)")
        blocks.append("\n".join(lines))
    print("\n\n".join(blocks))
    return 0


def cmd_from_transcript(root, paths, as_json):
    lessons = load_lessons(root)
    results = []
    for path in paths:
        rel = cited_form(root, path)
        results.append((rel, [lesson for lesson in lessons if rel in lesson["sources"]]))
    if as_json:
        print(json.dumps([
            {"transcript": rel, "lessons": [
                {"path": lesson["path"], "title": lesson["title"], "tldr": lesson["tldr"]}
                for lesson in found]}
            for rel, found in results], indent=1, ensure_ascii=False))
        return 0
    blocks = []
    for rel, found in results:
        lines = ["### " + rel]
        for lesson in found:
            lines += ["  " + lesson["path"], "        T: " + lesson["title"], "        " + lesson["tldr"]]
        if not found:
            # A mistyped path also cites nothing, so say which case this is.
            where = "" if (root / rel).is_file() else f" (and no such file under {root})"
            lines.append("  none: no active lesson cites this transcript" + where)
        blocks.append("\n".join(lines))
    print("\n\n".join(blocks))
    return 0


def quote_problems(root, cand, transcript):
    """Why a miner candidate's quote fails, or an empty list when it passes."""
    if not isinstance(cand, dict):
        return ["candidate is not an object"]
    sources = cand.get("sources")
    if isinstance(sources, str):
        sources = [sources]
    if not isinstance(sources, list) or not sources or not all(isinstance(s, str) and s.strip() for s in sources):
        return ["no transcript in sources"]
    quote = cand.get("quote")
    problems = []
    if quote is None:
        problems.append("missing quote")
    elif not isinstance(quote, str):
        problems.append("quote is not a string")
    elif not squash(quote):
        problems.append("empty quote")
    quote_ok = not problems
    found = []
    for source in sources:
        text = transcript(cited_form(root, source))
        if text is None:
            problems.append("transcript not found: " + source)
        else:
            found.append((source, text))
    if quote_ok and found and not any(squash(quote) in text for _, text in found):
        problems.append("quote not found in " + ", ".join(source for source, _ in found))
    return problems


def cmd_check_quotes(root, files):
    cache = {}

    def transcript(rel):
        # Several candidates usually cite one transcript, so read each once.
        if rel not in cache:
            path = root / rel
            cache[rel] = squash(path.read_text(encoding="utf-8-sig", errors="replace")) if path.is_file() else None
        return cache[rel]

    total = failed = unreadable = 0
    for name in files:
        try:
            candidates = json.loads(Path(name).read_text(encoding="utf-8-sig"))["new_lessons"]
            if not isinstance(candidates, list):
                raise TypeError("new_lessons is not a list")
        except (OSError, ValueError, KeyError, TypeError) as e:
            unreadable += 1
            print(f"{name}: cannot read new_lessons ({type(e).__name__}: {e})")
            continue
        for i, cand in enumerate(candidates, 1):
            total += 1
            problems = quote_problems(root, cand, transcript)
            if problems:
                failed += 1
                cid = cand.get("id") if isinstance(cand, dict) and cand.get("id") else f"#{i}"
                print(f"{name}: {cid}: " + "; ".join(problems))
    summary = f"{total} candidates, {failed} failed"
    if unreadable:
        summary += f", {unreadable} file(s) unreadable"
    print(summary)
    return 1 if failed or unreadable else 0


def main(argv=None):
    # `search ... | head` closes the pipe early; exit quietly instead of a
    # BrokenPipeError traceback. Windows has no SIGPIPE.
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    # A Windows pipe defaults to the locale code page, which cannot encode every
    # title; the agents reading this output decode UTF-8.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--root", type=Path, default=DEFAULT_ROOT, metavar="DIR",
                        help="folder holding lessons/ and transcripts/ (default: %(default)s)")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search", parents=[common], help="rank active lessons against each query")
    s.add_argument("-k", type=int, default=6, help="hits per query (default: 6)")
    s.add_argument("--json", action="store_true", help="print one JSON array instead of text")
    s.add_argument("queries", nargs="+", metavar="QUERY")
    t = sub.add_parser("from-transcript", parents=[common], help="list active lessons citing each transcript")
    t.add_argument("--json", action="store_true", help="print one JSON array instead of text")
    t.add_argument("transcripts", nargs="+", metavar="PATH")
    c = sub.add_parser("check-quotes", parents=[common], help="check miner quotes against their transcripts")
    c.add_argument("files", nargs="+", metavar="FILE.json")
    args = ap.parse_args(argv)
    if args.cmd == "check-quotes":
        return cmd_check_quotes(args.root, args.files)
    # A wrong --root would otherwise look like a library with no matches.
    if not (args.root / "lessons").is_dir():
        ap.error(f"no lessons/ folder under {args.root}")
    if args.cmd == "search":
        if args.k < 1:
            s.error("-k must be at least 1")
        return cmd_search(args.root, args.queries, args.k, args.json)
    return cmd_from_transcript(args.root, args.transcripts, args.json)


if __name__ == "__main__":
    sys.exit(main())
