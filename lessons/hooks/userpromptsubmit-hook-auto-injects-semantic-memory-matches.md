---
id: userpromptsubmit-hook-auto-injects-semantic-memory-matches
created: 2026-09-01
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-memory-system-compared-so-you-don-t-have-to_20260424.txt
---

# Use a UserPromptSubmit Hook to Auto-Inject Top Semantic Memory Matches Into Every Prompt

## TL;DR

mem-search wires a UserPromptSubmit hook that, on every prompt you type, searches your memory files semantically and injects the top few matches into context automatically, without you asking Claude to search.

## Why it matters

Waiting for Claude to decide to search memory means relevant history often never surfaces; firing the search unconditionally on every prompt via a hook guarantees the lookup happens even when you forget to ask for it.

## How to apply

Wire a UserPromptSubmit hook that runs a semantic search over your memory/daily-note files and prepends the top few matches (mem-search uses the top 3) to the prompt context before Claude sees it.

## Related

[[semantic-hybrid-memory-search-with-reranking]]
