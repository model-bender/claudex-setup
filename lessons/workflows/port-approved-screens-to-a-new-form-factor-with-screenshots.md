---
id: port-approved-screens-to-a-new-form-factor-with-screenshots
created: 2026-07-17
status: active
supersedes: null
category: workflows
tool: claude-design
sources:
  - transcripts/sean-kochel/open-design-is-every-vibe-coders-dream_MmTBkDmunk4_20260703.txt
---

# Port Approved Screens to a New Form Factor by Screenshotting Them into a Fresh Chat

## TL;DR

Once a set of mobile screens is right, screenshot them, drop the images into a new design chat, and ask for a web-app version of the same core functionality. The approved design carries the spec better than a rewritten prompt.

## Why it matters

A complete desktop translation came back in about 5 minutes from a deliberately vague ask: a three-pane layout with navigation left, canvas center, and progress right, with the slash-command affordances preserved.

The screenshots already encode the design system, interaction model, and content that a prose prompt would have to re-derive, and **re-deriving it is exactly where the second form factor drifts away from the first**.

## How to apply

Screenshot the screens you've approved, open a **new chat** rather than the thread that built them, attach the images, and ask openly:

> Mock up a web app version of this core functionality.

Answer the intake questions and let it propose the layout translation.

Feed real specs for the target form factor too if you have them, but the screenshots alone carry a surprising amount.

## Related

[[export-and-restart-instead-of-iterating-in-one-long-claude-design-thread]], [[claude-design-builds-desktop-only-check-mobile-before-shipping]], [[open-design-local-first-agent-agnostic-claude-design-alternative]]
