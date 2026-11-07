---
id: language-setting-for-reliable-non-english-responses
created: 2026-09-01
status: active
supersedes: null
category: settings
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# Set `language` in Claude Code's Settings for Reliable Non-English Responses

## TL;DR

Adding a language parameter (e.g. 'Japanese') to Claude Code's settings file makes it reliably respond in that language, rather than depending on the model catching a hint from your prompt.

## Why it matters

Asking for a non-English response inline in a prompt is inconsistent turn to turn; a settings-level language directive holds across the whole session.

## How to apply

Add a language key set to your target language in Claude Code's settings file, then prompt normally; responses come back in that language by default.
