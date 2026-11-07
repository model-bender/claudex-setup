---
id: plan-review-hook-only-blocks-on-explicit-block-verdict
created: 2026-09-01
status: active
supersedes: null
category: hooks
tool: claude-code
about: codex
sources:
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
---

# In an External Plan-Review Hook, Only Redo the Plan on an Explicit 'Block' Verdict

## TL;DR

When an ExitPlanMode hook sends the plan to Codex CLI and Gemini CLI for review, structure the flow so a 'warning' verdict from either reviewer lets Claude proceed with execution, and only an explicit 'block' verdict makes it redo the plan.

## Why it matters

The transcript shows this exact behavior happening live: 'we did not block the plan from happening because... the verdict that Gemini CLI gave is basically warning about issues... If Codex and Gemini said like, hey, we're gonna block the plan, then it would redo the plan.' Without deliberately encoding this warn-vs-block distinction, a reviewer hook either blocks on every nitpick (too strict) or ignores real blockers (too loose).

## How to apply

When building the review CLI's response contract, have it emit a verdict field with at least two levels (warn / block); in the hook or main-agent instructions, only halt and re-plan on 'block', and on 'warn' let Claude read the feedback, note it, and continue executing the current plan.

