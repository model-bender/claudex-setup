---
id: read-the-status-problem-list-for-hook-matchers-that-never-match-and-broken-artifact-files
created: 2026-11-22
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21327
---

# Read the /status problem list to find hook matchers that never match and broken skill or agent files

## TL;DR

`/status` now lists silent config failures, including hook matchers that can never fire.

## Why it matters

A mis-typed matcher produces a hook that is wired correctly and does nothing, which no error ever reports.

## How to apply

After adding or editing a hook, skill, agent or sandbox setting, open `/status` and read the problem list before trusting it.

Checked: changelog only; `/status` is a built-in command and not exercised here

> "Added a list in `/status` of broken agent, skill, command and output style files, keybinding errors, an unavailable sandbox, ignored permission settings and hook matchers that never match", Claude Code CHANGELOG 2.1.327

## Related

[[a-guard-hook-that-cannot-match-or-serialize-now-blocks-the-call]]
