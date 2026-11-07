---
id: make-delegated-workers-write-progress-back-to-the-plan
created: 2026-09-12
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
---

# Require Every Delegated Worker to Write Its Progress Back to the Plan Document

## TL;DR

Give the orchestrator the plan document as the single source of truth and require each delegated worker to write its progress back into it (or into its own status folder), so the orchestrator tracks state by reading the plan instead of re-reading the codebase.

## Why it matters

An orchestrator that reconstructs what happened by reading code pays full context cost for every status check, which is the cost the pure-delegator pattern exists to avoid in the first place. Routing worker reports into a shared document turns each status check into one small read. It also survives the orchestrator's own context reset, because the state lives on disk rather than in the conversation, so a compaction or a clear does not lose the record of what is done. The instruction currently sits inside a lesson titled about one model's weekly usage cap, so it never surfaces for anyone looking for orchestration mechanics.

## How to apply

In the orchestrator's first prompt, name the plan document as the source of truth and state the reporting requirement: every worker appends what it completed, what it changed, and anything blocked, either into the plan or into its own status folder. Have the orchestrator consult that record rather than the diff when deciding the next step. Leave the parallelisation mechanism (subagents, agent teams, worktrees) to the orchestrator rather than prescribing it.

## Related

[[delegate-all-execution-off-fable-to-preserve-its-separate-weekly-cap]]
