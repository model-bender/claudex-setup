---
id: lengthen-the-529-overloaded-backoff-for-parallel-runs
created: 2026-10-11
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Lengthen the 529 Overloaded Backoff for Heavy Parallel Runs

## TL;DR

`CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` (2.1.292) and `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` (2.1.296) set a longer base and maximum delay when retrying an overloaded (529) request.

## Why it matters

Many parallel agents retrying on the default schedule hit an overloaded API again together (inference); a longer backoff spreads them out.

## How to apply

For large fan-outs or scheduled batches, set both in the settings `env` block, raising the base first. Checked: the variables have 4 and 3 hits in the 2.1.296 binary; their defaults were not checked.

> "Added `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` environment variable to set a longer base delay for the backoff when retrying an overloaded (529) request", Claude Code CHANGELOG 2.1.292

> "Added `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` environment variable to set a longer maximum delay for the backoff when retrying an overloaded (529) request", Claude Code CHANGELOG 2.1.296
