---
id: reverse-engineer-one-feature-at-a-time-not-the-whole-app
created: 2026-10-19
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-tested-the-viral-reverse-engineer-anything-skill-what-you-need-to-know_rL5tw6h78zo_20261013.txt
---

# Point a Teardown at One Feature of an App You Like, Not the Whole App

## TL;DR

Pick the specific behaviour you want (how Loom's camera bubble moves and resizes, say), have the agent investigate and rebuild that, and clone the functionality rather than the UI.

## Why it matters

Nate Herk found it hard to say 'go reverse engineer Loom', and easier to pick features after using the app. The result of the camera-bubble approach was a different-looking app that stores recordings locally, not a clone. He frames the app itself as the PRD, so no spec has to be typed out.

## How to apply

1. Use the reference app a little and list the features you actually want. 2. Give the agent one feature per teardown, with the tech stack in mind (the repo routes analysis tools by how the app is built). 3. Never copy exact code or assets. Checked: no tool mechanism named; the five steps (pick a feature, route by build, summary first, tag seen/inferred/unknown, rebuild and test) are the repo's as described by the speaker, not inspected.

## Related

[[forensic-site-clone-via-browser-dom-capture]], [[turn-an-admired-example-into-a-skill-by-having-claude-analyze-why-it-works]]
