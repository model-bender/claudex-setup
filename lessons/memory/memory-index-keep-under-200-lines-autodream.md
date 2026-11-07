---
id: memory-index-keep-under-200-lines-autodream
created: 2026-09-01
status: active
supersedes: null
category: memory
tool: claude-code
sources:
  - transcripts/simon-scrapes/the-only-claude-code-updates-you-need-to-know-apr-2026_20260424.txt
---

# Auto-Dream Keeps Your memory.md Index Under 200 Lines on Purpose

## TL;DR

Auto-dream's memory consolidation specifically targets keeping the memory.md index file under 200 lines, because that file loads at every session startup and every token spent on it is a token not spent on actual work.

## Why it matters

A memory index is only useful if it stays small enough to be cheap to load every session; without an explicit size target it will grow indefinitely as more sessions add notes.

## How to apply

If you maintain your own memory index file (rather than relying purely on auto-dream), apply the same 200-line ceiling deliberately, prune or move detail into per-topic files linked from the index rather than letting the index itself grow.

## Related

[[auto-dream-memory-consolidation]]
