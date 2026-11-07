---
id: codex-hook-lifecycle-events
created: 2026-09-01
status: active
supersedes: null
category: hooks
tool: codex
sources:
  - transcripts/john-kim/complete-beginner-s-guide-to-openai-s-codex-app_20260424.txt
---

# Codex App Hooks Fire on Five Lifecycle Events

## TL;DR

Codex app hooks can target session start, pre-tool-use, post-tool-use, after a user submits a prompt, and when the agent stops.

## Why it matters

Knowing the full event list lets you pick the right hook instead of guessing, e.g. a post-tool-use hook to lint after every edit or a stop hook to send a notification.

## How to apply

In Codex app, ask Codex to write a hook targeting one of these five events (it edits config.toml for you); for example, ask for a post-tool-use hook that lints code after every edit.

## Related

[[add-a-codex-interrupt-hook-to-capture-state-on-esc]]
