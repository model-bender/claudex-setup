---
id: claude-design-slash-clear-context-clearing-unverified
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-design-builds-beautiful-3d-websites-instantly-full-tutorial_TcFeSjwTo7g_20260624.txt
---

# Don't Trust /clear in Claude Design to Fully Reset Context

## TL;DR

Claude Design accepts a /clear command and replies that it's cleared, but there's no confirmation it actually purges the underlying context window rather than just the visible thread.

## Why it matters

The creator ran /clear in a long Claude Design thread and got a "cleared, we're ready for the next instruction" response but says outright, "I can't say with certainty that that actually clears all of this from the context window. I haven't seen for sure yet."

## How to apply

Don't rely on /clear alone to escape a long, polluted Claude Design thread; use the proven method instead, export the project/design system and reopen it in a fresh session.

## Related

[[export-and-restart-instead-of-iterating-in-one-long-claude-design-thread]]
