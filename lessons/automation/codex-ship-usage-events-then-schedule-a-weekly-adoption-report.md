---
id: codex-ship-usage-events-then-schedule-a-weekly-adoption-report
created: 2026-11-06
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/ray-amjad/the-new-codex-update-that-manages-all-your-agents_3aMWv9FIu4o_20261106.txt
---

# After Shipping a Feature in Codex, Add Usage Events and a Weekly Automation That Reports Adoption in Slack

## TL;DR

In the shipping thread, ask Codex to add PostHog events for the feature, then after merge set an automation to message you weekly on Slack about usage. If nobody uses it, open a PR to remove it.

## Why it matters

Ray's worry is shipping features nobody uses or that cause later regressions. A thread automation keeps the thread's context, and Slack acts as his command center across projects.

## How to apply

1. In the thread: add PostHog events that measure how this feature is used.
2. After merging, create an automation in that same thread to Slack-message a weekly usage summary.
3. When the numbers show no use, ask the thread to open a PR removing the feature.

