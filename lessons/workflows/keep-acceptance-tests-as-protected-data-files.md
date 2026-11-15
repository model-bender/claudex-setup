---
id: keep-acceptance-tests-as-protected-data-files
created: 2026-11-15
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
source_type: post
sources:
  - https://martinfowler.com/articles/tests-as-data.html
---

# Keep the contract part of agent-era tests in read-only data files and check that changed files match the task type

## TL;DR

Put the important part of acceptance tests (inputs, expected outputs, setup) in text data files read by a small test runner. Then lock those files, or have CI fail when a task type that should not touch them changes them.

## Why it matters

Agents refactor and weaken tests as code evolves, and reviewers stop reading boring test diffs, so confidence in the suite erodes. Data files are easy to protect and easy to diff. The article's table says refactoring should change production code only, and improving coverage should change test data only.

## How to apply

Move customer-level cases into tables or files (for example YAML or CSV). Add a PreToolUse hook or a CI changed-files check that blocks edits to them unless the task is "new functionality" or "improve coverage".

> "it's possible to protect the files that we're not expecting the AI to change, by making them read-only in a way that the agent cannot bypass, or by running a check in CI that verifies what files were changed depending on the type of task.", Matteo Vaccari (Thoughtworks), martinfowler.com

