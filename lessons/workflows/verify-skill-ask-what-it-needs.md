---
id: verify-skill-ask-what-it-needs
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Ask /verify What It Needs From You Before Assuming End-to-End Verification Is Impossible

## TL;DR

Instead of guessing why a change can't be verified end-to-end, ask the /verify skill directly what tools, credentials, or environment it would need to complete verification.

## Why it matters

In the transcript, the presenter runs /verify after a voice-mode feature and it can't verify end-to-end (a live voice call) locally because LiveKit CLI and API keys aren't installed. Asking /verify 'what would you need from me to verify this end to end' makes it enumerate exactly what's missing (LiveKit CLI setup, a fake-mic audio strategy, a token budget for test calls, a Slack channel for the recording) instead of you inferring it.

## How to apply

After a build, invoke the /verify skill and explicitly ask it to list the tools/credentials/environment it would need for full end-to-end verification of this and future changes in this part of the project, then set those up once so future verifications aren't blocked.

