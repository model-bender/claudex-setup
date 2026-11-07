---
id: modularize-files-over-500-lines-to-cap-context-cost-of-edits
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Ask Claude Code to Find and Split Every File Over 500 Lines

## TL;DR

Periodically ask Claude Code to identify all files over 500 lines and modularize them, because editing a file always requires reading it in full first.

## Why it matters

In one observed run, reading through several 700-line files before making any edit filled the context window to 47% before real work even started. Long files mean every future edit pollutes context before changes begin.

## How to apply

Ask: 'Can you identify all files that are over 500 lines and then make them smaller or modularize it more?' Run this periodically so future edits read shorter files and consume less context up front.
