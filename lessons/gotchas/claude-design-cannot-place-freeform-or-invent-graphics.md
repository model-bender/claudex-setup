---
id: claude-design-cannot-place-freeform-or-invent-graphics
created: 2026-07-17
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Claude Design Can't Place Freely or Invent a Graphic: Make the Asset Elsewhere

## TL;DR

Claude Design is deterministic layout, not a canvas: you can't drag anything, and it can't conjure a custom graphic. When you want a specific visual element, generate the image in an image model, upload it, and reference it.

## Why it matters

Anthropic's own design team frames it as "closer to Claude Code than a pixel editor", and that has a cost.

Wanting a playful arrow pointing down at a video: the draw tool failed, then a comment failed, then draw plus comment failed, three rounds, because the model has to resolve every position into concrete margin and padding and couldn't compute how to render the arrow as a background element.

Worse, the comment tool won't accept an image attachment, so the obvious fix isn't available where you'd reach for it.

This is the boundary of the 90/10 rule: the last 10% (custom microcopy, exact icons, logos, real taste) still needs you.

## How to apply

When a change is spatial or needs a bespoke graphic, stop prompting after the first failure.

Screenshot the current design into an image model and ask it to draw the element in the same UI style ("a graphical arrow pointing down at the video below it, drawn in the style of the UI you see").

Download it, upload it through the main chat rather than a comment, and reference the attachment: "change X to look like the screenshot attached."

The wasted rounds are the expensive part, not the tokens, the whole arrow detour still only cost ~2% of a weekly limit.

## Related

[[pin-claude-design-edits-to-one-element-with-an-exact-value]], [[claude-design-draw-to-code]], [[claude-design-comment-box-rejects-image-attachments]]
