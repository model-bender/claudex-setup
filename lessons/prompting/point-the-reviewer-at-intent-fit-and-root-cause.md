---
id: point-the-reviewer-at-intent-fit-and-root-cause
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# Give the reviewer the PR's stated intent and ask three questions: solves its problem, fits the system, breaks something else

## TL;DR

A review prompt should read the diff against the whole repo and the PR's stated intent, and on a bug fix look for the root cause.

## Why it matters

This is how the article says its AI review reads every pull request. This lesson's reasoning: reviewing a diff without the intent can only find local defects, and the intent is what lets the reviewer say the change does not solve its problem.

## How to apply

Custom reviewer prompt: pass the PR description, then ask 'does the change solve its stated problem, fit the system, or break something else? For a bug fix, does it address the root cause?'

Checked: No mechanism named.

## Related

[[give-reviewers-only-the-spec-and-diff-and-verifiers-only-the-flow]]
