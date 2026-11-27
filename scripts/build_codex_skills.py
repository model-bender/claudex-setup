#!/usr/bin/env python3
"""Generate the Codex versions of this setup's Claude Code commands, skills and agents.

Each Codex skill is a short wrapper. It tells Codex to read the Claude Code file at
run time and follow it, translating Claude Code's tools into Codex's. Nothing from a
command's body is copied, so a change to a command reaches Codex at once. Only the
description is copied, because Codex chooses skills by it, and --check catches a
description that has drifted from its source.

  python3 scripts/build_codex_skills.py           write every generated file
  python3 scripts/build_codex_skills.py --check   exit 1 if a generated file is out of date
  python3 scripts/build_codex_skills.py --link    write, then link the user skills into ~/.codex/skills

What it writes:
  codex/skills/<name>/SKILL.md   user skills (any repo), linked into ~/.codex/skills
  .agents/skills/<name>/SKILL.md this repo's own commands, which Codex finds in the repo
  .codex/agents/<name>.toml      this repo's agents (agents/*.md), with their instructions

User commands are read from this repo's .claude/commands, and user skills from the
owner's global Claude config (~/.claude/skills), so --check skips the latter where
that is absent, as on CI. The ralph commands loop through a Stop hook; Codex runs the
same script as Claude Code from this repo's .codex/hooks.json. Not generated: GSD (its
installer writes its own Codex copies) and ticket (it needs Atlassian and GitHub MCP
servers neither tool has).
"""
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
USER_OUT = REPO / "codex" / "skills"
PROJECT_OUT = REPO / ".agents" / "skills"
AGENT_SRC = REPO / "agents"
AGENT_OUT = REPO / ".codex" / "agents"
CLAUDE_HOME = Path.home() / ".claude"

FETCH = ("Fetch each page with `curl` to a file (escalated, since it needs the network) and read the saved "
         "file, not a summary of it.")
COURSE_MCP = ("It calls an MCP server that the command file names. If Codex reports that server as not "
              "logged in, the user runs `codex mcp login <server name>` once; stop and say so rather than "
              "skipping the step.")
ROUTINES = ("Codex cannot list the owner's claude.ai cloud routines (Claude Code's RemoteTrigger tool or "
            "`/schedule`). Skip that part of the snapshot step and say in the report that routines were "
            "not checked.")

# name -> (kind, notes for this item). kind is "command" or "skill" (user level, any
# repo) or "project" (this repo's own command).
ITEMS = {
    "changelog-claude": ("command", [FETCH]),
    "changelog-codex": ("command", [FETCH, "Any `codex review` or `codex exec` call in the steps needs "
                                           "escalation too."]),
    "claude-loop": ("command", [
        "Run reviews, builders and escalations with `exec_command` (`tty: true`) and a short yield "
        "time in this terminal's background shell, then collect them with `write_stdin`. A tool "
        "session ID alone does not prove visibility in `/ps`; verify that before claiming it. Do not create tmux "
        "sessions or windows, a separate terminal, or another driver session; this overrides the "
        "general detached-tmux rule.",
        "Every `claude -p` run (the reviewer, any builder, the escalation) needs escalation, since it "
        "reaches the network.",
        "Without `--builder`, the steps that say this session writes the fixes mean that you write them. "
        "The default reviewer (Fable) is a different model from you, so keep it.",
    ]),
    "codex-loop": ("command", [
        "Run reviews, builders and escalations with `exec_command` (`tty: true`) and a short yield "
        "time in this terminal's background shell, then collect them with `write_stdin`. A tool "
        "session ID alone does not prove visibility in `/ps`; verify that before claiming it. Do not create tmux "
        "sessions or windows, a separate terminal, or another driver session; this overrides the "
        "general detached-tmux rule.",
        "Every `codex review` and `codex exec` call needs escalation, since it reaches the network. Keep "
        "the `-c` overrides exactly as written.",
        "Run from Codex, you are the driver as well, so triage is no longer a third model's reading of "
        "each finding: the reviewer, the builder and the triage all come from one family. Say so in the "
        "final report.",
    ]),
    "quiz-me": ("command", [
        "The `allowed-tools` line in the file's front matter is Claude Code's permission list. Ignore it, "
        "and keep to the read-only git and gh commands it names.",
        "Ask each quiz question with `request_user_input` and wait for the answer before the next one.",
    ]),
    "fable-mode": ("skill", [
        "In Claude Code a session hook turns this on for some models. In Codex it runs only when asked: "
        "`$fable-mode`, or the user saying \"fable mode\".",
    ]),
    "humanizer": ("skill", []),
    "readme-style": ("skill", [
        "The banner script and the template sit beside the skill file, in `~/.claude/skills/readme-style/` "
        "(`%USERPROFILE%\\.claude\\skills\\readme-style\\` on Windows). The `gh api markdown` check needs "
        "escalation, since it uses the network.",
    ]),
    "consolidate-lessons": ("project", []),
    "discover": ("project", []),
    "extract-lessons": ("project", [COURSE_MCP]),
    "extract-social-lessons": ("project", [FETCH]),
    "fact-check": ("project", []),
    "optimise": ("project", [ROUTINES]),
    "pr": ("project", []),
    "ralph-loop": ("project", [
        "The file opens with a block marked ```! that Claude Code runs before the model reads the rest. "
        "Run that command yourself first, from the root of this repo, with the user's words after "
        "`$ralph-loop` as its arguments, and stop if it fails.",
        "The loop repeats through a Codex Stop hook in this repo's `.codex/hooks.json`, the same script "
        "Claude Code uses: each time you finish, it sends the loop's prompt back as your next prompt. Codex "
        "runs it only once it is trusted in `/hooks`; if it is not, say so before starting, because the "
        "loop would stop after one pass.",
    ]),
    "cancel-ralph": ("project", [
        "The `allowed-tools` line in the file's front matter is Claude Code's permission list; ignore it.",
    ]),
    "ralph-help": ("project", []),
    "review-pr": ("project", []),
    "revise-claude-md": ("project", [
        "In this repo the shared rules live in `AGENTS.md`, which `CLAUDE.md` imports: put a rule both "
        "tools follow in `AGENTS.md`, and only a Claude-Code-only rule in `CLAUDE.md`.",
    ]),
    "test": ("project", []),
    "top-tips": ("project", []),
    "weekly-update": ("project", [COURSE_MCP, ROUTINES + " That applies to every area it runs "
                                  "`$optimise` for."]),
}

