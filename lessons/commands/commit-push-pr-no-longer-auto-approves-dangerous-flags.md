---
id: commit-push-pr-no-longer-auto-approves-dangerous-flags
created: 2026-08-16
status: active
supersedes: null
category: commands
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# `/commit-push-pr` No Longer Auto-Approves `--force`, `--amend` or `--no-verify`

## TL;DR

The bundled `/commit-push-pr` skill used to auto-approve git/gh commands carrying destructive flags; since 2.1.229 it prompts instead, which is a hard stop for any headless or overnight pipeline that ends in that command.

## Why it matters

Two-sided, and both sides matter. Historically, a `--force` push could go out under a command you invoked purely for convenience - no confirmation, no second look.

Going forward, an unattended loop that finishes with `/commit-push-pr` now hangs on a permission prompt instead of completing. Under `-p` or behind a Stop hook, there is no obvious signal explaining why the run stalled; it just never finishes.

## How to apply

Either drop the dangerous flags from your commit/PR flow entirely, or add explicit `permissions.allow` rules for the exact git/gh invocations you are willing to accept before running `/commit-push-pr` unattended.

> "Changed `/commit-push-pr` so git/gh commands with dangerous flags (`--force`, `--amend`, `--no-verify`, etc.) are no longer auto-approved", Claude Code CHANGELOG 2.1.229

## Related

[[guard-unattended-agent-runs-with-a-stall-watchdog-and-bounded-retry]]
