---
id: opt-out-of-claude-ai-skill-and-plugin-sync
created: 2026-09-24
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Sync of claude.ai Account Skills/Plugins Into Terminal Sessions Can Be Turned Off Per-Kind

## TL;DR

As of 2.1.275, signing into a terminal Claude Code session with your claude.ai account automatically pulls in whatever skills and plugins are enabled on that account; two separate settings keys let you opt out of skills syncing, plugin syncing, or both independently.

## Why it matters

This is a new source of tools/skills showing up in a terminal session that you didn't explicitly install there, driven purely by your claude.ai account state; if you want a terminal session's tool surface to be fully deliberate (e.g. for a clean/minimal-context session, or to avoid an account-level skill you don't want active everywhere), you need to know this sync exists and how to turn each half off.

## How to apply

Set `syncClaudeAiSkills: false` and/or `syncClaudeAiPlugins: false` in settings.json to stop terminal sessions signed in with your claude.ai account from auto-pulling that account's enabled skills/plugins. Checked: `syncClaudeAiSkills` and `syncClaudeAiPlugins` both confirmed present in the installed 2.1.281 binary (command grep -c -a: 8 hits each).

> "Added syncing of the skills and plugins enabled on your claude.ai account to terminal sessions signed in with it; opt out with `syncClaudeAiSkills: false` or `syncClaudeAiPlugins: false`", Claude Code CHANGELOG 2.1.275
