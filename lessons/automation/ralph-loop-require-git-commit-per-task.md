---
id: ralph-loop-require-git-commit-per-task
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/sean-kochel/how-to-run-a-ralph-loop-step-by-step_7TwIrPQnFfg_20260702.txt
---

# Require a Git Commit Per Completed Ralph Loop Task for a Reviewable Audit Trail

## TL;DR

Ralph loop tools don't commit per task by default; explicitly instruct the loop to generate a git commit after each completed task so there's a running, inspectable log of exactly what changed and why.

## Why it matters

Without a commit per task, a long unattended loop leaves you no way to trace which change caused a regression or to understand its reasoning after the fact; a per-task commit gives the loop (and you) a checkpoint it can reference later.

## How to apply

When defining or editing the loop's task list before starting it, add an explicit acceptance-criteria line to every task: 'commit your changes with a descriptive message once this task passes.' Verify the resulting log has one commit per task before trusting the loop for longer runs.

## Related

[[autonomous-ui-loop-acceptance-must-exercise-rendered-ui]], [[run-true-ralph-loops-with-ralph-tui-or-a-bash-script]]
