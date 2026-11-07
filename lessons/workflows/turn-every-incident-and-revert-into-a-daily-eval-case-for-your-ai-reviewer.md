---
id: turn-every-incident-and-revert-into-a-daily-eval-case-for-your-ai-reviewer
created: 2026-10-19
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: canonical
sources:
  - https://claude.dev/blog/solving-code-review-at-anthropic/
---

# Turn Every Incident and Revert Into a Case in a Daily Eval for Your AI Reviewer

## TL;DR

Collect past incident PRs with their fix-forwards and reverts, have someone who knows the code confirm each bug, and score every change to the reviewer's prompt, tools or model against that set.

## Why it matters

Tuning a reviewer by feel trades recall for noise. A regression set of real escapes, plus known-clean PRs to count harmful findings, gives a measurable stop condition for each reviewer change.

## How to apply

Build the set from incident and revert PRs, confirm each bug's location with the code owner, re-run your review prompt or skill on it after every edit, and keep a change only if the score goes up. Checked: no mechanism named.

> "Any incidents are now an eval. The team collected past PRs that caused incidents, with their fix-forwards and reverts, and had engineers who know that code confirm each bug and where it lived. The reviewer runs against that set daily.", Claude Code team blog (Addy Osmani, Morgan Westlee Lunt, Qing Wang)

## Related

[[design-agent-output-for-verifiability-before-building-evals]]
