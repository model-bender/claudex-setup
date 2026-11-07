---
id: reference-real-products-and-state-negatives-instead-of-adjectives
created: 2026-07-17
status: active
supersedes: null
category: prompting
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-design-builds-beautiful-3d-websites-instantly-full-tutorial_TcFeSjwTo7g_20260624.txt
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
---

# Name a Real Product and Era Instead of Reaching for Adjectives Like "Clean"

## TL;DR

"Make it clean" or "minimalistic" returns the training-data average. "Linear 2023 with higher density" names a target the model actually knows. Pair it with negatives, the fonts and color schemes you don't want, so you aren't correcting them later.

## Why it matters

"Reference, don't describe" is the first of the four moves that compound.

Aesthetic adjectives are nearly information-free, everyone's "clean" is different, so the model resolves the ambiguity toward its high-probability center, which is exactly the generic AI look you're trying to escape.

A named product plus a year is a dense, unambiguous pointer. A stated negative prunes a branch before it costs you a correction round.

## How to apply

Replace each aesthetic adjective with a real reference and an era, and add an explicit not-list of the fonts and color schemes you don't want.

Use the other reference channels in the same spirit rather than prose: real screenshots, gallery prompts, your design system, and pointing/commenting directly at elements.

## Related

[[feed-claude-design-a-reference-gallery-url-or-its-prompt]], [[split-brand-and-structure-sources-in-one-design-prompt]], [[bracket-claude-design-with-claude-code-skills]], [[learn-technical-vocabulary-for-precise-prompts]]
