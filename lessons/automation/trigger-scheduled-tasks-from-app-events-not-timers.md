---
id: trigger-scheduled-tasks-from-app-events-not-timers
created: 2026-08-29
status: active
supersedes: null
category: automation
source_type: canonical
tool: codex
sources:
  - https://developers.openai.com/codex/changelog
---

# Trigger Scheduled Tasks From Gmail, Slack, and GitHub Events Instead of Polling on a Timer

## TL;DR

ChatGPT scheduled tasks now support event triggers (Gmail sender/subject filters, watched Slack channels, PR reviews/comments/commits/merges), replacing cron-style polling for reactive automations.

## Why it matters

Polling automations burn runs checking for nothing and react late; an event trigger fires on the actual PR review or email. Two constraints from the linked task docs are non-obvious: an event-triggered task cannot also keep a time-based schedule, and near-simultaneous events may be coalesced into a single run.

## How to apply

In ChatGPT web or mobile, connect the app, then create a scheduled task with an event trigger (a Gmail sender/subject filter, a Slack channel the ChatGPT app has been added to, or a repo the GitHub app can access); review pending events under Scheduled.

> "ChatGPT scheduled tasks can now run when supported events occur in Gmail, Slack, or GitHub.", ChatGPT & Codex changelog, 2026-08-25

## Related

[[wire-cloud-scheduled-tasks-through-connectors-not-local-files-or-keys]], [[managed-agents-for-webhook-triggered-automation]]