# The Claude agent's model line decides the Codex model and effort, as in the essay
# template: the everyday model maps to Codex's everyday model at medium effort, the
# judgement model to the same model at high effort. A new tier stops the build.
AGENT_MODELS = {"sonnet": ("gpt-6.1-sol", "medium"), "opus": ("gpt-6.1-sol", "high"), "inherit": (None, None)}


def translation():
    user = ", ".join(f"`${n}`" for n, (k, _) in ITEMS.items() if k != "project")
    project = ", ".join(f"`${n}`" for n, (k, _) in ITEMS.items() if k == "project")
    return [
        f"Commands: a Claude Code command written `/name` is the Codex skill `$name` when one exists "
        f"(everywhere: {user}; inside claudex-setup also: {project}). For a Claude Code built-in such as "
        "`/clear` or `/rewind`, use Codex's nearest one or skip that step and say so.",
        "Project rules: Codex reads `AGENTS.md`, not `CLAUDE.md`. Where the file says to read or follow "
        "`CLAUDE.md`, read `AGENTS.md`, and `CLAUDE.md` as well if the repo has one.",
        "Asking the user (`AskUserQuestion`): `request_user_input`, one question per call.",
        "Subagents (the Agent tool, `subagent_type`, \"spawn an agent\"): `spawn_agent` with the full brief, "
        "then `wait_agent` for its result. Claude Code's agent types are not Codex roles: use the nearest "
        "role or the default.",
        "Files (`Read`, `Grep`, `Glob`, `Edit`, `Write`): read with the shell (`sed -n`, `rg`), edit with "
        "`apply_patch`.",
        "Web pages (`WebFetch`, `WebSearch`): the web search tool if you have one, otherwise `curl` to a "
        "file. The network is outside the sandbox, so request escalation with a one-line reason.",
        "Long commands (\"run it in the background\", \"wait for the completion notification\", a Bash "
        "`timeout` in milliseconds): start the command with `exec_command` and a short yield time, which "
        "returns a session while it is still running. Check on it with `write_stdin` (no input) or `wait`, "
        "with `sleep` between checks, until it prints its exit line. Never treat a running command as "
        "finished, and never pipe it through `head` or `tail`.",
        "`Monitor`, `ScheduleWakeup`, `CronCreate`, `TaskStop`: no Codex equivalent; poll with `sleep` as "
        "above.",
        "Artifacts: write the page to a local file and give its path.",
        "Calls to `codex` or `claude -p` in the steps reach the network, so each runs with "
        "`sandbox_permissions: \"require_escalated\"` and a one-line justification. Never add "
        "`--dangerously-bypass-approvals-and-sandbox`.",
        "\"This session\", \"the driver\" and \"you\" mean you, Codex. Where the file contrasts Claude with "
        "Codex, read it from Codex's side, and say in your final report where that changed the result.",
    ]


