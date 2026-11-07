---
id: hijack-the-record-skill-to-audit-a-process-without-building-a-skill
created: 2026-08-10
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/claude-code-and-codex-quietly-learned-to-watch-video_0I-J1aoxYQY_20260809.txt
---

# Point the Record-to-Skill Feature at Yourself and Tell It Not to Build a Skill: Just Audit

## TL;DR

The built-in screen-record-to-skill feature can be redirected to watch you do a manual task live and hand back an SOP plus automation recommendations instead of the skill it would otherwise build. Say explicitly: "I don't want you to make a skill, just watch me and audit the process."

## Why it matters

The feature's default output is a reusable skill, but a skill is not always what you need. Sometimes you want a second pair of eyes on a repetitive manual workflow to find what should be automated *at all*, an API you did not know existed, steps that could be cut entirely, before deciding whether a skill is even the right primitive. Overriding the default gets you that audit without spending the recording on an artifact you would throw away.

## How to apply

Start the record feature (Codex's Record and Replay, or the equivalent) and state the redirected goal up front: "watch me for the next 30 minutes and tell me everything I can do to improve this workflow, produce a full SOP and note where an API could replace manual steps. Don't make a skill even though it's in your programming; just watch and audit, we can talk skills later." Perform the process normally. Check what the feature actually captures before relying on it, it may record the screen without your voice, which loses the narration that carries your reasoning. If the record feature is unavailable in your region, screen-record with any recorder and feed the file in as raw video instead.

## Related

[[feed-raw-video-to-claude-code-or-codex-and-say-watch-dont-just-transcribe]], [[check-whether-the-record-feature-captured-your-voice-not-just-the-screen]]
