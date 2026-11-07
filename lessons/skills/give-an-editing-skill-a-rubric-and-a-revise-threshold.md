---
id: give-an-editing-skill-a-rubric-and-a-revise-threshold
created: 2026-09-12
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Give an Editing Skill a Scoring Rubric and a Revise Threshold Instead of Dozens of Examples

## TL;DR

The Stop Slop skill is core rules plus a few quick checks, then a 1-to-10 score across five named dimensions (rhythm, trust, authenticity, density and one more) for a total out of 50, with anything under 35 sent back for revision against the dimension that scored worst.

## Why it matters

Older-model skills pinned down style with a hundred worked examples, which is exactly the bulk newer models no longer need. A short rule set plus a numeric rubric gives the skill something the example dump never did: a stopping condition, so it revises until it clears the bar rather than making one vague pass.

## How to apply

Structure the skill as core rules, quick checks, a scored rubric over named dimensions, and an explicit revise-below-N threshold. Name the dimensions in the words you would use when rejecting a draft, and let the skill iterate against its own score.

## Related

[[skill-goal-oriented-not-railroaded]], [[delete-examples-and-negative-constraints-from-claude-md]], [[brand-voice-profile-reduces-ai-detection]]
