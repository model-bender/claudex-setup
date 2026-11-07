---
id: end-every-scheduled-run-with-a-handoff-naming-the-next-job
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/i-turned-gpt-6-astra-into-a-24-7-stock-trader-tutorial_TLQLfa7yH4I_20260910.txt
---

# End Every Scheduled Run With a Handoff That Names the Exact Next Job

## TL;DR

Each wake-up of a recurring agent is stateless, so make the last step of every run append what changed, the actual outcomes, remaining risk, unresolved issues and the exact next job, and make the first step read that entry. Write it even on a run that did nothing.

## Why it matters

Continuity comes from shared records, not from the model remembering the conversation. Without the baton the sequence behaves like a crowd of isolated workers re-deriving the situation every time, which the creator describes as throwing darts at a wall. The no-op run is exactly the one whose successor needs to know why nothing happened.

## How to apply

Give the routine a progress log and a shared startup and end-of-run protocol: read the strategy document and the previous handoff, check the external system for what actually happened, do the assigned job, update state, and leave instructions for the next wake-up. State in the prompt that the handoff is written on failed and no-op runs too.

## Related

[[routines-with-claude-generated-prompts]], [[write-the-handoff-as-a-prompt-for-the-next-session]]
