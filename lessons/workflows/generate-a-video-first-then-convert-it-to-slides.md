---
id: generate-a-video-first-then-convert-it-to-slides
created: 2026-07-17
status: active
supersedes: null
category: workflows
tool: claude-design
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Ask Claude Design for a Video First, Then Convert It Into the Slide Deck

## TL;DR

Prompting Claude Design for a slide deck directly yields static, generic slides. Ask for an animated video on the same content, then duplicate the project and convert it to clickable slides, the motion-first composition survives the conversion.

## Why it matters

Slides prompt the model toward a boring static default, whereas a video brief forces it to plan scenes, an intro/outro structure and staged animations, because motion is the whole point of the medium. Converting afterwards keeps that structure and pacing.

The resulting deck came out with per-slide narrative beats, embedded tweets placed on the right slides, and animated build-ups, from content that started life as a LinkedIn carousel.

The honest cost: the conversion "lost a little bit of the dynamic nature", so ask for animations back if you want them.

## How to apply

Create the project against your design system and prompt for the video, pasting the real source content rather than a summary:

> Make an animated video explaining the seven levels I explain in this video transcript, follow the <X> design system.

Review the scenes. Then Share → duplicate project (which also saves projects as templates) and prompt:

> Turn this into a slide deck instead of a video that I can click through.

Attach screenshots to replace slides that are overloaded with text, and tell it which slides they belong to, it will place them correctly.

Budget roughly 8% of a Max 20x weekly limit for the video step.

## Related

[[claude-design-animation-template-for-branded-motion-graphics]], [[precompute-the-design-system-outside-claude-design]]
