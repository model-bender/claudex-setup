---
id: export-and-restart-instead-of-iterating-in-one-long-claude-design-thread
created: 2026-07-17
status: active
supersedes: null
category: context-management
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
  - transcripts/nate-herk-ai-automation/claude-design-builds-beautiful-3d-websites-instantly-full-tutorial_TcFeSjwTo7g_20260624.txt
---

# Export and Restart Rather Than Iterating in One Long Claude Design Thread

## TL;DR

Claude Design bills the whole accumulated thread every turn and eventually surfaces "Start a new chat to save 110,000 tokens of context". When it does, export the project and reopen it in a fresh one instead of pushing on.

## Why it matters

This is a real cause of the "my limit was gone in 20 minutes" complaints: a long project thread makes every subsequent prompt more expensive while the context rots and cached tokens go stale.

**Restarting isn't starting over**, the built artifact travels in the export; only the conversation is dropped.

Design has no compaction, and `/clear`'s actual effect on the context window is unverified.

## How to apply

Watch for the in-product "start a new chat to save N tokens of context" hint, it's the product telling you the thread is now the cost.

When iteration stalls or the thread gets long, export the project (zip or HTML), open a new project, attach the export, and continue on top of what's already built with fresh context.

## Related

[[plan-in-claude-chat-then-hand-claude-design-only-the-finished-spec]], [[attach-only-the-files-claude-design-needs]], [[precompute-the-design-system-outside-claude-design]]
