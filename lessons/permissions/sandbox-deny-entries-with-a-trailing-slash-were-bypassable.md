---
id: sandbox-deny-entries-with-a-trailing-slash-were-bypassable
created: 2026-08-07
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Audit Sandbox Deny Entries for Trailing Slashes, Which Were Silently Bypassable Before 2.1.224

## TL;DR

A sandbox filesystem deny rule written with a trailing slash, such as `denyRead: "~/.aws/"`, was silently bypassable on both Linux and macOS until 2.1.224. Grep your settings for trailing-slash deny entries and confirm they now actually hold.

## Why it matters

This is the worst class of security bug: the rule was present, looked correct in the settings file, and produced no warning, so every audit of that config would have passed while the path stayed readable. Anyone who wrote deny paths in directory form (a natural way to write them) had a hole in the exact place they thought they had a wall, for as long as they were on an earlier version.

## How to apply

Grep your settings for deny entries ending in `/` (`denyRead`, `denyWrite`, and friends), upgrade to 2.1.224 or later, and re-test the ones that matter by asking Claude to read a denied path and confirming it is refused. Do not assume a rule works because it is present and syntactically valid.

> "Fixed sandbox filesystem deny entries written with a trailing slash (e.g. `denyRead: \"~/.aws/\"`) being silently bypassable on Linux and macOS", Claude Code CHANGELOG 2.1.224

## Related

[[keep-credentials-out-of-the-agent-sandbox]], [[sandbox-network-strict-allowlist-for-unattended-runs]], [[contain-agents-at-environment-layer-not-permission-prompts]]
