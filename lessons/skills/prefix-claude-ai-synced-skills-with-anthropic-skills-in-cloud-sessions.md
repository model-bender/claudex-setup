---
id: prefix-claude-ai-synced-skills-with-anthropic-skills-in-cloud-sessions
created: 2026-09-13
status: active
supersedes: null
category: skills
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Qualify a claude.ai-Synced Skill as `anthropic-skills:<name>` in a Cloud Session

## TL;DR

Skills synced from claude.ai into cloud sessions are namespaced `anthropic-skills:<name>`; the bare name resolves only when nothing else claims it.

## Why it matters

Invoking a skill by bare name is muscle memory built in local sessions. In a cloud session with a same-named project or plugin skill, the bare name quietly resolves to the wrong one rather than erroring.

## How to apply

In a cloud session, reference an ambiguous synced skill as `anthropic-skills:<name>`. Verified present in the installed 2.1.270 binary (6 occurrences of `anthropic-skills`).

> "Changed skills synced from claude.ai in cloud sessions to be named `anthropic-skills:<name>`, matching Claude Desktop; the bare name still works when nothing else uses it", Claude Code CHANGELOG 2.1.269
