---
id: set-the-retry-watchdog-usage-limit-recheck-for-unattended-runs
created: 2026-10-25
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21305
---

# Set CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS So Unattended Retry Mode Notices a Lifted Usage Limit

## TL;DR

With unattended retry mode (`CLAUDE_CODE_RETRY_WATCHDOG`) on, a run waiting out a usage limit can now re-check on an interval and resume when the limit lifts before its stated reset.

## Why it matters

Without the re-check, an unattended job that hits a limit sleeps until the reset time even when capacity comes back sooner, so the run finishes later than it needs to.

## How to apply

Next to `CLAUDE_CODE_RETRY_WATCHDOG=1`, set `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS` to a re-check interval in milliseconds, and keep any maximum-wait cap you already use as the outer bound. Checked: 4 matches in the installed 2.1.310 binary; the changelog gives no default.

> "Added `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS` so unattended retry mode (`CLAUDE_CODE_RETRY_WATCHDOG`) notices a usage limit that was lifted before its reset", Claude Code CHANGELOG 2.1.305

## Related

[[cap-the-usage-limit-wait-in-unattended-retry-mode]]
