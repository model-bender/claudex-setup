"""Tests for scripts/lessons.py, the search, transcript lookup and quote check that the
lesson miners share.

Each test builds a tiny library under tmp_path and runs the script as a subprocess, so
the command line, the printed output and the exit codes are what get checked. Nothing
here touches the network or the real lessons/ folder.

Run: uv run --with pytest pytest -q tests/
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "lessons.py"
TRANSCRIPT = "transcripts/some-creator/hooks-talk_abc123_20261120.txt"
UNCITED = "transcripts/some-creator/unrelated-talk_def456_20261121.txt"
LONG_TLDR = (
    "A hook that runs your tests before Claude may finish must exit with code 2 on failure. "
    "Exit 1 is only a non-blocking error, so the work is still treated as finished and the task "
    "is marked complete. Wrap the test command so a failure turns into exit 2, and print the reason "
    "to stderr so Claude knows what to fix before it tries to stop again."
)


def lesson(slug, title, tldr, status="active", sources=(TRANSCRIPT,), created="2026-11-20"):
    cited = "".join(f"  - {s}\n" for s in sources)
    return (
        f"---\nid: {slug}\ncreated: {created}\nstatus: {status}\nsupersedes: null\ncategory: x\n"
        f"tool: claude-code\nsources:\n{cited}---\n\n# {title}\n\n## TL;DR\n\n{tldr}\n\n"
        "## How to apply\n\n1. Do the thing.\n"
    )


@pytest.fixture
def root(tmp_path):
    files = {
        "hooks/exit-2-blocks-completion-gate-hooks": lesson(
            "exit-2-blocks-completion-gate-hooks",
            "Make completion-gate hooks exit 2, not 1", LONG_TLDR),
        # Superseded and worded exactly like the search below, so only the status
        # filter can keep it out of the results.
        "hooks/old-hook-exit-code-advice": lesson(
            "old-hook-exit-code-advice", "Hook exit code 2 blocks completion",
            "Hook exit code 2 blocks completion of the task.", status="superseded"),
        "model-selection/route-browser-driving-work-to-codex": lesson(
            "route-browser-driving-work-to-codex", "Route browser-driving work to Codex",
            "Codex drives a real browser more cheaply, so send clicking and form filling there.",
            sources=("transcripts/other-creator/browser-talk_ghi789_20261101.txt",)),
    }
    for rel, text in files.items():
        path = tmp_path / "lessons" / (rel + ".md")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    # Some real lessons were saved with Windows line endings; they must still count.
    crlf = lesson("keep-memory-files-short", "Keep memory files short",
                  "Long memory files crowd the context window.", created="2026-10-01",
                  sources=("transcripts/other-creator/memory-talk_jkl012_20261001.txt",))
    path = tmp_path / "lessons" / "memory" / "keep-memory-files-short.md"
    path.parent.mkdir(parents=True)
    path.write_bytes(crlf.replace("\n", "\r\n").encode("utf-8"))
    transcript = tmp_path / TRANSCRIPT
    transcript.parent.mkdir(parents=True)
    transcript.write_text(
        "# Creator: some-creator\n\nSo most test tools exit with one on failure\n"
        "and the task   just gets marked as completed anyway. Only exit code two sends Claude back.\n",
        encoding="utf-8")
    (tmp_path / UNCITED).write_text("Nothing about hooks here.\n", encoding="utf-8")
    return tmp_path


def run(subcommand, root, *args):
    return subprocess.run([sys.executable, str(SCRIPT), subcommand, "--root", str(root), *args],
                          capture_output=True, text=True, encoding="utf-8")


def search_json(root, *queries, k="6"):
    result = run("search", root, "--json", "-k", k, *queries)
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


# --- search -------------------------------------------------------------------

def test_search_ranks_the_matching_lesson_first_and_never_returns_a_superseded_one(root):
    results = search_json(root, "hook exit code 2 blocks completion", "route browser driving work to codex")
    assert results[0]["hits"][0]["path"] == "hooks/exit-2-blocks-completion-gate-hooks"
    assert results[1]["hits"][0]["path"] == "model-selection/route-browser-driving-work-to-codex"
    paths = [hit["path"] for r in results for hit in r["hits"]]
    assert "hooks/old-hook-exit-code-advice" not in paths


def test_search_finds_a_lesson_saved_with_windows_line_endings(root):
    results = search_json(root, "memory files short")
    assert results[0]["hits"][0]["path"] == "memory/keep-memory-files-short"
    assert results[0]["hits"][0]["created"] == "2026-10-01"


def test_search_json_has_the_documented_keys_and_the_full_tldr(root):
    results = search_json(root, "exit code", "nothing matches xyzzy", k="1")
    assert [r["query"] for r in results] == ["exit code", "nothing matches xyzzy"]
    assert all(set(r) == {"query", "hits"} for r in results)
    assert len(results[0]["hits"]) == 1
    hit = results[0]["hits"][0]
    assert set(hit) == {"score", "created", "path", "title", "tldr"}
    assert hit["score"] > 0 and hit["created"] == "2026-11-20"
    assert hit["title"] == "Make completion-gate hooks exit 2, not 1"
    assert hit["tldr"] == LONG_TLDR
    assert results[1]["hits"] == []


def test_search_text_output_shows_the_query_hit_and_a_cut_tldr(root):
    result = run("search", root, "hook exit code 2 blocks completion")
    assert result.returncode == 0, result.stderr
    lines = result.stdout.splitlines()
    assert lines[0] == "### hook exit code 2 blocks completion"
    assert lines[1].split()[1:] == ["2026-11-20", "hooks/exit-2-blocks-completion-gate-hooks"]
    assert "Make completion-gate hooks exit 2, not 1" in lines[2]
    assert LONG_TLDR not in result.stdout
    assert lines[3].strip().startswith(LONG_TLDR[:200]) and lines[3].endswith("...")


# --- from-transcript --------------------------------------------------------------

def test_from_transcript_lists_citing_lessons_and_reports_none_for_an_uncited_one(root):
    result = run("from-transcript", root, TRANSCRIPT, UNCITED)
    assert result.returncode == 0, result.stderr
    cited, uncited = result.stdout.split("\n\n")
    assert cited.splitlines()[0] == "### " + TRANSCRIPT
    assert "hooks/exit-2-blocks-completion-gate-hooks" in cited
    assert "old-hook-exit-code-advice" not in cited  # superseded, though it cites the transcript
    assert uncited.splitlines()[0] == "### " + UNCITED
    assert "none: no active lesson cites this transcript" in uncited


def test_from_transcript_json_and_an_absolute_path(root):
    result = run("from-transcript", root, "--json", str(root / TRANSCRIPT), UNCITED)
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    assert data[0]["transcript"] == TRANSCRIPT
    assert [l["path"] for l in data[0]["lessons"]] == ["hooks/exit-2-blocks-completion-gate-hooks"]
    assert set(data[0]["lessons"][0]) == {"path", "title", "tldr"}
    assert data[1] == {"transcript": UNCITED, "lessons": []}


# --- check-quotes -------------------------------------------------------------------

def write_miner(root, name, candidates):
    path = root / name
    path.write_text(json.dumps({"new_lessons": candidates}), encoding="utf-8")
    return str(path)


def test_check_quotes_passes_exact_and_rewrapped_quotes(root):
    miner = write_miner(root, "miner-ok.json", [
        {"id": "exact", "sources": [TRANSCRIPT], "quote": "Only exit code two sends Claude back."},
        # The transcript breaks this line and has three spaces where the quote has one.
        {"id": "rewrapped", "sources": [TRANSCRIPT],
         "quote": "most test tools exit with one on failure and the task just gets marked as completed anyway."},
        {"id": "string-source", "sources": TRANSCRIPT, "quote": "  exit with one\non failure "},
    ])
    result = run("check-quotes", root, miner)
    assert result.returncode == 0, result.stdout
    assert result.stdout.splitlines() == ["3 candidates, 0 failed"]


def test_check_quotes_fails_retyped_missing_and_empty_quotes_and_exits_1(root):
    good = write_miner(root, "miner-good.json", [
        {"id": "fine", "sources": [TRANSCRIPT], "quote": "Only exit code two sends Claude back."},
    ])
    bad = write_miner(root, "miner-bad.json", [
        {"id": "retyped", "sources": [TRANSCRIPT], "quote": "Only exit code 2 sends Claude back."},
        {"id": "no-transcript", "sources": ["transcripts/nobody/missing.txt"], "quote": "anything"},
        {"id": "no-quote", "sources": [TRANSCRIPT]},
        {"id": "blank-quote", "sources": [TRANSCRIPT], "quote": "  \n "},
    ])
    result = run("check-quotes", root, good, bad)
    assert result.returncode == 1
    lines = result.stdout.splitlines()
    assert lines[-1] == "5 candidates, 4 failed"
    failures = {line.split(": ")[1]: line for line in lines[:-1]}
    assert set(failures) == {"retyped", "no-transcript", "no-quote", "blank-quote"}
    assert all(line.startswith(bad + ": ") for line in failures.values())
    assert "quote not found" in failures["retyped"]
    assert "transcript not found: transcripts/nobody/missing.txt" in failures["no-transcript"]
    assert "missing quote" in failures["no-quote"]
    assert "empty quote" in failures["blank-quote"]


def test_check_quotes_exits_1_on_a_file_without_new_lessons(root):
    broken = root / "broken.json"
    broken.write_text("{not json", encoding="utf-8")
    result = run("check-quotes", root, str(broken))
    assert result.returncode == 1
    assert result.stdout.splitlines()[-1] == "0 candidates, 0 failed, 1 file(s) unreadable"


# --- usage ----------------------------------------------------------------------------

@pytest.mark.parametrize("args", [[], ["bogus"]])
def test_no_or_unknown_subcommand_prints_usage_and_exits_2(args):
    result = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
    assert result.returncode == 2
    assert "usage:" in result.stderr
