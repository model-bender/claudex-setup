---
id: feed-raw-video-to-claude-code-or-codex-and-say-watch-dont-just-transcribe
created: 2026-08-10
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/claude-code-and-codex-quietly-learned-to-watch-video_0I-J1aoxYQY_20260809.txt
---

# Drag a Raw Video Into Claude Code or Codex and Tell It to Watch, Not Just Transcribe

## TL;DR

Both Claude Code and Codex now natively ingest a raw video file or a link to one, breaking it into timestamped frames plus the audio transcript, no skill, plugin, or Gemini hand-off required. Say explicitly "watch it end to end" or they default to pulling only the transcript and miss everything visual.

## Why it matters

This supersedes the older route of compressing the file and shipping it to Gemini's video-understanding API, which existed only because Claude and Codex could not watch anything themselves. That hand-off is now unnecessary work and an extra API bill. The underlying value is unchanged and still the point: a screen recording of you narrating over your own product, or over a reference site you want to emulate, substitutes for a long written brief. The agent sees exactly what you looked at paired with what you said about it, including the tacit "under your breath" reasoning you would never write down, instead of you translating that understanding into text first.

## How to apply

Drag the MP4 into the chat, or give a URL (a Loom link works, tell it to download first) and state the goal plus "watch this end to end, don't just pull the transcript, look at everything I'm looking at." Narrate while recording, with the mic on: the reasoning you speak is most of the value. If installed skills intercept video downloads, add "don't use any skills" to force vanilla libraries. Keep videos short (10-20 min) and lower-resolution, frames are processed individually and are context-heavy, so long or high-res footage burns the window fast; a compression step still helps for that reason, just not for a third-party API. To turn a recording into a skill, ask for a comprehensive SOP capturing every nuance first, then hand that SOP to `skill-creator` in plan mode, wiring an ask-user-input tool for human checkpoints; restart the session before invoking the freshly installed skill. Also works for auditing your own site from a self-recorded walkthrough, or cloning a reference site's feel by narrating over it.

## Related

[[hijack-the-record-skill-to-audit-a-process-without-building-a-skill]], [[screenshot-paste-instead-of-describing-ui-problems]], [[paste-a-word-level-transcript-claude-design-cannot-hear-video]], [[turn-a-recording-into-an-sop-first-then-hand-that-to-skill-creator]]
