---
id: import-claude-code-into-codex-and-turn-on-sync
created: 2026-08-16
status: active
supersedes: null
category: configuration
tool:
  - claude-code
  - codex
source_type: canonical
sources:
  - https://learn.chatgpt.com/docs/changelog
  - https://github.com/openai/codex/pull/36356
---

# Migrate a Claude Code Setup Into Codex With `/import`, Then Turn On Settings > Import Sync

## TL;DR

`/import` in the Codex CLI pulls instructions, settings, MCP servers, skills, plugins, projects, and recent chats across from Claude Code - and `Settings > Import` has an automatic-updates toggle that keeps the imported copy current instead of frozen at import time.

## Why it matters

This replaces the older one-shot migration offer that only appeared when you first attached a folder. `/import` is a standing command you can run at any time, from any project, so a missed prompt is no longer a config you re-enter by hand.

The sync toggle is the part nobody finds, and it is the part that matters over time: without it, imported skills and MCP servers drift the moment you edit the Claude Code side, and you are back to maintaining two copies of the same setup.

## How to apply

Run `/import` in the Codex CLI to migrate settings, MCP servers, plugins, sessions, commands, and project-scoped memories. On desktop, use the import flow, then enable automatic updates under **Settings > Import**. Re-imported sessions extend the existing Codex thread rather than duplicating it.

> "Codex CLI can also import supported setup and recent chats from Claude Code and Cursor with `/import`.", Codex changelog, 2026-08-11

## Related

[[port-a-project-between-claude-code-and-codex-by-layer]], [[codex-has-no-custom-slash-commands-port-them-as-skills]], [[route-work-between-claude-code-and-codex-by-task-type]]
