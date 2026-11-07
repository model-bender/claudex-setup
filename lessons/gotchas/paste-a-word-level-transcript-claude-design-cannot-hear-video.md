---
id: paste-a-word-level-transcript-claude-design-cannot-hear-video
created: 2026-07-17
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-just-destroyed-every-video-editing-tool_ZNbgOhxhzXg_20260624.txt
---

# Claude Design Cannot Hear Your Video: Paste a Word-Level Timestamped Transcript

## TL;DR

Claude Design can't watch or listen to an uploaded MP4. Without a transcript carrying word-level timestamps, nothing it overlays can sync to what you're actually saying.

## Why it matters

This is the core limitation of the animation surface: "it can't actually read or listen to or understand what's being said in the video, which when you're animating a video, that's super important."

Two things break without it, the graphics can't land on the right beat, and the tool doesn't know what concepts to illustrate in the first place.

Claude Design half-admits it by asking you to paste the script with rough timestamps, but rough is the wrong resolution: word-level is what lets captions and motion graphics hit the syllable.

## How to apply

Transcribe before you upload and paste the JSON when it asks. Running the transcription in a Claude Code project and pasting the resulting word-level JSON into the Design chat works well.

For the transcription itself, whisper.cpp locally works but is RAM-hungry, running eight videos at once wedged a machine, with OpenAI's Whisper API via an API key as the fallback.

Separately, cut retakes and dead space out of the raw footage yourself first: the model can't tell a flubbed take from a real one, and steering it cut-by-cut costs more than doing it by hand.

## Related

[[claude-design-animation-template-for-branded-motion-graphics]], [[claude-design-has-no-mp4-export-render-via-claude-code]], [[cut-retakes-and-dead-space-before-uploading-video-to-claude-design]]
