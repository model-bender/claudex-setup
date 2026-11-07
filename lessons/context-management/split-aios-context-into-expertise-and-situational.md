---
id: split-aios-context-into-expertise-and-situational
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/5-hacks-to-instantly-level-up-your-ai-os_Ek1NBfnnTH0_20260724.txt
---

# Split an AI Operating System's Knowledge Into Always-Loaded Expertise Context and Just-in-Time Situational Context

## TL;DR

Keep identity, goals, and policies (expertise context) always in the agent's context like a system prompt, but fetch per-task facts (situational context, e.g. one customer's ticket) only when a task actually needs them.

## Why it matters

Preloading situational data that only matters for one task adds bloat, confusion, and clash risk for every other task the agent later handles.

## How to apply

Store expertise facts in a small always-loaded file, router or system-prompt style. For situational data, do a live lookup at the moment a task needs it rather than syncing it into the always-loaded store.

## Related

[[split-a-growing-knowledge-store-into-per-feed-wikis]]
