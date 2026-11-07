---
id: scope-hooks-to-one-subagent-skill-or-command-in-its-frontmatter
created: 2026-09-01
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# Scope PreToolUse/PostToolUse/Stop Hooks to One Subagent, Skill, or Command in Its Own Frontmatter

## TL;DR

Subagents, skills, and slash commands can define their own pretooluse, posttooluse, and stop hooks directly in frontmatter, so the hook only fires for that agent, skill, or command instead of every task via settings.json.

## Why it matters

A global settings.json hook runs for everything, which is the wrong tool when you only want a check (like 'did types compile') or a side effect (like a deploy health-check notification) to happen around one specific subagent's work.

## How to apply

In a subagent's (or skill's/slash command's) frontmatter, add a hooks block with pretooluse, posttooluse, and/or stop entries plus matchers, e.g. a Cloudflare-deploy subagent whose PreToolUse hook checks type compilation and whose PostToolUse hook runs a health check and sends a desktop notification.

## Related

[[guard-skill-env-secrets-with-skill-scoped-hooks]]
