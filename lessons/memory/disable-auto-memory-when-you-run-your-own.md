---
id: disable-auto-memory-when-you-run-your-own
created: 2026-07-17
status: active
supersedes: null
category: memory
sources:
  - transcripts/simon-scrapes/stop-using-fable-5-in-claude-code-it-s-holding-you-back_d9XCX0PcOq0_20260712.txt
---

# Turn Off Built-In Auto-Memory if You Already Run Your Own Memory System

## TL;DR

Claude Code's auto-memory does a background extraction pass over your session to pull out project memories; if you already run a custom or external memory system doing the same job, disable auto-memory so you're not paying for redundant background work every session.

## Why it matters

Auto-memory and a hand-rolled memory system overlap, both scan the session to capture what should persist. Running both means duplicated background extraction with no added benefit, and (as with any injected memory) built-in auto-memory can also bleed stale or wrong-project context into a session you're deliberately keeping clean. If your own system is the source of truth, the built-in one is pure overhead.

## How to apply

Only after your own memory system is working, disable Claude Code's auto-memory from the `/memory` settings. Keep it on if you have no external system, you'd lose the built-in capture and gain nothing. This is the "disable it entirely" end of the same dial as another lesson (which turns *use* off while still generating, to measure value first).

## Related

[[markdown-wiki-knowledge-base-over-vector-rag]]
