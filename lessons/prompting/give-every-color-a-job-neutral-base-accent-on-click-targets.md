---
id: give-every-color-a-job-neutral-base-accent-on-click-targets
created: 2026-08-16
status: active
supersedes: null
category: prompting
tool: claude-design
sources:
  - transcripts/tristen-o-brien/claude-design-ai-slop-fixed-in-9-minutes_S2DE95bGld0_20260810.txt
---

# Give Every Color a Job: Neutral Majority, Accent Only Where You Want a Click

## TL;DR

Tell the generator most of the page stays neutral - one base surface color plus a high-contrast text color - and that bold color appears only where you want attention or a click: buttons, links, one word you want to pop. Ban gradients outright.

## Why it matters

Color is the loudest AI tell after typography, and the failure is **allocation**, not palette: the model spreads brand color across the whole page and reaches for the purple gradient.

A rule that ties color to a job ("it only goes where you want people to look or click") is one the model can apply to any palette you hand it, so it survives a palette swap and works for a brand you have not defined yet. It also encodes the true ratio, because the neutral base plus text is the majority of what a visitor actually sees. The creator applies it as a rule that "works with almost any brand", not as a taste call.

## How to apply

Attach two or three palettes for inspiration and state the intent in plain language ("bright and fun, this is an energy drink") so the model knows what it is coloring. Then add the allocation rule: keep most of the page neutral with a base color and a clean text color; add bold color sparingly; every color has to earn its place, and it only goes where you want people to look or click (buttons, links, a single word); no gradient anywhere.

Review the result on *where the color landed* rather than on whether you like the hue - the hue is the part you can change in one follow-up.

## Related

[[numeric-type-and-spacing-contract-in-the-design-brief]], [[bracket-claude-design-with-claude-code-skills]], [[reference-real-products-and-state-negatives-instead-of-adjectives]]
