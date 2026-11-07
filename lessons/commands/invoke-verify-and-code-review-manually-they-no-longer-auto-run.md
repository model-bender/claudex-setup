---
id: invoke-verify-and-code-review-manually-they-no-longer-auto-run
created: 2026-07-25
status: active
supersedes: null
category: commands
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Invoke `/verify` and `/deep-research` Yourself: Claude Does Not Start Them on Its Own

## TL;DR

`/verify` (since 2.1.215) and `/deep-research` (since 2.1.218) start only when you invoke them, so a workflow that relied on Claude reaching for them unprompted silently skips verification. `/code-review` went manual in 2.1.215 too, but since 2.1.246 Claude can start it on its own again.

## Why it matters

A pipeline whose quality gate was "Claude will run `/verify` when it matters" quietly lost its gate. The failure mode is an unverified change that looks exactly like a verified one, not an error message, so you find out at merge, or later.

## How to apply

Call `/verify` explicitly at the end of a task, or encode it as a numbered step in CLAUDE.md so the invocation is structural rather than remembered. Do the same for `/code-review` wherever a review must happen every time: Claude may start it on its own now, but may is not a gate. The companion 2.1.218 line reads "Changed `/deep-research` to start only when invoked manually; Claude no longer launches it on its own".

> "Claude no longer runs the `/verify` and `/code-review` skills on its own; invoke them with `/verify` or `/code-review` when you want them", Claude Code CHANGELOG 2.1.215

Corrected 2026-10-03: the `/code-review` half is out of date. A headless probe on 2.1.288 (telemetry off) listed `code-review` among the skills the model's Skill tool offers, while `verify` and `deep-research` were absent. In the 2.1.288 binary the built-in verify skill registers `disableModelInvocation:()=>!$tr()`, a server-side flag that was off for this account, so Claude may start `/verify` unprompted on accounts where the flag is on.

> "Changed `/code-review` so Claude can also start it on its own on Bedrock, Vertex AI, and Foundry, through the Claude apps gateway, and when telemetry or non-essential traffic is disabled", Claude Code CHANGELOG 2.1.246

## Related

[[encode-the-whole-task-lifecycle-in-claude-md-with-every-stage-in-a-subagent]]
