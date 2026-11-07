---
id: contract-first-parallel-waves-avoid-subagent-merge-conflicts
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-made-codex-and-claude-code-build-the-same-app-one-clearly-won_WCrnS09vpfo_20260820.txt
---

# Agree Interfaces First, Then Split Implementation Into Parallel Waves, to Get Zero Merge Conflicts Across Sub-Agents

## TL;DR

In a large autonomous build, structuring the work as contract-first (agreeing interfaces and schemas before implementation) and then dividing it into parallel waves of sub-agents produced zero merge conflicts.

## Why it matters

Parallel sub-agents that implement against a shared, already-agreed contract don't collide on shape or shared files the way agents improvising interfaces on the fly would.

## How to apply

Before fanning out parallel sub-agents on a big build, settle the interfaces/contracts each piece depends on first, then split the actual implementation into waves of sub-agents that build against that fixed contract.

## Related

[[agent-teams-agent-should-not-touch-same-files]]
