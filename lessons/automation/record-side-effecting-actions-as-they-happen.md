---
id: record-side-effecting-actions-as-they-happen
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/i-turned-gpt-6-astra-into-a-24-7-stock-trader-tutorial_TLQLfa7yH4I_20260910.txt
---

# Log Each Side-Effecting Action the Moment It Happens, Not at the End of the Run

## TL;DR

If a scheduled run can place an order, send an email or move money, write the record at the moment of the call, so an interrupted run can be recovered without repeating the action.

## Why it matters

The failure list for the trading setup is explicit and mundane: a prior run crashed after sending an order, two runs overlapped, the machine went offline. An end-of-run log loses the fact that the irreversible thing already happened, and the next wake-up does it again.

## How to apply

Give the routine an append-only journal and require a write immediately after each irreversible call, before any further work. Make the startup step reconcile the journal against the real system (the account, the outbox, the API) rather than trusting its own notes, and brainstorm the failure list with the agent up front so the protocol covers overlap and corruption too.

## Related

[[end-every-scheduled-run-with-a-handoff-naming-the-next-job]], [[set-once-true-to-prevent-duplicate-hook-runs]]
