---
id: silently-index-conversations-on-sessionend-and-precompact-hooks
created: 2026-09-01
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-memory-system-compared-so-you-don-t-have-to_20260424.txt
---

# File and Index Conversation Data Silently via SessionEnd and PreCompact Hooks

## TL;DR

MemPalace-style verbatim memory systems file and index every conversation in the background using hooks on session end and right before compaction, not just at session start.

## Why it matters

If you only hook SessionStart, you capture nothing about what happened during or at the close of a session; SessionEnd and PreCompact are the moments where the content worth indexing actually exists.

## How to apply

Register hooks on SessionEnd (to file the just-finished conversation) and PreCompact (to capture what's about to be summarized away) that write conversation content into your indexed memory store, alongside any SessionStart hook you already use for injection.
