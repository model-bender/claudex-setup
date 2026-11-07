---
id: change-permission-mode-mid-task-with-permissions
created: 2026-09-12
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Run /permissions Mid-Task to Change Mode Without Rerunning the Work

## TL;DR

/permissions overrides the running session's mode from that point on, so when you see a task heading for an action it cannot take, switch mode or add a rule in place rather than aborting and starting again with the right settings.

## Why it matters

The expensive failure is discovering halfway through a long task that the mode is wrong, then rebuilding all that context in a fresh run just to get past a permission. Changes made mid-session apply to everything that follows, so the work continues from where it stopped.

## How to apply

Run /permissions during the task, switch between allow, ask and auto, or add a specific allow rule for the tool it is about to reach for, then let the same turn carry on.

