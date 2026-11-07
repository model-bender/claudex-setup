---
id: claude-design-asset-upload-size-cap
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
  - transcripts/nate-herk-ai-automation/claude-design-builds-beautiful-3d-websites-instantly-full-tutorial_TcFeSjwTo7g_20260624.txt
---

# Claude Design Caps Media Uploads Around 30-40MB

## TL;DR

Claude Design rejects or silently fails on long/large video uploads. The creator got 15-second clips through reliably and a 20-second clip once, but flagged a roughly 30-40MB ceiling.

Claude Design won't accept long video uploads; the practical cap is roughly 30-40MB and it starts rejecting clips as duration climbs past about 15-20 seconds.

## Why it matters

Background hero videos are a common Claude Design technique, and the creator hit this directly: "there is a cap and I think it might be around 30 or 40 megabytes... if you try to upload like a 5-minute video, it's probably not going to let you." Not knowing the rough ceiling, a failed upload reads as a random bug rather than a size/duration problem.

The creator hit upload limits directly: an 8-second clip worked easily, a 15-second video worked, a 20-second video also worked but is near the edge, and he states the cap is around 30 or 40 megabytes and that a full multi-minute video will not upload at all.

## How to apply

Before uploading an MP4 as a hero or background video, trim it well under ~20 seconds and check the export is well under 30-40MB. If an upload silently fails, re-export shorter/smaller before assuming a platform bug.

Trim hero/background video generations to well under ~20 seconds and keep the file size under roughly 30-40MB before uploading to Claude Design, rather than discovering the rejection after generating a longer clip.

## Related

[[cut-retakes-and-dead-space-before-uploading-video-to-claude-design]], [[bring-your-own-hero-video-to-claude-design-with-matched-first-and-last-frames]], [[paste-a-word-level-transcript-claude-design-cannot-hear-video]]
