---
id: set-autocompact-once-for-each-model-you-use
created: 2026-10-11
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Run /autocompact Once for Each Model You Use: the Window Is Saved Per Model

## TL;DR

Since 2.1.288 the auto-compact window is stored per model, so a budget set while on one model does not apply after `/model` switches to another.

## Why it matters

A 100K budget set on Opus is not in force when you switch to Sonnet or Haiku, so that session can run to the full context limit without compacting, in the range where retrieval quality has already dropped.

## How to apply

Switch to each model you use and run `/autocompact <tokens>` on it once. Check the value after any model switch. Checked: `/autocompact` has 7 hits in the 2.1.296 binary.

> "Changed `/autocompact` to save the auto-compact window per model, so each model keeps its own setting when you switch", Claude Code CHANGELOG 2.1.288

## Related

[[set-a-fixed-token-auto-compact-window]], [[run-autocompact-200k-behind-a-gateway-that-stops-at-200k]]
