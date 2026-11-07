---
id: override-the-300-second-webfetch-deadline-when-a-fetch-must-wait
created: 2026-09-13
status: active
supersedes: null
category: configuration
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Set `CLAUDE_CODE_WEBFETCH_DEADLINE_MS` When a Fetch Legitimately Needs Longer Than 5 Minutes

## TL;DR

WebFetch now fails after 300 seconds instead of hanging forever, and `CLAUDE_CODE_WEBFETCH_DEADLINE_MS` changes that deadline (`0` disables it).

## Why it matters

This is a new default that can truncate a workflow which used to work: a slow report endpoint or a streaming API now gets cut off at five minutes. Without knowing the deadline exists you would debug the endpoint rather than the client.

## How to apply

Export `CLAUDE_CODE_WEBFETCH_DEADLINE_MS=<milliseconds>` before a session that must wait longer, or `0` to remove the deadline. Verified present in the installed 2.1.270 binary (4 occurrences).

> "Fixed WebFetch hanging indefinitely on a server that keeps the response open without finishing; a fetch now fails after 300 seconds. Set `CLAUDE_CODE_WEBFETCH_DEADLINE_MS` to override the deadline (0 turns it off)", Claude Code CHANGELOG 2.1.268
