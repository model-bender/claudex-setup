"""Checks for scripts/build_codex_skills.py, which writes the Codex wrappers in codex/skills.

The wrappers copy each Claude Code command's description, so a changed description
must be regenerated. --check fails when one has drifted; CI runs it here. Skills from
the global Claude config are skipped where that config is absent, as on CI.

Run: uv run --with pytest pytest -q tests/
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "build_codex_skills.py"

spec = importlib.util.spec_from_file_location("build_codex_skills", SCRIPT)
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


def test_committed_wrappers_match_their_sources():
    result = subprocess.run([sys.executable, str(SCRIPT), "--check"], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_every_command_wrapper_is_committed_and_named_after_its_folder():
    for name, (kind, _) in build.ITEMS.items():
        if kind == "skill":
            continue
        _, _, _, wrapper = build.source_paths(name, kind)
        assert wrapper.is_file(), f"{wrapper} missing; run scripts/build_codex_skills.py"
        assert build.frontmatter(wrapper.read_text(encoding="utf-8")).get("name") == name


def test_every_agent_has_a_codex_toml_that_parses():
    import tomllib

    for source in sorted((REPO / "agents").glob("*.md")):
        target = REPO / ".codex" / "agents" / f"{source.stem}.toml"
        assert target.is_file(), f"{target} missing; run scripts/build_codex_skills.py"
        data = tomllib.loads(target.read_text(encoding="utf-8"))
        assert data["name"] == source.stem
        assert data["description"]
        assert build.body(source.read_text(encoding="utf-8")).strip() in data["developer_instructions"]


def test_frontmatter_reads_block_scalars():
    text = "---\nname: x\ndescription: |\n  first line\n  second line\nmodel: opus\n---\nbody\n"
    fields = build.frontmatter(text)
    assert fields["description"] == "first line second line"
    assert fields["model"] == "opus"


def test_codex_wording_rewrites_commands_but_not_paths():
    text = "Use after /codex-loop or /quiz-me, not research/quiz-me.md or ~/humanizer/x"
    assert build.codex_wording(text) == "Use after $codex-loop or $quiz-me, not research/quiz-me.md or ~/humanizer/x"


def test_frontmatter_reads_quoted_and_plain_values():
    text = '---\ndescription: "A \\"quoted\\" one: here"\nargument-hint: plain\n---\nbody\n'
    fields = build.frontmatter(text)
    assert fields["description"] == 'A "quoted" one: here'
    assert fields["argument-hint"] == "plain"
