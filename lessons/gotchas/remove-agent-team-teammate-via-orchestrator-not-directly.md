---
id: remove-agent-team-teammate-via-orchestrator-not-directly
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
---

# Ask the Orchestrator to Remove an Unneeded Agent-Team Teammate, Don't Tear It Down Yourself

## TL;DR

If a teammate turns out unnecessary, tell the lead/orchestrator to clean it up rather than killing it directly, since the docs warn manual teardown outside the orchestrator's control can leave the team in a weird state.

## Why it matters

The orchestrator manages the team's shared task list and lifecycle; bypassing it to kill a teammate can produce inconsistent state or a memory leak.

## How to apply

Say something like you don't need the X teammate anymore, shut it down, to the orchestrator instead of using a raw kill on that teammate's pane or process.

## Related

[[shut-down-agent-teams-gracefully]]