def frontmatter(text):
    """Return the top-level keys of a file's YAML front matter as plain strings.

    Handles plain, quoted and block (`|` or `>`) scalars, which is all these files use;
    a block scalar's lines are joined with spaces, since every caller wants one line.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields, key, block = {}, None, None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if block is not None:
            if line.startswith((" ", "\t")) or not line.strip():
                block.append(line.strip())
                continue
            fields[key] = " ".join(part for part in block if part)
            block = None
        match = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip()
        if value in ("|", ">", "|-", ">-", "|+", ">+"):
            block = []
            continue
        if value.startswith('"') and value.endswith('"') and len(value) > 1:
            try:
                value = json.loads(value)
            except ValueError:
                value = value[1:-1]
        elif value.startswith("'") and value.endswith("'") and len(value) > 1:
            value = value[1:-1].replace("''", "'")
        fields[key] = value
    if block is not None:
        fields[key] = " ".join(part for part in block if part)
    return fields


def body(text):
    """Everything after the closing --- of the front matter."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return text
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "".join(lines[i + 1:])
    return ""


def codex_wording(text):
    """Turn `/name` for each generated item into `$name`, leaving paths such as a/b alone."""
    for name in sorted(ITEMS, key=len, reverse=True):
        text = re.sub(r"(?<![\w/.~-])/" + re.escape(name) + r"(?![\w-])", "$" + name, text)
    return text


def source_paths(name, kind):
    """Return (file read at build time, POSIX path Codex reads, Windows path Codex reads, output file)."""
    if kind == "command":
        return (REPO / ".claude" / "commands" / f"{name}.md",
                f"~/.claude/commands/{name}.md",
                f"%USERPROFILE%\\.claude\\commands\\{name}.md",
                USER_OUT / name / "SKILL.md")
    if kind == "skill":
        return (CLAUDE_HOME / "skills" / name / "SKILL.md",
                f"~/.claude/skills/{name}/SKILL.md",
                f"%USERPROFILE%\\.claude\\skills\\{name}\\SKILL.md",
                USER_OUT / name / "SKILL.md")
    return (REPO / ".claude" / "commands" / f"{name}.md",
            f".claude/commands/{name}.md (from the root of this repo, `git rev-parse --show-toplevel`)",
            f".claude\\commands\\{name}.md (from the root of this repo)",
            PROJECT_OUT / name / "SKILL.md")


def render(name, kind, notes, source_text):
    fields = frontmatter(source_text)
    description = codex_wording(fields.get("description", "").strip())
    if not description:
        raise ValueError(f"no description in the source of {name}")
    if fields.get("disable-model-invocation", "").lower() == "true":
        description += " Run only when the user asks for it by name."
    hint = fields.get("argument-hint", "").strip()
    _, posix, windows, _ = source_paths(name, kind)
    kind_word = "skill" if kind == "skill" else "command"
    origin = "claudex-setup" if kind != "project" else "this repo"
    out = [
        "---",
        f"name: {name}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        "---",
        "",
        f"> Generated by `scripts/build_codex_skills.py` in {origin} from the Claude Code {kind_word} "
        f"`/{name}`. Edit that source or the script, not this file.",
        "",
        f"# ${name}",
        "",
        f"The steps for this {kind_word} live in a Claude Code file. Before doing anything else, read the "
        "whole of it and follow it as written, translating Claude Code's tools as set out below.",
        "",
    ]
    if kind == "project":
        out.append(f"- The file: `{posix.split(' ')[0]}`{posix[len(posix.split(' ')[0]):]}")
    else:
        out += [f"- WSL, Linux or macOS: `{posix}`", f"- Windows: `{windows}`"]
    out += [
        "",
        "If the file is missing, stop and say so: this skill has nothing to run without it.",
        "",
        "The file was written for Claude Code, which hands it the words typed after the command as "
        f"`$ARGUMENTS`. Here those are whatever the user typed after `${name}`, or nothing."
        + (f" Expected form: {hint}" if hint else ""),
        "",
        "## Claude Code to Codex",
        "",
    ]
    out += [f"- {line}" for line in translation()]
    if notes:
        out += ["", f"## Notes for ${name}", ""]
        out += [f"- {line}" for line in notes]
    return "\n".join(out) + "\n"


def toml_string(text):
    return json.dumps(text, ensure_ascii=False)


