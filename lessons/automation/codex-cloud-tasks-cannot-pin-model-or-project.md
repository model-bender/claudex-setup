---
id: codex-cloud-tasks-cannot-pin-model-or-project
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/i-turned-gpt-6-astra-into-a-24-7-stock-trader-tutorial_TLQLfa7yH4I_20260910.txt
---

# Keep a Codex Routine Local When the Model Matters, Cloud Tasks Cannot Set One

## TL;DR

Codex's cloud scheduled tasks keep running with the device offline but expose no chat, project, model or reasoning setting. The 'this device' option exposes all four.

## Why it matters

If the whole point of the routine is that it runs on a specific model at a specific reasoning level, the cloud option silently takes that choice away, which the creator hit directly when he needed the runs on a named model at high reasoning and had to switch back to local.

## How to apply

Choose 'this device' when the routine needs a specific project, thread, model or reasoning level, and accept that it only fires while the machine is awake. Use cloud tasks for work where any capable model will do and uptime matters more.

## Related

[[point-every-scheduled-task-at-one-codex-thread]]
