---
id: bring-your-own-hero-video-to-claude-design-with-matched-first-and-last-frames
created: 2026-07-17
status: active
supersedes: null
category: workflows
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-design-builds-beautiful-3d-websites-instantly-full-tutorial_TcFeSjwTo7g_20260624.txt
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
---

# Bring Your Own Hero Video to Claude Design, Controlling the Loop with First and Last Frames

## TL;DR

Claude Design can't generate video, so render it elsewhere and drag the MP4 in as context. Feed the **same still as both first and last frame** for a seamless static-camera loop, and match the video's background to the page's hex so it composites invisibly.

## Why it matters

An endless-loop hero video is what separates these builds from a generic landing page, and the loop only reads as seamless if the camera doesn't move, feeding the identical still as both first and last frame is what pins it ("the key thing here is that the camera isn't moving").

Start/end-frame control also buys reveals: blank background → logo produced a hand-drawn logo animation.

And if the video's background doesn't match the page background exactly, you see the seam.

## How to apply

Ask a regular Claude chat for an image prompt plus a video prompt for the vibe, specifying **no text** and negative space where the hero copy goes.

Render the still at 16:9, then feed it as both first and last frame to a video model with the animation prompt.

Drag the MP4 into the Design project and state the composite explicitly:

> the animation's background is the bone color, so make the whole hero background bone so it fits in seamlessly

Grab exact hex codes if the first pass is close but off.

Uploads cap around 30-40MB: 8-15 second clips are fine, 20 seconds worked, a 5-minute video won't.

## Related

[[claude-design-animation-template-for-branded-motion-graphics]], [[paste-a-word-level-transcript-claude-design-cannot-hear-video]], [[feed-claude-design-a-reference-gallery-url-or-its-prompt]]
