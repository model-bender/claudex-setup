---
id: numeric-type-and-spacing-contract-in-the-design-brief
created: 2026-08-16
status: active
supersedes: null
category: prompting
tool: claude-design
sources:
  - transcripts/tristen-o-brien/claude-design-ai-slop-fixed-in-9-minutes_S2DE95bGld0_20260810.txt
---

# Replace "Modern" With a Numeric Type and Spacing Contract in the Design Brief

## TL;DR

State measurable typography and spacing rules instead of adjectives: exactly one display font, body copy at 16-18px, every gap and margin a multiple of 8, and a layout that deliberately breaks the centred column.

## Why it matters

An unconstrained brief resolves to the training-data average, and two of that average's tells are the fastest to spot and cheapest to fix: Inter everywhere, and every element stacked straight down the middle of the page.

Neither fix requires design vocabulary from you - only numbers the model can check its own output against. The 8-multiple grid specifically is what makes a page read as *intentionally* aligned rather than approximately aligned. Claude Design already applies 8-point spacing on some runs, so this is a check-and-state rule rather than an always-missing one, and the creator's before/after showed the centred-column layout surviving right up until it was named.

## How to apply

Put the constraints in the generation prompt or the design-system notes: one display font only, body text 16-18px so it stays readable, all spacing a multiple of 8 (8, 16, 24), and do not run the layout straight down the centre of the page.

Attach font references pulled from the same sites you used for layout inspiration, labelled as inspiration rather than a copy target. When Claude Design offers font options, pick one and adjust it with a single named change ("make it a little heavier") instead of re-prompting the whole typography pass. If a render comes back centred or off-grid, say only that.

## Related

[[bracket-claude-design-with-claude-code-skills]], [[reference-real-products-and-state-negatives-instead-of-adjectives]], [[give-every-color-a-job-neutral-base-accent-on-click-targets]]
