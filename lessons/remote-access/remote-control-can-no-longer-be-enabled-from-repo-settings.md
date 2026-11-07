---
id: remote-control-can-no-longer-be-enabled-from-repo-settings
created: 2026-08-07
status: active
supersedes: null
category: remote-access
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Enable Remote Control at User Scope: Repo-Local Settings Can Only Turn It Off Now

## TL;DR

As of 2.1.222, `.claude/settings.json` and `.claude/settings.local.json` can still disable Remote Control auto-start but can no longer enable it. Enabling is a user-scope action via `/config`.

## Why it matters

This closes a real supply-chain style hole: a repo you clone or a plugin you install could previously flip on remote control of your session just by shipping a settings file. Turning it on is now a deliberate per-user decision rather than something a checked-in file can do to you. The asymmetry is intentional, since letting a repo turn it *off* is harmless.

## How to apply

If you relied on a repo-committed setting to auto-enable Remote Control for collaborators, that no longer works: each person enables it themselves via `/config`. Treat this as the general pattern for project-local config, which is untrusted for anything that expands capability.

> "Changed Remote Control auto-start so repo-local settings (`.claude/settings.json` or `.claude/settings.local.json`) can no longer turn it on (they can still turn it off); enable it at user scope via `/config`", Claude Code CHANGELOG 2.1.222

## Related

[[contain-agents-at-environment-layer-not-permission-prompts]], [[relocate-automode-config-to-user-settings]]
