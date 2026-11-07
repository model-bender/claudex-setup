---
id: right-size-screenshots-so-claude-can-locate-the-code
created: 2026-09-01
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Size UI Screenshots So Surrounding Text Is Visible, Not Just the Broken Element

## TL;DR

A screenshot that's too tightly cropped gives Claude Code nothing to text-match against; one that's too large gives no clear focal point. Pair a full-context screenshot with a smaller cropped zoom of the exact element when referencing competitor UIs.

## Why it matters

Claude Code locates the relevant part of the codebase by matching visible text/labels in the screenshot. A too-small crop lacks that surrounding text; an oversized screenshot has no clear target.

## How to apply

When reporting a UI bug or referencing a competitor design, take a screenshot sized so nearby labels/text are visible (not a tight, tiny crop). For competitor references, also include a smaller zoomed-in crop of the exact element alongside the full screenshot.

## Related

[[screenshot-paste-instead-of-describing-ui-problems]]
