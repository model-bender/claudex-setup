---
id: leave-codex-locked-use-off-on-macos
created: 2026-08-29
status: active
supersedes: null
category: gotchas
source_type: post
tool: codex
sources:
  - https://x.com/swyx/status/2092492963435946494
---

# Don't Enable Codex's "Locked Use" Capability on macOS: It Can Lock You Out of Your Keychain

## TL;DR

Codex's locked-use capability rides on unstable macOS features and repeatedly locked swyx out of his macOS keychain; leave it off until it stabilizes.

## Why it matters

A keychain lockout is machine-level damage far beyond a bad agent run, and the underlying macOS issue is acknowledged on Apple's developer forums as a known bug, so no Codex-side setting protects you while it is enabled.

## How to apply

Leave the locked-use capability disabled in Codex on macOS; re-check the Codex changelog and Apple forums before enabling it again. Verified via the r.jina.ai mirror of swyx's timeline (posted 2026-08-26).

> "PSA: do not use codex \"locked use\" capabilities right now. it is currently relying on unstable mac features and has completely locked me out of my macos keychain twice this week.", swyx
