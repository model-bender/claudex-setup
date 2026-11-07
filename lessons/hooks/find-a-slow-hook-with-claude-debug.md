---
id: find-a-slow-hook-with-claude-debug
created: 2026-10-11
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Find a Slow Hook With claude --debug: Finished Hooks Now Log Their Duration

## TL;DR

Since 2.1.296 `--debug` logs the command, plugin, outcome and duration of command hooks on tool calls, prompts, SessionStart and Stop when they finish.

## Why it matters

A slow SessionStart or PreToolUse hook adds delay to every session or tool call with no visible culprit.

## How to apply

Launch `claude --debug`, run the slow flow once, and read the hook lines for the longest duration. Checked: `--debug` has 103 hits in the 2.1.296 binary.

> "Improved `--debug` output for hooks: command hooks on tool calls, prompts, SessionStart and Stop now log their command, plugin, outcome and duration when they finish, so a slow hook is identifiable", Claude Code CHANGELOG 2.1.296
