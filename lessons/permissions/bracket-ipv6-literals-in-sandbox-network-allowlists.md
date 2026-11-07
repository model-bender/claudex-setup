---
id: bracket-ipv6-literals-in-sandbox-network-allowlists
created: 2026-08-16
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Bracket IPv6 Literals in Sandbox Network Lists, Then Run `/doctor`

## TL;DR

An unbracketed IPv6 entry in a sandbox network domain list is an ambiguous spelling; since 2.1.229 it is enforced fail-closed and flagged by `/doctor`, which means a rule like `::1:443` never meant what it looked like before that release.

## Why it matters

This is the same family as the trailing-slash deny-entry bug already in the corpus: a network rule that parses cleanly, warns about nothing, and does not hold. That is the worst shape of security bug, because the config file reads as though the protection is in place.

Fail-closed is the safe direction, but it cuts both ways - an allowlist that appeared to work before the upgrade may start blocking traffic afterwards. That is the rule being enforced correctly for the first time, not a regression.

## How to apply

Rewrite every IPv6 entry in `sandbox.network` domain lists in bracketed form (`[::1]:443`), then run `/doctor` and fix whatever it flags as ambiguous.

> "Improved sandbox: IPv6 literals in network domain lists are now bracketed (`[::1]:443`), and ambiguous spellings are enforced fail-closed and flagged by `/doctor`", Claude Code CHANGELOG 2.1.229

## Related

[[sandbox-deny-entries-with-a-trailing-slash-were-bypassable]], [[sandbox-network-strict-allowlist-for-unattended-runs]]
