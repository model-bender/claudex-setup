---
id: websearch-budget-now-refills-hourly-instead-of-ending-at-200
created: 2026-10-11
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Stop Restarting Research Sessions for WebSearch: the Budget Now Refills at 100 Calls an Hour

## TL;DR

Since 2.1.290 the interactive WebSearch budget refills over time (100 calls an hour) instead of ending after 200 calls; `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` sets the rate and 0 turns refills off.

## Why it matters

Long research sessions used to hit a hard wall and need a restart. Now they throttle instead, so the old workaround is unnecessary.

## How to apply

Leave the default for research-heavy sessions, or set `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` in the `env` block to change the rate. Checked: the variable has 5 hits in the 2.1.296 binary.

> "Changed the interactive session's WebSearch budget to refill over time (100 calls/hour; `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` sets the rate, 0 turns it off) instead of ending after 200 calls", Claude Code CHANGELOG 2.1.290
