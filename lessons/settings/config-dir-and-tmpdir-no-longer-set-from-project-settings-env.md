---
id: config-dir-and-tmpdir-no-longer-set-from-project-settings-env
created: 2026-08-29
status: active
supersedes: null
category: settings
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Move CLAUDE_CONFIG_DIR and TMPDIR Out of Project settings.json env: They Are Ignored There Now

## TL;DR

As of 2.1.251, a project-level `.claude/settings.json` `env` block can no longer set `CLAUDE_CONFIG_DIR`, `CLAUDE_CODE_TMPDIR`, or `TMPDIR`/`TMP`/`TEMP`; those keys are silently ignored there and must live in shell, user, or managed settings.

## Why it matters

Teams commit a project `env` block precisely so every clone inherits it with no per-machine step. For these variables that route is now dead with no error: the session quietly falls back to the real config and temp locations, which can move state (and secrets handling) somewhere you did not intend.

## How to apply

Grep your repos for `CLAUDE_CONFIG_DIR`, `CLAUDE_CODE_TMPDIR`, `TMPDIR`, `TMP`, and `TEMP` inside `.claude/settings.json` `env` blocks, and relocate them to `~/.claude/settings.json` or the shell profile. Other env keys in project settings still apply.

> "Changed project-level `.claude/settings.json` `env` to no longer set `CLAUDE_CONFIG_DIR`, `CLAUDE_CODE_TMPDIR`, or `TMPDIR`/`TMP`/`TEMP`; set them in your shell, user, or managed settings instead", Claude Code CHANGELOG 2.1.251
