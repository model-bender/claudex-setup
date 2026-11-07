---
id: transcribe-the-video-first-so-motion-graphics-land-on-the-spoken-words
created: 2026-10-02
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/opus-5-5-just-changed-video-editing-forever-free-skills_7jHXoPGnA4c_20261002.txt
---

# Transcribe a Video First So an Agent Can Time Animations to What Is Said

## TL;DR

For agent-driven video editing, make transcription the first step. It lets the agent land graphics at the right moments and also find mistakes and dead space to cut.

## Why it matters

The creator's first instruction in each video-editing prompt is to transcribe the clip so animations arrive at the exact right time. They list transcription as essential, with cutting mistakes and dead air as the next step, and note you can use the ElevenLabs API (paid per use, a bit quicker) or Whisper (local, free, slower). They had Claude set up whichever they chose.

## How to apply

Ask Claude Code to set up Whisper or ElevenLabs transcription, then to transcribe the clip before any animation work. In the prompt, tell it to use the transcript to cut mistakes and long gaps and to place each graphic where you name it.

Verified: Process advice with no tool flag to check. The Whisper versus ElevenLabs trade-off is the creator's statement.

## Related

[[hyperframes-claude-code-video-rendering-pipeline]], [[hosted-whisper-api-for-concurrent-video-transcription]], [[feed-raw-video-to-claude-code-or-codex-and-say-watch-dont-just-transcribe]]
