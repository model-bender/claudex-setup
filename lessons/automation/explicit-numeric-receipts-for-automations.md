---
id: explicit-numeric-receipts-for-automations
created: 2026-07-17
status: active
supersedes: null
category: automation
sources:
  - transcripts/austin-marchese/how-anthropic-engineers-actually-automate-their-work_3Y6kVI3fR9c_20260715.txt
---

# Make Automation Receipts Report Exact Counts, Not Vague Confirmations

## TL;DR

End every automated or proactive run with an explicit numeric receipt ("141 emails reviewed, 4 drafted, 12 skipped") rather than a vague "emails reviewed", the number is a cheap tripwire that instantly flags when the job did too little or too much.

## Why it matters

A proactive system you don't sit and watch drifts silently, and a vague "done" hides whether it processed 3 items or 300, or gamed the task. Anthropic engineers separate the *receipt* (the outcome summary you skim) from the *trace* (the full transcript you audit on demand), and insist the receipt carry concrete numbers: "141 emails reviewed" instantly reads wrong when you know you only had ~30 unread, whereas "emails reviewed" tells you nothing.

## How to apply

In the skill/routine output spec, require counts and concrete values in the final summary, N processed, N acted on, N skipped and why, instead of adjectives. When a number looks off, open that run's trace/conversation history, find where it went wrong, and feed the exact excerpt back to Claude ("you did X here, should have done Y, update the skill so it never repeats"). Keep the receipt short and the trace one click away.

## Related

[[audit-agent-transcripts-dont-trust-the-success-claim]], [[guard-unattended-agent-runs-with-a-stall-watchdog-and-bounded-retry]]
