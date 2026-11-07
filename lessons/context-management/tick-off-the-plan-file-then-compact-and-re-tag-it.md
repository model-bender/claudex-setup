---
id: tick-off-the-plan-file-then-compact-and-re-tag-it
created: 2026-09-12
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
  - transcripts/simon-scrapes/the-only-claude-code-updates-you-need-to-know-apr-2026_20260424.txt
---

# Tick Completed Items Off the Plan File, Compact, Then Re-Tag the Plan

## TL;DR

On a long multi-step build, periodically ask Claude to mark the finished items in the plan file as done, compact the conversation, then re-tag the plan file and continue, so the plan carries the state forward instead of the transcript.

## Why it matters

Compaction decides on its own what to keep, and a plan is exactly the kind of structured state a summariser flattens. Writing progress into the plan file before compacting moves the state out of the transcript, so what survives is a file you control rather than a summary you do not, and re-tagging the file after the compaction restores it at full fidelity for free. It is the cheapest version of a handoff: no new session, no paste-back, just a durable artifact and one @-mention. The technique currently sits inside a lesson whose title and TL;DR are about a context ceiling, so a reader looking for a long-build loop never finds it.

## How to apply

Keep a plan file in the repository. Every so often during a long build, ask Claude to tick off the plan items it has actually completed, run /compact, then @-mention the plan file again in the next message so the freshly compacted session reads it in full. Repeat rather than letting the session run to the edge of the window.

## Related

[[cap-1m-context-usage-around-200k-tokens-to-avoid-context-anxiety]]
