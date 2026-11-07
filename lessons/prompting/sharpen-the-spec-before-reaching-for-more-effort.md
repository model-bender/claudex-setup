---
id: sharpen-the-spec-before-reaching-for-more-effort
created: 2026-07-17
status: active
supersedes: null
category: prompting
sources:
  - transcripts/mark-kashef/this-is-the-ai-setting-everyone-gets-wrong_4__5q76f04s_20260714.txt
  - transcripts/nate-herk-ai-automation/claude-code-for-non-coders-6-hour-course_jdbOVepEtUE_20260712.txt
---

# Sharpen the Spec Before Reaching for a Higher Effort Level

## TL;DR

Reasoning effort is a reflection/token budget, not an intelligence dial, when output is weak, tighten the prompt/spec (state exactly what you want) before cranking effort, because a good spec closes the gap far more cheaply than more thinking does.

## Why it matters

The same task run across a dozen effort levels produced near-identical results (extra-high only added a favicon); the model wasn't getting "smarter" with more budget, it was just reflecting more. When people mistake effort for intelligence, they park on max and burn 2-5x tokens for cosmetic gains, while the actual shortfall was an underspecified prompt the extra reasoning can't read your mind to fix. A concrete spec (e.g. naming the styling you want) lifts even low-effort output to near-max quality.

## How to apply

When the result disappoints, first rewrite the spec to remove the ambiguity that caused it, then re-run, don't reflexively bump effort. Start low (the default is enough for most work on a capable model) and raise effort only when a concrete shortfall gives you evidence the task genuinely needs more reflection. For how high to go once you do climb, and why max rarely beats high, see [[max-effort-is-a-trap-quality-plateaus-at-high]].

## Related

[[max-effort-is-a-trap-quality-plateaus-at-high]], [[force-explore-and-read-before-implementing]], [[escalate-model-then-effort-then-claude-md-when-output-misses-the-bar]]
