---
id: prompt-interaction-states-they-are-omitted-by-default
created: 2026-07-17
status: active
supersedes: null
category: prompting
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/jono-catliff/claude-code-web-design-10-years-covered-in-66-minutes_2Gda_ZvV1V4_20260701.txt
---

# Prompt for Interaction States Explicitly: Generated UI Ships Flat

## TL;DR

Hover, focus, and transition states are the cheapest polish win and the one thing generated sites reliably omit: buttons swap colour instantly, inputs have no focus ring, cards don't lift. Ask for them with named specs.

## Why it matters

This is a category the model skips entirely rather than gets wrong, so it never surfaces as an error, the site looks fine in a screenshot and feels dead in a browser.

It's a large share of what reads as "AI slop" in an otherwise well-designed page, and it survives the Claude Design handoff because a static design artifact has no hover state to export.

## How to apply

After the handoff build, run a dedicated pass naming the states and their specs:

> On hover, invert the button colours, scale ~10%, add a shadow, transition over 300ms; on input focus add a ring with a ring offset; lift cards with a shadow on hover; underline nav links left-to-right over 300ms.

The 300ms transition is what separates a professional feel from an instant colour swap. The same pass is the right place for the sticky translucent/frosted navbar and the mobile hamburger drawer.

Precision matters: a ring is not a border, and ring offset is the gap between them.

## Related

[[learn-technical-vocabulary-for-precise-prompts]], [[scaffold-the-target-framework-before-pasting-the-design-handoff]]
