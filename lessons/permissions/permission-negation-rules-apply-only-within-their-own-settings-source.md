---
id: permission-negation-rules-apply-only-within-their-own-settings-source
created: 2026-09-13
status: active
supersedes: null
category: permissions
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Put a `!` Permission Exception in the Same Settings File as the Rule It Carves Out

## TL;DR

A `!`-prefixed deny or ask rule now applies only within the settings source that wrote it, and a bare `!` is ignored entirely.

## Why it matters

A negation written in one settings file used to reach into another, so an exception you rely on may silently stop applying after 2.1.269. Anyone running layered user, project and local settings has to re-check placement rather than assume the old cross-scope behaviour.

## How to apply

Audit every `permissions.deny` and `permissions.ask` entry containing `!` across `settings.json` and `settings.local.json`, and move each negation into the same source as the rule it modifies. Do not rely on a standalone `!` doing anything.

> "Fixed a deny or ask permission rule starting with `!` applying beyond the settings source that wrote it; such a rule now applies only within its own source, and a bare `!` negation is ignored", Claude Code CHANGELOG 2.1.269
