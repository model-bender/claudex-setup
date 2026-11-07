---
id: rewind-to-undo-an-unhelpful-fork
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-subagent-upgrade-yet_20260424.txt
---

# Use /rewind to Undo a Forked Subagent's Result You Didn't Want

## TL;DR

If a forked subagent's answer isn't helpful, run /rewind to go back to before you spun it up, since a fork's spawn and result are part of the main conversation's timeline.

## Why it matters

Forks run inline (unlike a background subagent), so their invocation and output show up as turns you can roll back, letting you discard a bad tangent cleanly instead of manually correcting course.

## How to apply

After a forked subagent returns an unhelpful result, run /rewind and select the point before you asked for the fork, then try a different approach.

## Related

[[rewind-instead-of-arguing-with-stale-context]]
