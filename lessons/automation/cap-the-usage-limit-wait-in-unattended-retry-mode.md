---
id: cap-the-usage-limit-wait-in-unattended-retry-mode
created: 2026-10-19
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21301
---

# Cap How Long Unattended Retry Mode Waits for a Usage Limit With CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS

## TL;DR

With `CLAUDE_CODE_RETRY_WATCHDOG` on, this variable ends a request at a usage limit that resets too far away instead of waiting for it.

## Why it matters

The existing max-wait variable covers 429 and 529 retries. A plan usage limit that resets many hours later is a separate wait, and without a cap an overnight job sleeps instead of failing where the calling script can see it.

## How to apply

Set `CLAUDE_CODE_RETRY_WATCHDOG=1` and `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS=<ms>`, and handle the ended request in the calling script. Checked: 5 hits in the 2.1.303 binary.

> "Added `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS` so unattended retry mode (`CLAUDE_CODE_RETRY_WATCHDOG`) ends a request at a usage limit that resets too far away instead of waiting", Claude Code CHANGELOG 2.1.301

## Related

[[cap-unattended-retry-waits-with-claude-code-retry-watchdog-max-wait-ms]], [[autocontinue-at-usage-limit-resumes-the-task-after-reset]]
