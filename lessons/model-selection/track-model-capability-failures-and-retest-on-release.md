---
id: track-model-capability-failures-and-retest-on-release
created: 2026-09-01
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Keep a Doc of Prompts Claude Code Couldn't Do, and Retest Them on Every New Model Release

## TL;DR

Log the specific tasks Claude Code failed at into a separate document, then re-try each one whenever a new model ships.

## Why it matters

The speaker notes his biggest limitation is stale assumptions: people try something once, it fails, and they never retry even though a new model gets 80-95% of the way there. Without a written log, you have no reliable trigger to revisit.

## How to apply

Keep a running document of tasks/prompts Claude Code couldn't complete. On each new model release, replay each logged prompt against the new model before assuming the limitation still holds.

