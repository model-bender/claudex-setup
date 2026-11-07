---
id: teammate-model-change-restarts-whole-agent-team
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
---

# Changing a Teammate's Model Mid-Run Restarts the Entire Agent Team

## TL;DR

Asking to change which model a specific teammate runs on doesn't hot-swap just that teammate; it typically shuts down all current teammates and recreates the team.

## Why it matters

You lose any in-progress teammate state when you make a model change, so it's not a free, isolated adjustment.

## How to apply

Set the model you want for each teammate at team-creation time rather than mid-run, or accept the team will restart if you change it later.

## Related

[[agent-team-teammates-now-inherit-the-leader-s-model-name-the]]
