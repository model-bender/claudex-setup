---
id: reload-plugins-after-a-repo-local-plugin-install
created: 2026-09-01
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-memory-system-compared-so-you-don-t-have-to_20260424.txt
---

# Run /reload plugins After Installing a Repo-Local Plugin, or It Stays Inactive

## TL;DR

Installing a plugin scoped to just the current repo writes to settings.local.json but doesn't activate it; you have to run /reload plugins (or restart) before Claude Code will use it.

## Why it matters

A plugin that's present in settings but not reloaded looks installed yet its skills and hooks never fire, which reads as a broken plugin rather than a missing activation step.

## How to apply

After running /plugin marketplace add <repo> and /plugin install <name> scoped to 'this repo only', run /reload plugins to activate it without a full restart.

## Related

[[plugin-system-install-from-marketplace]]
