---
id: add-an-allow-rule-for-pyright-it-is-no-longer-treated-as-read-only
created: 2026-10-11
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Add an Allow Rule for pyright if a Loop Runs It: Bash Now Asks Before Running It

## TL;DR

Since 2.1.290 the Bash tool asks for permission before running `pyright`, which is no longer treated as a read-only command.

## Why it matters

An unattended loop that uses pyright as a type-check gate now stalls on a permission prompt with no obvious cause.

## How to apply

In trusted projects, add an allow rule for it in a settings file you control (for example `Bash(pyright *)`), then run the loop once to confirm no prompt appears. Checked: `pyright` has 40 hits in the 2.1.296 binary.

> "Changed the Bash tool to ask for permission before running `pyright`, which is no longer treated as a read-only command", Claude Code CHANGELOG 2.1.290
