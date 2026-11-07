---
id: one-hero-clip-scrubbed-by-scroll-for-an-immersive-site
created: 2026-08-16
status: active
supersedes: null
category: workflows
tool:
  - claude-code
  - codex
sources:
  - transcripts/mark-kashef/3d-websites-just-became-free-one-prompt_FSnubu4Lpz8_20260812.txt
---

# Budget One Hero Clip for an Immersive Scroll Site, Then Let the Agent Scrub It Frame by Frame

## TL;DR

An immersive scroll site needs exactly one video. Everything after that is mechanics the coding agent implements: split the clip into frames and map frame index to scroll position. Calibrate on a short lowest-resolution render before committing hours to the real hero clip.

## Why it matters

The expensive input looks like "lots of assets" and is actually a single clip, so getting the asset budget wrong is measured in days: hero clips took roughly 4.5 to 9 hours on a high-spec laptop, and about two days for the same job on a Mac Mini.

Once the clip exists, the immersive effect is deterministic - frame N shown at scroll position N - which is ordinary code an agent writes in one pass, and the identical architecture rebrands to a completely different site. A short lowest-resolution test tells you what your hardware can do before you commit to the long run, a free local upscaler recovers much of the quality you traded away, and the cloud render of the same clip cost about $2 if the wall-clock isn't worth it.

## How to apply

Source one hero clip that travels between the two states you want the page to move between (vault closed to vault open), ending on the state your call to action sits in.

Analyse the clip first, then tell the agent where the file is, what it depicts, and how many frames it contains; instruct it to extract the frames, read a handful of them, and wire frame index to scroll offset. Have it verify by scrolling the rendered page and checking the beats, rather than by confirming the code exists.

This is a different technique from a looping hero video, which pins the first and last frame to the same still so the camera never moves.

## Related

[[bring-your-own-hero-video-to-claude-design-with-matched-first-and-last-frames]], [[autonomous-ui-loop-acceptance-must-exercise-rendered-ui]], [[visual-self-validation-screenshot-grading]], [[render-a-long-clip-in-the-cloud-and-upscale-the-cheap-render-locally]]
