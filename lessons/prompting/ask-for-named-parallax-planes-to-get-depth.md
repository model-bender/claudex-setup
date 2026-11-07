---
id: ask-for-named-parallax-planes-to-get-depth
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/fable-5-1-finally-kills-ai-website-slop_FFWtxjvW2ts_20260910.txt
---

# Ask for Named Parallax Planes Moving at Different Scroll Rates, Not for 'Depth'

## TL;DR

Spell out the layers you want and what is on each one (far background, mid background, subject, foreground), and say they move at different rates as the page scrolls. Layering is the single technique that reads as premium, and it only happens if you enumerate the planes.

## Why it matters

Nate Herk identifies layering as the specific thing he learned makes sites feel premium rather than generic, and he gets it by describing the exact stack he saw on a reference site: a back mountain, a middle mountain, a laptop screen, and a front layer of trees, each moving at its own rate. Asking for depth or a premium feel returns the training-data average instead. The same enumerated stack survived into later builds, plants on separate planes, backgrounds tracking left at a different rate to the subject.

## How to apply

In the build prompt, list the planes top to bottom, say what asset sits on each, and state that they translate at different rates on scroll: 'four layers, far mountains slowest, mid mountains faster, the product still in front of them, foreground trees fastest.' Verify by stepping the scroll and screenshotting, the rate differences are exactly what a single screenshot cannot show. Pair with a named real reference rather than adjectives.

## Related

[[reference-real-products-and-state-negatives-instead-of-adjectives]], [[screenshot-a-scroll-animation-frame-by-frame-not-once]], [[name-gsap-for-claude-code-scroll-animations]]
