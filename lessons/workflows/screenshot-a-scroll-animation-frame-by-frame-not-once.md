---
id: screenshot-a-scroll-animation-frame-by-frame-not-once
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/fable-5-1-finally-kills-ai-website-slop_FFWtxjvW2ts_20260910.txt
---

# Verify Scroll Animations by Screenshotting Frame by Frame Down the Page, a Single Screenshot Proves Nothing

## TL;DR

One screenshot of an animated page is one arbitrary moment of it. Have the agent step the scroll position and screenshot at each step, so it effectively watches a video of what the visitor experiences and can catch the hard cuts, out-of-bounds text and colour breaks that only exist mid-transition.

## Why it matters

Nate Herk's rule is blunt: if it is not taking screenshots and saying 'this looks bad, this is out of bounds, this colour is off, let me fix that', what are you doing? His own one-shot builds prove the need, a hard cut mid-scroll on the keyboard site and coffee text rendering out of bounds on another, both invisible in a top-of-page screenshot and both obvious in the sequence. Scroll-driven layout is the case where the existing screenshot-and-grade loop needs more than one frame.

## How to apply

Extend your visual verification step: 'Open the running page, step the scroll position in increments from top to bottom, screenshot at each step, then review the sequence for hard cuts, elements out of bounds, overlapping text and colour drift, and fix what you find.' Run it as a loop until the sequence is clean, and run the same sweep at mobile width. Cheaper than a full video capture and it is the same frame-index-to-scroll-offset idea used to drive scrubbed hero clips.

## Related

[[visual-self-validation-screenshot-grading]], [[one-hero-clip-scrubbed-by-scroll-for-an-immersive-site]], [[claude-design-builds-desktop-only-check-mobile-before-shipping]]
