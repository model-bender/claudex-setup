---
id: effort-level-does-not-predict-token-spend
created: 2026-09-12
status: active
supersedes: null
category: gotchas
tool: codex
sources:
  - transcripts/mark-kashef/i-tested-every-gpt-6-astra-effort-level-here-s-what-i-d-use_OQipTxv9Qv0_20260910.txt
---

# Don't Assume a Lower Effort Level Spends Fewer Tokens

## TL;DR

On the same prompt, Astra low burned about 15M tokens, medium about 10M and high about 14M. Effort is not a reliable proxy for cost, so measure the run instead of inferring it.

## Why it matters

The mental model that effort scales spend monotonically is what makes people avoid a level they should be using, or assume a cheap setting is protecting them. Kashef's controlled threads broke the ordering outright: low cost more than medium, and max spent fewer tokens than high while taking longer in wall-clock time. He expects the timings to repeat on a rerun but calls token spend increasingly unpredictable, which means the dial controls behaviour, not a budget.

## How to apply

When cost matters, read the actual token and time counts for the run rather than reasoning from the effort label, and compare levels on your own representative task before standardising. Do not justify a level choice on assumed savings.

## Related

[[default-astra-to-medium-effort-in-codex]], [[max-effort-is-a-trap-quality-plateaus-at-high]], [[spin-up-parallel-threads-at-different-effort-levels-from-one-prompt]]
