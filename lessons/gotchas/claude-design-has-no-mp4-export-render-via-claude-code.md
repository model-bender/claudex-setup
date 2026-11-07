---
id: claude-design-has-no-mp4-export-render-via-claude-code
created: 2026-07-17
status: active
supersedes: null
category: gotchas
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-just-destroyed-every-video-editing-tool_ZNbgOhxhzXg_20260624.txt
---

# Claude Design Won't Export MP4: Hand the Animation to Claude Code to Render

## TL;DR

Animation projects have no MP4 export. Screen-record for a quick clip, or use the hand-off-to-Claude-Code command and have Claude Code render the file.

## Why it matters

You can build a finished, branded animation in Claude Design and then discover there's no way to get a video file out of it, the deliverable is a live preview. That's fine until you need to post it.

The project is just HTML underneath, so Claude Code can drive FFmpeg over it and produce the MP4 that Design won't.

## How to apply

For a short clip, full-screen the preview and screen-record it.

For anything longer, use Share → hand off to Claude Code, copy the generated command, paste it into Claude Code and say "render this as an MP4", you get a downloadable file.

This complements the existing zip-export handoff: same bridge, different reason (a missing export format rather than code-level iteration or quota).

Budget for it: render work runs ~10% of a 5-hour Max limit per project, because generating that much HTML is output-token heavy, and rendering several videos at once will visibly starve your CPU/RAM.

## Related

[[claude-design-animation-template-for-branded-motion-graphics]], [[hand-off-claude-design-exports-to-claude-code]], [[hand-off-to-claude-code-from-the-project-root-not-a-page]]
