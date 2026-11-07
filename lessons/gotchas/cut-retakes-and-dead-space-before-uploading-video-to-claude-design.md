---
id: cut-retakes-and-dead-space-before-uploading-video-to-claude-design
created: 2026-08-31
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-just-destroyed-every-video-editing-tool_ZNbgOhxhzXg_20260624.txt
---

# Cut Retakes and Dead Space Yourself Before Uploading Footage to Claude Design

## TL;DR

Claude Design cannot tell a flubbed take from a real one, so edit retakes and dead space out of raw footage by hand before uploading; steering the model cut-by-cut through prompts costs more than doing the rough cut yourself.

## Why it matters

The model has no signal for which take you meant to keep, so it treats everything in the upload as intended content and overlays animation work onto footage you never planned to ship. Correcting those editing decisions through prompt rounds is slower and more expensive than a quick manual pass in any editor.

## How to apply

Before uploading an MP4 to Claude Design's animation surface, do a rough cut that removes flubbed takes and dead space, then upload the cleaned footage. Reserve prompting for the animation and overlay work itself, not for editing decisions the model cannot make reliably.

## Related

[[paste-a-word-level-transcript-claude-design-cannot-hear-video]]
