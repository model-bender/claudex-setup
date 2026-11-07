---
id: call-a-cheap-model-from-a-function-hook
created: 2026-09-12
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Call a Cheap Model From Inside a Function Hook With $model

## TL;DR

Hooks can invoke a model. A turn-end hook that passes the turn to Haiku for a one-line summary and sends it to the operating system's text-to-speech is a small persistent prompt plus a $model call, and the same primitive can generate keywords that a $http call uses to pull context back into the session.

## Why it matters

Until now a hook could only run a script, so anything needing judgment had to interrupt the main model. $model puts a cheap model inside the hook, which is what makes spoken turn summaries, prompt enrichment from a company knowledge base, and quiz-before-PR gates possible without spending main-session tokens.

## How to apply

Write the hook with a short system prompt plus a $model call to Haiku, then pipe the result wherever it goes (TTS, a UI row, an injected context string). Pair it with $http when the hook needs to reach an internal service.

## Related

[[userpromptsubmit-hook-auto-injects-semantic-memory-matches]], [[enable-function-hooks-to-unlock-plugin-authoring]]
