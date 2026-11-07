---
id: redact-secrets-before-they-enter-the-transcript
created: 2026-09-12
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Redact Secrets at the Prompt With a Function Hook That Swaps in an ID

## TL;DR

A function hook can intercept your input, detect high-entropy strings, emails and IP addresses, replace each with an ID, hold the real value in the hook's in-memory store, and substitute it back only when a tool actually needs it.

## Why it matters

Once a key lands in the session transcript your options are deleting the transcript or rotating the key. In the demo an Anthropic API key was pasted into the prompt, was replaced with an ID the moment enter was pressed, and the subsequent API request still succeeded because the hook rewrote the ID back to the real key at call time. The agent used a secret it never saw.

## How to apply

Ask /plugin-authoring for a hook that blocks secrets from entering the session transcript by measuring entropy, plus patterns for emails and IP addresses. Keep the values in the per-session variable store, not the persistent one.

## Related

[[put-api-keys-only-in-dot-env-files]], [[guard-skill-env-secrets-with-skill-scoped-hooks]]
