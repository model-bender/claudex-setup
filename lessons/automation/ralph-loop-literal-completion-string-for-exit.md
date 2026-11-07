---
id: ralph-loop-literal-completion-string-for-exit
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/sean-kochel/how-to-run-a-ralph-loop-step-by-step_7TwIrPQnFfg_20260702.txt
---

# Give a Ralph Loop a Single Literal Completion String as Its Only Exit Condition

## TL;DR

A Ralph loop should only be allowed to stop when it prints one specific, literal word (e.g. 'complete'), checked by the outer wrapper after it re-verifies every task's acceptance criteria; anything else sends it back to the start with a fresh context window.

## Why it matters

A deterministic, greppable exit signal is what lets a wrapper script or tool reliably decide whether to relaunch the loop instead of guessing from free-form output; without it, the loop has no unambiguous way to communicate 'actually done' versus 'stopped for some other reason'.

## How to apply

When designing or configuring the loop, define the completion criterion as a single literal string that the model must print only once it has re-checked that every task's acceptance criteria pass. Have the driving script or tool grep for that exact string to decide whether to exit or relaunch with a clean context.

## Related

[[run-true-ralph-loops-with-ralph-tui-or-a-bash-script]], [[loops-as-abstraction-over-prompts]]
