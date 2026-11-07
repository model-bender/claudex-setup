---
id: turn-a-recording-into-an-sop-first-then-hand-that-to-skill-creator
created: 2026-09-12
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/mark-kashef/claude-code-and-codex-quietly-learned-to-watch-video_0I-J1aoxYQY_20260809.txt
---

# Convert a Screen Recording Into an SOP Before Handing It to skill-creator

## TL;DR

Do not ask the agent to turn a recording straight into a skill. Ask first for a comprehensive SOP capturing every nuance, then hand that SOP to skill-creator in plan mode, and restart the session before invoking the freshly installed skill.

## Why it matters

A recording plus 'make me a skill' collapses two jobs into one pass: extracting what you actually did, and encoding it as an artifact. Splitting them gives you a reviewable intermediate, the SOP, that you can correct before it is baked into a skill you will then debug blind. Plan mode on the skill-creator step gives a second checkpoint before files are written, and the session restart matters because a skill installed mid-session is not picked up until the session reloads.

## How to apply

After the agent has watched the recording, prompt for a comprehensive SOP capturing every nuance of the process, read and correct it, then pass the SOP to skill-creator in plan mode, wiring an ask-user-input tool wherever the process needs a human checkpoint. Restart the session before invoking the new skill.

## Related

[[feed-raw-video-to-claude-code-or-codex-and-say-watch-dont-just-transcribe]]
