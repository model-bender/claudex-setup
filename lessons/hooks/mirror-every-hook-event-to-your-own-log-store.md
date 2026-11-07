---
id: mirror-every-hook-event-to-your-own-log-store
created: 2026-09-12
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Mirror Every Hook Event to Your Own Log Store for an Audit Trail

## TL;DR

In a regulated setting (healthcare, payments), register a function hook on every Claude Code event that ships the result to your organisation's log store, so there is an auditable record of exactly what the agent did.

## Why it matters

Session transcripts live on the operator's machine and disappear with cleanup settings, which is not an audit trail. Hooks fire on every event regardless of what the model decides, so the log is complete by construction rather than by the agent remembering to write it.

## How to apply

Register one hook across all events that forwards the event payload to your log endpoint, and treat the forward as fire-and-forget so a logging outage never blocks the session. Scrub secrets in the same hook if you are also running redaction.

## Related

[[silently-index-conversations-on-sessionend-and-precompact-hooks]], [[ralph-loop-require-git-commit-per-task]], [[redact-secrets-before-they-enter-the-transcript]]
