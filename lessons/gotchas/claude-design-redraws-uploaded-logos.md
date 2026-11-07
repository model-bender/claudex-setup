---
id: claude-design-redraws-uploaded-logos
created: 2026-07-17
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
---

# Expect Claude Design to Redraw Your Uploaded Logo: Reject It in the Design-System Review

## TL;DR

Claude Design re-renders logos rather than placing the PNG you uploaded, mangling detailed icon marks while simple letterform wordmarks survive. Catch it tile-by-tile in the design-system review and tell it the PNG is not to be changed.

## Why it matters

Called "one of the major flaws I've noticed with Claude Design so far" and "historically bad with logos", and hit three separate times in one build: in the design system, in the pitch deck, and at the end of a launch video.

It's silent. Colors and type look right, so the tile passes review unless you inspect the mark itself.

Every correction round costs tokens, so catching it once in the design system beats catching it in every downstream artifact. A letter-based logo never broke; a detailed tally cross broke repeatedly.

## How to apply

During design-system generation, review each tile and reject any where the mark shifted:

> No, that needs work. The logo is not appearing as it should. I dropped in a PNG of a logo and you should keep it exactly as is, there's no reason to change that. The colors and font are fine, but the icon logo is not correct.

Prefer a letterform logo where you have the choice.

For a stubborn last-mile fix on a poster or one-pager, drop the export into a design tool and place the real logo yourself rather than burning rounds arguing.

## Related

[[seed-design-system-with-a-real-brand-kit]], [[claude-design-cannot-place-freeform-or-invent-graphics]]
