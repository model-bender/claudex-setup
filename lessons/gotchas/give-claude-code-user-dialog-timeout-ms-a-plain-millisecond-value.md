---
id: give-claude-code-user-dialog-timeout-ms-a-plain-millisecond-value
created: 2026-10-11
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Write CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS as Plain Milliseconds, Not a Value With a Unit

## TL;DR

A unit-suffixed value such as `5m` used to be read as 5 ms and cancel remote dialogs at once; since 2.1.290 it falls back to the `dialogExpiry` setting, so it still does not mean five minutes.

## Why it matters

Either way the suffix form does not give the timeout you wrote, and the failure looks like dialogs that expire for no reason.

## How to apply

Write the value in milliseconds (300000 for five minutes), or set `dialogExpiry` instead. Checked: `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS` and `dialogExpiry` each have 7 hits in the 2.1.296 binary.

> "Fixed `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS=5m` being read as 5 ms and cancelling remote dialogs at once; values with a unit suffix now fall back to `dialogExpiry`", Claude Code CHANGELOG 2.1.290
