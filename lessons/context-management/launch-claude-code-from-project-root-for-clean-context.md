---
id: launch-claude-code-from-project-root-for-clean-context
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/john-kim/how-i-use-claude-code-meta-staff-engineer-tips_20260307.txt
---

# Launch Claude Code From the Project Root, Not a Subdirectory

## TL;DR

Start `claude` in the repo's root directory, because that is the working directory Claude zips into its very first context load.

## Why it matters

John Kim says the initial root directory is where Claude Code 'zips up the context into that first token,' and that unexplained token usage right after opening a session traces back to Claude preparing the project from wherever it was launched.

## How to apply

cd to the project root before running `claude`, especially in projects with rule files (CLAUDE.md, .claude/) that should apply globally rather than being scoped to whatever subfolder you happened to be in.

## Related

[[be-a-context-minimalist-provision-a-lean-harness]]
