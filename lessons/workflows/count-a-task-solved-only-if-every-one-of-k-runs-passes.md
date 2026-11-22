---
id: count-a-task-solved-only-if-every-one-of-k-runs-passes
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
source_type: post
sources:
  - https://eugeneyan.com/writing/public-evals
---

# Rerun a Skill or Prompt Several Times and Count a Task Solved Only If Every Run Passes

## TL;DR

When you check a skill, command or prompt on a set of tasks, run each task k times and report all-k passes, because an average pass rate hides unreliable behaviour.

## Why it matters

Two setups can both score 70% while one needs every output checked by you. All-k scoring (pass^k) separates the reliable one, and reliability is what decides whether you can stop supervising.

## How to apply

Run each test task five times against your skill or CLAUDE.md change, count it solved only if all five pass, and compare that number, not the mean, before and after an edit.

> "Consider two agents that both score 70%. The first solves 70% of tasks every time, while the second solves every task 70% of the time.", Eugene Yan

