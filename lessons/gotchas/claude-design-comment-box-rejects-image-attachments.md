---
id: claude-design-comment-box-rejects-image-attachments
created: 2026-09-12
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Claude Design's Comment Box Takes No Image Attachment: Upload in the Main Chat and Reference It

## TL;DR

You cannot attach an image to a pinned comment in Claude Design, which is exactly where you reach for one. Upload the image through the main chat instead and refer to it from the prompt.

## Why it matters

Pinning feedback to a specific element is the recommended way to drive Claude Design, and showing it a picture is the fastest way to specify a bespoke graphic, so the two meet in the obvious workflow that the surface does not support. Discovering it mid-iteration costs rounds, and rounds are the expensive part of Claude Design rather than tokens.

## How to apply

Generate or screenshot the asset elsewhere, upload it through the main chat, and say 'change X to look like the screenshot attached'. Keep pinned comments for text instructions carrying an exact value.

## Related

[[claude-design-cannot-place-freeform-or-invent-graphics]]
