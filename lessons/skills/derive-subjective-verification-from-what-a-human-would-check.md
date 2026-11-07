---
id: derive-subjective-verification-from-what-a-human-would-check
created: 2026-09-24
status: active
supersedes: null
category: skills
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/how-to-build-codex-skills-better-than-99-of-people_9KOtMsZ9I28_20260920.txt
---

# Derive a Skill's Subjective Verification Steps by Asking What a Human Would Check to Approve It

## TL;DR

When a task has no hard metric (does this sound right, does this look good), ask yourself what you personally would look at before giving the output a stamp of approval, then write that exact check into the skill's verification instructions.

## Why it matters

Subjective checks are harder to write than objective ones because there's no rule to state, but every human reviewer already has an implicit checklist they run before approving something. Making that checklist explicit turns a vague 'looks good to me' into an instruction the agent can actually follow, closing more of the gap before you ever see the output.

## How to apply

For any verification step you can't express as a pass/fail rule, ask: 'If I handed this task to a human, what would I look at to decide whether to approve it?' Translate each answer into an explicit instruction in the skill (e.g. 'check that no screenshot needs surrounding context to make sense', 'check that the tone matches these examples'), then have the agent run those checks against its own draft before returning it.

## Related

[[split-verification-into-rule-based-and-taste-based-skills]], [[evidence-clause-in-long-running-prompts]]
