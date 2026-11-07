---
id: batch-claude-design-comments-and-drawings-then-send-once
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-design
sources:
  - transcripts/austin-marchese/17-things-you-didn-t-know-claude-design-could-do_7rRVwjzVQsc_20260910.txt
---

# Queue Every Claude Design Comment and Drawing, Then Send Them All in One Pass

## TL;DR

Leave inline comments and circle regions with the draw tool across the whole design, click through the queued comments to check them, then hit Send to Claude once so the model fixes the batch together.

## Why it matters

Prompting one change at a time costs a generation round per fix and lets earlier edits drift while you describe the next one. Marchese reviews a whole page, attaches each note to the element it concerns (change the header to span two lines, move this graphic here), then sends the set, which is both fewer rounds and less ambiguity because every note is anchored to a position rather than described in prose.

## How to apply

On the rendered design, add a comment on each element you want changed and use the draw tool to circle anything positional. Click through the comment list to confirm nothing is half-typed (the draw comment box can hide your own text), then press Send to Claude once for the whole batch.

## Related

[[claude-design-draw-comment-input-obscured-bug]], [[draw-on-the-claude-design-canvas-only-for-things-that-arent-elements]], [[one-visual-change-per-claude-design-prompt]]
