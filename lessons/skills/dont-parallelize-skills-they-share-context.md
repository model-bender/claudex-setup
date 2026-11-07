---
id: dont-parallelize-skills-they-share-context
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/ray-amjad/better-than-mcps-claude-code-s-new-skills-feature_20260307.txt
---

# Don't Try to Run Skills in Parallel: They Share the Main Context Window

## TL;DR

Because skills execute as tools inside the same session, running several in parallel quickly fills up that one context window; use subagents instead when you need true parallel work.

## Why it matters

Ray Amjad notes Claude Code can run many tools in parallel and skills are essentially tools, but doing this with skills 'will quickly fill up the context window and then it will basically be unusable.'

## How to apply

Chain skills sequentially within a session; reach for subagents (each with their own independent context) when the work genuinely needs to happen in parallel.

