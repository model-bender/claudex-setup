---
id: hosted-whisper-api-for-concurrent-video-transcription
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-just-destroyed-every-video-editing-tool_ZNbgOhxhzXg_20260624.txt
---

# Use a Hosted Whisper API Instead of Local whisper.cpp When Running Several Video Sessions at Once

## TL;DR

Local whisper.cpp transcription for word-level video timestamps eats a lot of RAM; if you're running multiple video-editing agent sessions in parallel, switch to a hosted Whisper API (e.g. via an OpenAI key) instead.

## Why it matters

The creator had to uninstall local whisper.cpp because running roughly eight video sessions simultaneously was killing his RAM; the API alternative offloads the compute.

## How to apply

When a video-editing skill asks whether to transcribe locally or via API, hand it an API key (OpenAI's Whisper endpoint) instead of letting it install and run whisper.cpp locally, particularly if you expect to run several sessions concurrently.
