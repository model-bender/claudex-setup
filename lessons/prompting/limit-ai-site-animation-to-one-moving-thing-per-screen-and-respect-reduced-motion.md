---
id: limit-ai-site-animation-to-one-moving-thing-per-screen-and-respect-reduced-motion
created: 2026-11-15
status: active
supersedes: null
category: prompting
tool: [claude-code, claude-design]
sources:
  - transcripts/nate-herk-ai-automation/i-studied-10-000-ai-websites-here-s-what-i-learned_mImbbszCjCI_20261112.txt
---

# Constrain scroll animation: one thing moves per screen, text readable at once, honour reduced motion

## TL;DR

Tell Claude every animation must do one job, only one element moves per screen, the first-screen headline and button are readable immediately, and animations turn off for users with the reduced-motion setting.

## Why it matters

The transcript says scroll animation is the fastest way to look premium and the fastest way to look AI generated. It cites Nielsen Norman Group on moving things pulling attention, and a Purdue parallax study where people found it more fun but no easier to use (the creator's citations).

## How to apply

Add to the design prompt: one thing moves per screen (the product, result or before and after); never delay headline, text or button with fade-ins on the first screen; respect the prefers-reduced-motion setting and optionally add a motion toggle like a dark mode switch. Apple's AirPods Pro page, where only the product moves, is the model cited.

## Related

[[screenshot-a-scroll-animation-frame-by-frame-not-once]]
