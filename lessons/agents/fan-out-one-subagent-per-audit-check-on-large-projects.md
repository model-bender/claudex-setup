---
id: fan-out-one-subagent-per-audit-check-on-large-projects
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/5-hacks-to-instantly-level-up-your-ai-os_Ek1NBfnnTH0_20260724.txt
---

# Fan Out One Explore Subagent Per Audit Check When a Project Has 100+ Folders

## TL;DR

For a knowledge-base audit skill running against a large project, spawn one Explore subagent per check (routing integrity, index truth, freshness, etc.), handing each the check's instructions verbatim plus the project root, then merge their reports.

## Why it matters

A single sequential pass over a 100+ folder project is slow and risks missing things; partitioning by check lets each subagent focus with full context on one narrow question.

## How to apply

In the audit skill's instructions, add a size threshold (e.g. 100+ folders) that triggers fan-out: one subagent per check, verbatim check text plus project root as its prompt, then the orchestrator merges all subagent reports into one.

## Related

[[audit-knowledge-base-claims-against-disk-read-only]]
