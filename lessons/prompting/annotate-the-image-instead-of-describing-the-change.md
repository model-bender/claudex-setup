---
id: annotate-the-image-instead-of-describing-the-change
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Annotate the Image in the Desktop App Instead of Describing Where to Move Things

## TL;DR

For a change that is easier to point at than to say ('move this up here'), draw on the screenshot in the desktop app and prompt against the mark: 'remove the red circle'.

## Why it matters

Spatial instructions in prose are where visual work stalls, because 'the button under the hero on the right' has several readings and the agent picks one. A circle has one.

## How to apply

Attach or paste the screenshot in the desktop app, use the annotation tool to mark the element, then write the instruction referring to the annotation rather than to a position.

## Related

[[pin-claude-design-edits-to-one-element-with-an-exact-value]]
