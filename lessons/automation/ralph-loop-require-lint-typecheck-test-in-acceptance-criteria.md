---
id: ralph-loop-require-lint-typecheck-test-in-acceptance-criteria
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/sean-kochel/how-to-run-a-ralph-loop-step-by-step_7TwIrPQnFfg_20260702.txt
---

# Add Lint, Type-Check, and Test Runs to Every Ralph Loop Task's Acceptance Criteria

## TL;DR

By default a Ralph loop task can be marked done just because the files exist; explicitly require it to run linting, type-checking, and tests before accepting a task as complete, or it will happily mark broken code as finished.

## Why it matters

In this run, the loop's first pass introduced errors in a client file; because testing wasn't required, that error would have gone undetected and been carried forward into later tasks instead of being caught and fixed immediately.

## How to apply

Before starting the loop, edit the generated task list so each task's acceptance criteria explicitly runs lint, type-check, and the test suite, and only marks the task done if all three pass.

## Related

[[autonomous-ui-loop-acceptance-must-exercise-rendered-ui]]
