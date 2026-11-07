---
id: give-orchestrator-broad-goals-not-narrow-checklists
created: 2026-07-10
status: active
supersedes: null
category: agents
sources:
  - transcripts/mark-kashef/anthropic-s-new-claude-architect-guide-in-39-minutes_vizgFWixquE_20260704.txt
---

# Give the Orchestrator Agent Broad Goals, Not a Narrow Checklist

## TL;DR

A coordinator/main agent that decomposes a task too narrowly makes its subagents miss whole categories even when each subagent does its job perfectly - e.g. 'research AI in creative industries' becomes only visual-arts subtasks, silently dropping music, writing, film, and games; give the orchestrator a broad goal and let the subagents figure out the breakdown.

## Why it matters

The failure isn't in the workers - it's a bad manager scoping the work wrong, so the output looks complete but has systematic blind spots. Over-specified decomposition caps coverage at the orchestrator's own blind spots instead of expanding it.

## How to apply

Prompt the lead agent with the broad outcome and constraints and explicitly instruct it to let subagents determine their own sub-scopes rather than assigning a narrow checklist. Spot-check that the spawned subtasks span the full problem space instead of clustering in one sub-area before letting them run.
