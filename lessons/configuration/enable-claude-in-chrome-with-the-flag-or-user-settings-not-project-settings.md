---
id: enable-claude-in-chrome-with-the-flag-or-user-settings-not-project-settings
created: 2026-10-11
status: active
supersedes: null
category: configuration
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Turn On Claude in Chrome With --chrome, /chrome or User Settings: Project Settings Can No Longer Enable It

## TL;DR

Since 2.1.290 a project's settings files cannot turn Claude in Chrome on; use the `--chrome` flag, the `/chrome` command, or your user settings.

## Why it matters

A checked-in project setting that used to enable the browser tools for everyone now does nothing, silently. It also means a cloned repo cannot open a browser connection on its own.

## How to apply

Launch with `claude --chrome`, run `/chrome` in the session, or set it in `~/.claude/settings.json`. Checked: `--chrome` has 22 hits in the 2.1.296 binary.

> "Changed Claude in Chrome so that a project's settings files can no longer turn it on; use `--chrome`, `/chrome` or your user settings", Claude Code CHANGELOG 2.1.290
