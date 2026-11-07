---
id: run-codex-doctor-network-only-when-codex-cannot-reach-the-model
created: 2026-11-06
status: active
supersedes: null
category: gotchas
tool: codex
source_type: canonical
sources:
  - https://github.com/openai/codex/releases/tag/rust-v0.166.0
---

# Run codex doctor --network-only First When Codex Cannot Reach the Model

## TL;DR

`codex doctor --network-only` checks config, network environment, provider HTTP and the Responses WebSocket without the full health report.

## Why it matters

Proxy, VPN and sandbox network problems otherwise show up as vague reconnect loops; the narrow check separates a network fault from an auth or config fault.

## How to apply

Run `codex doctor --network-only` (add `--json` for a redacted machine-readable report) before changing sandbox or proxy settings.

Checked: `codex doctor --help` on 0.167.0 lists `--network-only` ("Run config, network environment, provider HTTP, and Responses WebSocket checks") and `--json` ("Emit a redacted machine-readable report").

> "Added `codex doctor --network-only` for focused configuration, connectivity, and WebSocket diagnostics.", openai/codex release notes 0.166.0
