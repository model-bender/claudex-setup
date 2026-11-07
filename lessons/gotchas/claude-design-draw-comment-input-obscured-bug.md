---
id: claude-design-draw-comment-input-obscured-bug
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
  - transcripts/jono-catliff/how-i-built-insane-claude-design-websites-in-10-minutes_xYv4_cTOSNM_20260701.txt
  - transcripts/nate-herk-ai-automation/claude-design-builds-beautiful-3d-websites-instantly-full-tutorial_TcFeSjwTo7g_20260624.txt
---

# Claude Design's Draw-Tool Comment Box Can Hide What You're Typing

## TL;DR

When you circle something with the draw tool and start typing feedback, the comment input can get visually stuck or covered so you can't see the text you're entering, a research-preview UI bug two separate creators hit independently.

Drawing a shape on the Claude Design canvas to leave a comment can place the resulting comment marker low on the screen where it's easy to miss.

## Why it matters

One creator noted "the little comments get stuck down there, so it's sometimes it's hard to see" and another separately hit "it's a little bit buggy down here" trying to leave draw-tool feedback, so this isn't a one-off fluke.

The creator hit this directly while demoing draw-and-comment: "when I do the drawing thing, the little comments get stuck down there so it sometimes it's hard to see. That's just kind of a UI bug... this is in research preview so little kinks will get ironed out."

## How to apply

If the note box appears to vanish or overlap other UI while using draw-and-type feedback, send the message anyway and check the result rather than assuming the interaction failed. If it seems unreliable, prefer clicking the specific element (comment/edit) over drawing.

After drawing a comment on the canvas, scroll to check for the comment marker before assuming the draw action failed or didn't register, especially on the current research-preview build.

## Related

[[draw-on-the-claude-design-canvas-only-for-things-that-arent-elements]]
