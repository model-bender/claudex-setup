---
id: strip-the-utf-8-bom-from-agent-skill-and-command-files-a-bom
created: 2026-08-22
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Strip the UTF-8 BOM From Agent, Skill, and Command Files: a BOM Silently Disables Them

## TL;DR

Until 2.1.239, an agent/skill/command .md file starting with a UTF-8 BOM was ignored with no error at all.

## Why it matters

This is the invisible-failure class that review never catches: the file exists, the frontmatter is valid, `claude plugin validate` passes on the content, and the artifact just never appears. Windows editors, PowerShell `Out-File`, and Excel-adjacent tooling all emit BOMs by default, so a file authored on Windows can be dead on arrival.

## How to apply

If an artifact never shows up, check for a BOM (`file x.md` or `head -c3 x.md | xxd`) and re-save as UTF-8 without BOM; upgrade to 2.1.239+ so it loads regardless.

> "Fixed agents, skills, and commands whose `.md` file starts with a UTF-8 BOM being silently ignored", canonical: Claude Code CHANGELOG 2.1.239
