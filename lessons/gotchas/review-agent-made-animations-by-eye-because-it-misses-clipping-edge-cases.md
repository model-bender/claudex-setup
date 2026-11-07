---
id: review-agent-made-animations-by-eye-because-it-misses-clipping-edge-cases
created: 2026-10-02
status: active
supersedes: null
category: gotchas
tool: codex
sources:
  - transcripts/john-kim/how-to-use-codex-to-create-beautiful-app-animations_f-Ar8mwm3kQ_20261002.txt
---

# Look at agent-made animations yourself, since it does not catch clipped edges

## TL;DR

Agents are poor at catching animation edge cases such as an element being cut off. Review frames manually.

## Why it matters

In the Rive demo John Kim points out an edge that cuts off in an animation Codex made. John Kim says AI is very bad at catching edge cases and tests of this nature, which is why you want to see the animation yourself, and says many people skip that check because they don't know what can go wrong.

## How to apply

Watch each generated animation yourself and look closely for elements that are cut off. As the lesson's own suggestion, pausing at the start and end of each clip and reporting the exact issue back to the agent makes the check concrete.

Verified: Observation from the source, no tool mechanism claimed.

## Related

[[score-video-takes-frame-by-frame-instead-of-eyeballing-smoothness]]
