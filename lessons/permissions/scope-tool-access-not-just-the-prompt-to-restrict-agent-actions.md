---
id: scope-tool-access-not-just-the-prompt-to-restrict-agent-actions
created: 2026-08-07
status: active
supersedes: null
category: permissions
tool: claude-code
about: null
sources:
  - transcripts/nate-herk-ai-automation/5000-hours-of-building-ai-in-just-17-minutes_7WZ6XldxX0U_20260807.txt
---

# Scope Tool Access, Not Just the Prompt, to Restrict What an Agent Can Do

## TL;DR

A prompt instruction like "only draft, never send" is a suggestion the model can violate; the only real restriction is removing or scoping the underlying tool/API key so the forbidden action is physically impossible.

## Why it matters

Models are non-deterministic, the same instruction can be followed 99 times and ignored once. An agent with a send-email tool that was told "only draft" sent a discount code to 150,000 people because a to-do item read as an implicit go-ahead; nothing forced it to stop at drafting. A rule that lives only in the prompt degrades every time you swap models, add context, or hit an edge case the prompt didn't anticipate; a rule enforced by the tool itself doesn't.

## How to apply

For every tool, database, file path, and API key an agent can reach, assume it will eventually use it, then ask "can it only draft, or can it also send?" If the answer is scarier than intended, fix the access, not the prompt: issue scoped API keys (draft-only, read-only, no-delete) so the capability itself is capped, rather than relying on instructions to hold the line.

## Related

[[contain-agents-at-environment-layer-not-permission-prompts]], [[harden-always-on-agents-least-privilege-and-capable-models]], [[start-an-email-routine-on-drafts-only-never-send]]
