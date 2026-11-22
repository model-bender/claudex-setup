---
id: audit-hooks-that-always-print-decision-block-because-it-now-holds-in-more-cases
created: 2026-11-22
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21326
---

# Audit any hook that prints a decision of block on every run: it may now block more calls

## TL;DR

Hooks emitting `"decision": "block"` are honoured in more situations than before.

## Why it matters

A logging or advisory hook that prints the field unconditionally can start stopping tool calls after an upgrade.

## How to apply

Grep your hook scripts for `"decision": "block"` and make sure each only prints it on the path where you want a block.

Checked: changelog only

> "Changed a hook's `"decision": "block"` to hold in more cases, so a hook that always prints one may start blocking calls", Claude Code CHANGELOG 2.1.326
