---
id: keep-the-claude-design-brief-open-enough-to-trigger-its-question-round
created: 2026-07-17
status: active
supersedes: null
category: prompting
tool: claude-design
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
  - transcripts/sean-kochel/4-step-claude-design-system-for-pro-uis_mJ98eeC0oDg_20260703.txt
  - transcripts/nate-herk-ai-automation/claude-just-destroyed-every-video-editing-tool_ZNbgOhxhzXg_20260624.txt
---

# Leave the Brief Open Enough to Trigger Claude Design's Question Round

## TL;DR

Claude Design's clarifying questions are its planning stage, and they only fire when the brief has room. Over-prescribe and you skip the interview entirely, Claude just assumes the answers instead.

## Why it matters

Both halves of this are observable. A heavily-specified landing-page brief silently skipped the questions ("we didn't really get the interactivity of Claude asking us different questions because we were so prescriptive"), while a deliberately looser wireframe brief triggered a long interview credited as "the purpose of this design planning", questions detailed enough that they surfaced decisions the author hadn't made.

This is the affordance Claude Design has that the Claude Code terminal doesn't, and it's the difference between a design that lands first time and one you rework. The same point from the other end: "build me a dashboard" returns the average of the training data because you gave no motivational context.

## How to apply

Aim for prescriptive enough that it won't go off the rails, open enough that it asks. Pin down the design system, attach reference screenshots, and state the goal and constraints, then leave the interaction decisions unmade.

Expect questions like: which screens to render, how many variations per screen, what the variations should explore, what the tweaks panel should toggle, device frame, annotations/callouts, layout of the deliverable, and sample content.

Answer the ones you have taste about. "Decide for me" is a legitimate answer for the axes you don't.

## Related

[[claude-design-question-round-times-out-into-defaults]], [[declare-variation-axes-and-tweak-toggles-up-front]], [[design-philosophy-first-strip-prd-then-pick-one-ux-direction]]
