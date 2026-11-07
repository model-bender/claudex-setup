---
id: wrong-output-diagnosis-knew-too-little-raise-model-skipped-work-raise-effort
created: 2026-10-25
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/austin-marchese/use-claude-models-effort-level-better-than-97-of-people_BZluE67z1MA_20261024.txt
---

# When Claude Gets Something Wrong, Ask Which Failure It Was Before Touching Model or Effort

## TL;DR

If Claude had everything it needed and still got it wrong, raise the model; if it skipped a file, skipped a test or bailed halfway, raise the effort.

## Why it matters

Austin Marchese presents a two-question test, which he attributes to Anthropic's guidance, to stop blind switching: a wrong answer despite full context is a capability problem, while skipped steps are an effort problem. It tells you which of the two dials to turn instead of changing both.

## How to apply

After a bad result, ask the two questions. Case 1: it had everything it needed and still got it wrong: use a better model. Case 2: it ignored a file, left out a test or stopped early: raise effort (`claude --effort high`). The commands and the next step below are this lesson's additions, not the video's: switch models with /model, and if neither case fits, suspect the spec (see the related lesson on sharpening it). Checked: claude --help on 2.1.310 confirms --effort exists. The attribution to Anthropic guidance is the creator's and was not checked against the docs.

## Related

[[escalate-model-then-effort-then-claude-md-when-output-misses-the-bar]], [[sharpen-the-spec-before-reaching-for-more-effort]]
