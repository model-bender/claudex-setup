---
id: cloud-routines-run-at-most-hourly
created: 2026-11-22
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/jono-catliff/full-claude-code-masterclass-beginner-to-expert-in-2-hours-2026_R3mx8XHX8ns_20261002.txt
---

# Design cloud routines around an hourly minimum interval

## TL;DR

A scheduled cloud routine cannot run more often than once an hour, so do not plan a workflow that needs five or ten minute polling on it.

## Why it matters

The speaker sets the email triage to hourly and notes nothing shorter is offered.

## How to apply

Pick the hourly preset, or for another cadence select Custom in the task's edit dialog (or run `/schedule update`) and enter a cron expression no more frequent than hourly. Anything that needs faster reaction needs a different trigger: the docs list an API trigger (an HTTP POST to the task's endpoint) and GitHub event triggers.

Checked: Live docs at code.claude.com/docs/en/routines.md (fetched 2026-11-22): 'Expressions that run more often than once per hour are rejected.' The docs now call a routine a cloud scheduled task ('formerly a routine'). API fires share a cap of 30 per hour per task with Run now; that this makes the API trigger fit for reacting to events rather than for fast polling is this lesson's inference.

