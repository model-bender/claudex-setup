---
id: set-claude-code-disable-file-mentions-to-pass-paths-not-contents
created: 2026-10-19
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21299
---

# Set CLAUDE_CODE_DISABLE_FILE_MENTIONS So @-Mentions Pass Paths Instead of Inlining File Contents

## TL;DR

With this env var set, an `@file` mention hands Claude the path to read with its file tools rather than pasting the whole file into the prompt.

## Why it matters

Inlined mentions put whole files into context each time, large ones included. Path-only mentions keep the prompt small and send the read through the normal Read tool and its permission rules.

## How to apply

Set `CLAUDE_CODE_DISABLE_FILE_MENTIONS=1` in the shell or in settings.json `env`, and keep using `@path` as a pointer. Checked: 8 hits in the 2.1.303 binary.

> "Added `CLAUDE_CODE_DISABLE_FILE_MENTIONS` environment variable: Claude gets the paths of `@` file mentions to read with its file tools, not the files' contents", Claude Code CHANGELOG 2.1.299
