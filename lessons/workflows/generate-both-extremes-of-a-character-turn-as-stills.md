---
id: generate-both-extremes-of-a-character-turn-as-stills
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-design-get-dangerously-good-at-website-animation_c3B5OMF9MNs_20260910.txt
---

# Generate Both Ends of a Character's Turn as Stills Before Asking for the Video

## TL;DR

For a hero character that tracks the cursor, generate three stills (head 70 degrees left, centre, 70 degrees right) from the same original, then ask for a 5 second clip travelling from still one to still three. Handing a video model one still and asking it to invent the turn produces a clip that snaps.

## Why it matters

Tristen O'Brien names the single-still approach as the mistake: 'what a lot of people do here is they take that static image that they have, and they hand it to a video model, and they just ask it to make a video of its head turning back and forth, that's a big mistake, your video is going to snap in place instead of being that smooth back and forth.' The 70 degree figure is deliberate rather than aesthetic: at 90 degrees 'it's going to lose both of its eyes' and the character stops reading as looking at the viewer, which kills the effect. Pinning both extremes means the video model interpolates between two known frames rather than inventing the range of motion.

## How to apply

Take the original centred still, hand it back and ask for two variants with everything identical except the head rotated about 70 degrees left and about 70 degrees right. Label them 1 (left), 2 (centre), 3 (right). Give all three to the video model with an explicit motion contract: start at position 1, end at position 3, turn smoothly at a consistent speed, keep the body frozen, and return three variations to choose from. On the page the clip is embedded paused and the cursor's horizontal position selects the frame, so cursor left shows still 1 and cursor right shows still 3.

## Related

[[one-hero-clip-scrubbed-by-scroll-for-an-immersive-site]], [[bring-your-own-hero-video-to-claude-design-with-matched-first-and-last-frames]], [[claude-design-static-camera-for-seamless-background-loop-video]]
