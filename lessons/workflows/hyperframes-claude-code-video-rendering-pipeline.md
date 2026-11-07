---
id: hyperframes-claude-code-video-rendering-pipeline
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-just-destroyed-every-video-editing-tool_ZNbgOhxhzXg_20260624.txt
---

# Drive HyperFrames From Claude Code to Render HTML-Based Motion Graphics Videos

## TL;DR

HyperFrames is an open-source, agent-drivable video framework: Claude Code writes HTML/CSS motion graphics, HyperFrames renders it through a headless browser into frames, then FFmpeg assembles the frames into an MP4.

## Why it matters

It gives more control than Claude Design's animation template (which can't export MP4 at all) and lets you build a reusable 'video editing studio' of skills and design docs inside one Claude Code project that improves with every video you make.

## How to apply

Give Claude Code the HyperFrames GitHub repo URL and ask it to analyze the repo, build skills and knowledge around how it works, and help install it. Then iterate: drop a raw video into the project root, invoke a 'make a video' skill, and let it interview you about layout, captions, and transcript needs before rendering.

## Related

[[claude-design-has-no-mp4-export-render-via-claude-code]]
