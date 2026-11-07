---
id: search-cross-project-session-history-in-natural-language
created: 2026-09-01
status: active
supersedes: null
category: memory
tool: claude-code
sources:
  - transcripts/simon-scrapes/you-re-using-claude-code-wrong-these-10-tips-will-change-everything_20260307.txt
---

# Ask Claude to Summarize Cross-Project Session History Instead of Searching Manually

## TL;DR

You can ask Claude Code in plain language what you discussed across all your projects recently and get a per-project breakdown, rather than manually grepping the session-history store.

## Why it matters

The speaker notes Claude Code's history 'lives in this Claude projects global file' and that you can search it manually via the command line, 'but just to be honest, ask Lord Code to do it for you because it's much quicker.' Asking directly returns which projects had activity, session counts, and a summary of each, then supports drilling into a specific topic.

## How to apply

In any session ask something like 'What have we spoken about in the last week in all my projects? Give me a summary.' Claude reads the global project/session history and reports which projects had recent activity plus a summary per session. Follow up with 'tell me more about X' (naming a project or topic) to restore that context into the current conversation.

