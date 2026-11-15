---
id: set-deny-instead-of-prompting-for-unattended-sessions
created: 2026-11-15
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Set permissions.denyInsteadOfPrompting so unattended sessions deny what would have waited for a prompt and keep going

## TL;DR

A new boolean makes any call that would block on a permission prompt come back as a denial, so the turn carries on instead of hanging.

## Why it matters

Overnight loops, subagents and teammates used to stall silently on the first unapproved call. The docs say it works with whatever permission mode you are in, and unlike `dontAsk` it is a separate key.

## How to apply

Put `"permissions": {"denyInsteadOfPrompting": true}` in user or managed settings (or pass it via `--settings`) for unattended runs, then read the denials afterwards and add allow rules for the ones that were legitimate.

Checked: `denyInsteadOfPrompting` has 22 hits in the installed Claude Code 2.1.325 binary.

> "Added `permissions.denyInsteadOfPrompting` setting: a tool call that would wait on a permission prompt is denied and the turn continues, in terminal sessions, subagents and teammates", Claude Code CHANGELOG 2.1.319

## Related

[[auto-mode-pauses-after-repeated-blocks-headless-runs-skip-the-action]]
