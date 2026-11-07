---
id: cap-unattended-retry-waits-with-claude-code-retry-watchdog-max-wait-ms
created: 2026-10-11
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Cap How Long Unattended Retry Mode Waits Out 429 and 529 Errors

## TL;DR

With `CLAUDE_CODE_RETRY_WATCHDOG` on, unattended runs wait out rate-limit and overload errors with no upper bound; since 2.1.295 `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS` sets one.

## Why it matters

A scheduled or `claude -p` run that sits in retry for hours holds its slot and hides the failure from whatever scheduled it.

## How to apply

Set `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS` (for example 1800000 for 30 minutes) alongside `CLAUDE_CODE_RETRY_WATCHDOG`, so the run fails and the scheduler can try again later. Checked: the variable has 5 hits in the 2.1.296 binary.

> "Added `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS` to limit how long unattended retry mode (`CLAUDE_CODE_RETRY_WATCHDOG`) waits out 429 and 529 errors", Claude Code CHANGELOG 2.1.295

## Related

[[guard-unattended-agent-runs-with-a-stall-watchdog-and-bounded-retry]]
