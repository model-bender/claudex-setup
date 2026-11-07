---
id: agent-team-teammate-spawn-shown-by-colored-text
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
---

# Spot a Spawned Agent-Team Teammate by Its Colored Terminal Text

## TL;DR

When Claude Code spawns a sub-agent or agent-team teammate, its output renders in a distinct color in the terminal, which is the quickest way to tell a delegation actually happened.

## Why it matters

Without this visual cue it's easy to miss that work was delegated rather than done inline by the main session.

## How to apply

Watch for a colored block of text appearing mid-session; that block is a spawned sub-agent or teammate, not the main orchestrator.
