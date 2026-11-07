---
id: score-video-takes-frame-by-frame-instead-of-eyeballing-smoothness
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-design-get-dangerously-good-at-website-animation_c3B5OMF9MNs_20260910.txt
---

# Have Claude Score Candidate Video Takes Frame by Frame Instead of Judging Smoothness by Eye

## TL;DR

Generate several takes of a motion clip, then have Claude write a throwaway script that measures how much changes between consecutive frames and ranks them. At full speed every take looks smooth; jerk only shows up once the clip is driven by the cursor.

## Why it matters

Tristen O'Brien is blunt that human review fails here: 'with your naked eye, it's hard to tell which one is the smoothest by just watching it, they all look pretty smooth at full speed.' The reason the difference matters is that the clip will not be played at full speed, it will be scrubbed, so any frame-to-frame jump becomes a visible stutter under the mouse. Claude's pass measures the change between frames rather than judging vibes, which is a measurement the eye cannot do at 30 frames per second.

## How to apply

Ask Claude Code to take the candidate clips, extract frames, score each take by inter-frame change, and report which is genuinely the smoothest rather than which looks smoothest. In the same pass have it upscale the winner to 4K and interpolate to double the frame count, which gives the cursor more distinct positions to land on. Expect this prompt to be long (O'Brien's runs past 400 words across six paragraphs); keep it in a file rather than retyping it per project.

## Related

[[one-hero-clip-scrubbed-by-scroll-for-an-immersive-site]], [[generate-both-extremes-of-a-character-turn-as-stills]], [[visual-self-validation-screenshot-grading]]
