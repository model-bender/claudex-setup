---
id: relocate-automode-config-to-user-settings
created: 2026-07-17
status: active
supersedes: null
category: permissions
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Move autoMode Config Out of settings.local.json: It's Now Ignored There

## TL;DR

An `autoMode` block in the repo-resident `.claude/settings.local.json` is now silently ignored; auto-mode config is read only from user-level `~/.claude/settings.json`.

## Why it matters

Auto mode auto-approves actions, so honoring its config from a repo-resident file let the repo you're working in influence how much gets auto-approved. Claude Code closed that by reading `autoMode` only from user scope, which silently breaks any existing `settings.local.json` auto-mode config until you move it.

## How to apply

Relocate your `autoMode` settings from any `.claude/settings.local.json` into `~/.claude/settings.json` (user scope). If auto mode suddenly behaves differently after an upgrade, check whether your config was stranded in a local settings file.

> "Changed auto mode to no longer read `autoMode` from `.claude/settings.local.json` (repo-resident); use `~/.claude/settings.json` instead", Claude Code CHANGELOG 2.1.207

