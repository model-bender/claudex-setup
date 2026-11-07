---
id: insert-a-planning-phase-between-research-and-build-in-autonomous-prompts
created: 2026-08-31
status: active
supersedes: null
category: prompting
tool:
  - claude-code
  - codex
sources:
  - transcripts/nate-herk-ai-automation/i-made-codex-and-claude-code-build-the-same-app-one-clearly-won_WCrnS09vpfo_20260820.txt
---

# Insert a Planning and Mapping Phase Between Research and Build in Long Autonomous Prompts

## TL;DR

Whatever the harness, do not let a long unattended prompt go straight from research to build: write an explicit planning and mapping phase between them, and check the run's scope early rather than at the end.

## Why it matters

In a head-to-head test of the same autonomous app build, both the Claude Code run and the Codex run drifted in scope, and the creator's retrospective pinned it on going directly from research to build. An explicit intermediate phase forces the run to consolidate what research found into a scoped plan before code starts. A run that has already spawned a hundred subagents has already made the scope decision for you, so the checkpoint has to come early.

## How to apply

When writing a long autonomous or orchestrator prompt, define the phases explicitly and place a planning and mapping phase between the research phase and the build phase. Then inspect the resulting scope early in the run instead of discovering the sprawl at the end.

## Related

[[shape-the-prompt-to-the-harness-goal-for-claude-code-steps-for-codex]]
