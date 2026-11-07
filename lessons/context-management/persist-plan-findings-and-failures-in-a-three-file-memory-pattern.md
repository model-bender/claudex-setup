---
id: persist-plan-findings-and-failures-in-a-three-file-memory-pattern
created: 2026-07-10
status: active
supersedes: null
category: context-management
sources:
  - transcripts/sean-kochel/5-claude-code-tools-that-make-vibe-coders-cry-tears-of-joy_QK0B1mbJ-VU_20260703.txt
---

# Persist Plan, Findings, and Failures in a Three-File Memory Pattern That Survives Context Resets

## TL;DR

Adopt a Manus-style three-file memory system, one file tracking phases/progress, one storing research and findings, one logging each session's results and errors, updated on a two-action cadence, so a context reset loses neither your findings nor the record of what already failed.

## Why it matters

Claude's built-in to-do state evaporates on every context reset, causing the todo list to vanish, goal drift as tool calls pile up, and repeated failures because nothing tracked that an approach already didn't work; persisting findings and failures (not just the plan) to durable files fixes all three and makes long research/build tasks resumable.

## How to apply

Have the agent create a plan broken into phases, and every ~two operations save what it just found to the findings file and append any errors to the log; when you want to go deeper, re-invoke it and it reads the existing findings and appends new phases rather than restarting, reach for this on multi-session research or builds, especially when you're not using a spec-driven tool that already tracks state.
