---
id: point-every-scheduled-task-at-one-codex-thread
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/i-turned-gpt-6-astra-into-a-24-7-stock-trader-tutorial_TLQLfa7yH4I_20260910.txt
---

# Point a Family of Codex Scheduled Tasks at One Named Thread

## TL;DR

When several routines are stages of one job, create a project, open a thread, rename it, and set every scheduled task to run inside that chat rather than each spawning its own.

## Why it matters

Tasks that share a thread share history and Codex's auto-compaction, so each stage starts warm instead of cold, and every run's messages land in one place tagged as sent from another task, which is the only practical way to read six runs a day. The creator set this up for six wake-ups plus two notification tasks.

## How to apply

Create the project and thread first and rename the thread, then tell Codex to create the tasks and choose that chat for each one, or select the chat manually in each task's settings. Keep the project folder scoped to just this job so unrelated context does not leak into it.

## Related

[[dedicated-lean-repo-per-cloud-routine]], [[end-every-scheduled-run-with-a-handoff-naming-the-next-job]]
