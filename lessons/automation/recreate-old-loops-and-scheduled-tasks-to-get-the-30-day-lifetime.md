---
id: recreate-old-loops-and-scheduled-tasks-to-get-the-30-day-lifetime
created: 2026-11-22
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21330
---

# Recreate old scheduled tasks and loops to get the 30-day lifetime instead of 7 days

## TL;DR

Recurring tasks and /loop now last 30 days, but only for tasks created on or after 2.1.330.

## Why it matters

A loop you set up last week still dies at 7 days even after updating.

## How to apply

Re-create any long-running recurring task after updating to 2.1.330 or later, and note the end date Claude now states.

Checked: changelog only

> "Changed recurring scheduled tasks and `/loop` to run up to 30 days instead of 7 while their session keeps running, and say when they end; tasks made before this release still end at 7 days", Claude Code CHANGELOG 2.1.330
