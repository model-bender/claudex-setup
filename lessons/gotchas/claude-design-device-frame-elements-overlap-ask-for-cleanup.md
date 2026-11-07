---
id: claude-design-device-frame-elements-overlap-ask-for-cleanup
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Claude Design's Mobile Device Frame Can Overlap Its Own Status Bar With Content: Ask It to Clean Up Formatting

## TL;DR

Wireframes generated for a named device frame (e.g. iPhone) can render the phone's simulated time/battery bar crossing over real page content; explicitly ask Claude Design to clean up the formatting for that frame rather than assuming the device chrome is accurate.

## Why it matters

Picking a device frame in the wireframe intake doesn't guarantee correct safe-area handling, the generated screens looked convincing at a glance but had the simulated status bar overlapping headers and notes scattered out of place.

## How to apply

After generating device-framed wireframes, check the top and edges of each screen for overlap with simulated OS chrome (status bar, notch). If you see it, comment or prompt specifically: 'clean up the formatting, the header crosses over the phone status bar.'

## Related

[[keep-the-claude-design-brief-open-enough-to-trigger-its-question-round]]
