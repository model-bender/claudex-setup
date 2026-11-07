---
id: set-onfailure-block-on-guard-hooks-so-they-fail-closed
created: 2026-10-11
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Set onFailure: "block" on Guard Hooks So a Hook That Cannot Run Stops the Action

## TL;DR

By default a command or HTTP hook that cannot start, times out, or exits with an unexpected code lets the action through; since 2.1.295 `onFailure: "block"` makes it fail closed.

## Why it matters

A guard hook whose only job is to deny (a force-push blocker, a secret-path blocker) is worthless if it fails open, and a crashed hook looks the same as a hook with nothing to object to.

## How to apply

Add `onFailure: "block"` to each command or HTTP hook that exists to deny, and leave advisory hooks on the default. Confirm it once with a copy of the hook that exits 1 and check the call is blocked. Checked against the changelog only: the bare `onFailure` token in the 2.1.296 binary is dominated by unrelated engine strings, so the exact placement in the hook definition was not confirmed from the binary.

> "Added `onFailure: "block"` for command and HTTP hooks: a hook that can't start, times out, or exits with an unexpected code blocks the action instead of letting it through", Claude Code CHANGELOG 2.1.295

## Related

[[a-guard-hook-that-cannot-match-or-serialize-now-blocks-the-call]]
