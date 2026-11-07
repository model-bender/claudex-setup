---
id: centre-the-hero-character-to-leave-room-for-motion
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-design-get-dangerously-good-at-website-animation_c3B5OMF9MNs_20260910.txt
---

# Centre the Character in the Source Image So It Has Room to Turn Later

## TL;DR

When generating a hero character that will later track the cursor or scroll, put it dead centre of the frame with clear space on both sides. Off-centre framing leaves no room for the motion you have not generated yet.

## Why it matters

Tristen O'Brien calls this out as the thing to get right at image-generation time, before any video exists: 'you want to make sure that your character is centered in the middle of the screen, and that's because it's going to give them room on both sides to turn its head left and right as you move the mouse around.' The cost of missing it is not a bad frame, it is a re-generation of the whole asset chain: the two turn extremes and the interpolated clip are all derived from this still, so a cropped turn is discovered three steps downstream.

## How to apply

In the image prompt, fix the composition as well as the subject: centred in frame, facing the camera, headroom and equal negative space on the left and right. Check the returned image for the space before deriving anything from it. Ask for four variations of the character so you can pick the one that is both on-brand and correctly framed.

## Related

[[generate-both-extremes-of-a-character-turn-as-stills]], [[bring-your-own-hero-video-to-claude-design-with-matched-first-and-last-frames]]