def render_agent(path):
    text = path.read_text(encoding="utf-8")
    fields = frontmatter(text)
    name = fields.get("name") or path.stem
    description = codex_wording(fields.get("description", "").strip())
    if not description:
        raise ValueError(f"no description in {path}")
    claude_model = fields.get("model", "inherit").strip()
    if claude_model not in AGENT_MODELS:
        raise ValueError(f"no Codex model mapped for model: '{claude_model}' in {path}")
    model, effort = AGENT_MODELS[claude_model]
    instructions = body(text)
    if "'''" in instructions:
        raise ValueError(f"{path} contains ''' which cannot go into a TOML literal string")
    tools = fields.get("tools", "").strip()
    preface = [
        f"Generated from agents/{path.name} by scripts/build_codex_skills.py. Claude Code's tool names below "
        "map to Codex's: Read, Grep and Glob are shell reads; Edit and Write are apply_patch; Bash is the "
        "shell. Codex reads AGENTS.md where these instructions say CLAUDE.md, and CLAUDE.md too if the repo "
        "has one.",
    ]
    if tools:
        preface.append(f"In Claude Code this agent may use only: {tools}. Keep to the same limits here.")
    out = [
        f"# Generated from agents/{path.name} by scripts/build_codex_skills.py. Edit the source, not this copy.",
        "",
        f"name = {toml_string(name)}",
        f"description = {toml_string(description)}",
    ]
    if model:
        out += [f"model = {toml_string(model)}", f"model_reasoning_effort = {toml_string(effort)}"]
    out += ["developer_instructions = '''", "\n\n".join(preface), "", instructions.rstrip("\n"), "'''"]
    return name, "\n".join(out) + "\n"


def emit(target, text, check, problems):
    if check:
        current = target.read_text(encoding="utf-8") if target.is_file() else None
        if current != text:
            problems.append(f"{target.relative_to(REPO)} is out of date")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {target.relative_to(REPO)}")


def build(check):
    """Write (or, with check, compare) every generated file. Return the list of problems."""
    problems = []
    for name, (kind, notes) in ITEMS.items():
        source, _, _, target = source_paths(name, kind)
        if not source.is_file():
            if check and kind == "skill":
                print(f"skip {name}: {source} not on this machine")
                continue
            problems.append(f"{name}: source missing at {source}")
            continue
        emit(target, render(name, kind, notes, source.read_text(encoding="utf-8")), check, problems)
    agent_names = set()
    for path in sorted(AGENT_SRC.glob("*.md")):
        try:
            name, text = render_agent(path)
        except ValueError as error:
            problems.append(str(error))
            continue
        agent_names.add(name)
        emit(AGENT_OUT / f"{name}.toml", text, check, problems)
    expected = {
        USER_OUT: {n for n, (k, _) in ITEMS.items() if k != "project"},
        PROJECT_OUT: {n for n, (k, _) in ITEMS.items() if k == "project"},
    }
    for folder, names in expected.items():
        if folder.is_dir():
            for entry in sorted(p for p in folder.iterdir() if p.is_dir()):
                if entry.name not in names:
                    problems.append(f"{entry.relative_to(REPO)} is not generated by this script")
    if AGENT_OUT.is_dir():
        for entry in sorted(AGENT_OUT.glob("*.toml")):
            if entry.stem not in agent_names:
                problems.append(f"{entry.relative_to(REPO)} is not generated by this script")
    return problems


def link():
    """Link each user skill into Codex's user skills folder. Return the list of problems."""
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    skills = codex_home / "skills"
    names = [n for n, (k, _) in ITEMS.items() if k != "project"]
    if os.name == "nt":
        print("Windows needs an elevated PowerShell for symlinks. Run there:")
        for name in names:
            print(f"  New-Item -ItemType SymbolicLink -Force -Path \"{skills / name}\" -Target \"{USER_OUT / name}\"")
        return []
    skills.mkdir(parents=True, exist_ok=True)
    problems = []
    for name in names:
        path, target = skills / name, USER_OUT / name
        if path.is_symlink():
            if path.resolve() == target.resolve():
                print(f"ok {path}")
                continue
            path.unlink()
        elif path.exists():
            problems.append(f"{path} exists and is not a link; move it aside and run --link again")
            continue
        path.symlink_to(target)
        print(f"linked {path} -> {target}")
    return problems


def main(argv):
    check = "--check" in argv
    problems = build(check)
    if not problems and "--link" in argv and not check:
        problems = link()
    for problem in problems:
        print(f"build_codex_skills: {problem}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
