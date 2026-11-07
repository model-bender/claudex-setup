---
id: set-claude-code-disable-attachments-in-user-or-shell-settings
created: 2026-10-11
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Set CLAUDE_CODE_DISABLE_ATTACHMENTS in Shell, User or Managed Settings: a Repo Settings File Can No Longer Set It

## TL;DR

Since 2.1.290 a repository's `.claude/settings.json` or `.claude/settings.local.json` cannot set `CLAUDE_CODE_DISABLE_ATTACHMENTS`; only the shell, user settings and managed settings can.

## Why it matters

A project that set this variable in its own settings file silently loses the effect after upgrading, with no error.

## How to apply

Move the variable to the `env` block of `~/.claude/settings.json`, your shell profile, or managed settings. Checked: `CLAUDE_CODE_DISABLE_ATTACHMENTS` has 11 hits in the 2.1.296 binary.

> "Changed `CLAUDE_CODE_DISABLE_ATTACHMENTS` so a repository's `.claude/settings.json` or `.claude/settings.local.json` can no longer set it; shell, user and managed settings still can", Claude Code CHANGELOG 2.1.290
