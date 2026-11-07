---
id: update-the-codex-app-to-get-the-destructive-command-guardrails
created: 2026-08-22
status: active
supersedes: null
category: gotchas
tool: codex
source_type: post
sources:
  - https://x.com/thsottiaux/status/2089891927659585918
---

# Update the Codex app to get the destructive-command guardrails: the $HOME-deletion fixes ship client-side

## TL;DR

OpenAI's mitigations for Codex deleting user files (stricter deletion checks, harder-to-enable Full access, improved Auto-review) landed in client releases, so a pinned or stale Codex install still carries the old data-loss behavior.

## Why it matters

This is the follow-up to the July $HOME-deletion incident, and the actionable half is easy to miss: the guardrails are execution-layer checks and prompt changes in the client, not a server-side model fix. Pinning an agent CLI version for reproducibility is normal practice, and here it silently opts you out of the data-loss protections.

## How to apply

Keep the Codex client updated rather than pinned, and run under `Ask for approval` or `Approve for me`; reserve `Full access` for a container or VM you can recover. Tibo names the root cause to watch for: Codex "reusing a system environment variable like $HOME for temporary work" and a malformed cleanup then pointing at the real home directory.

> "Two things to do on your end: - Keep the Codex app up to date. We are always improving safety, performance and many other things. - Use one of the sandbox modes: \"Ask for approval\" or \"Approve for me\". Only use Full access for environments you trust and can recover.", Thibault (Tibo) Sottiaux
