---
id: sandbox-network-strict-allowlist-for-unattended-runs
created: 2026-07-25
status: active
supersedes: null
category: permissions
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Set `sandbox.network.strictAllowlist` So Unattended Sandboxed Runs Fail Instead of Hanging on a Prompt

## TL;DR

Without this setting, a sandboxed command reaching a host outside the allowlist raises a permission prompt, which in an unattended or scheduled run is an indefinite hang rather than a clean failure.

## Why it matters

Egress control is only a real boundary if it can decide on its own. A prompt-on-unknown-host policy converts a security control into a liveness problem the moment nobody is at the keyboard, and a hung scheduled run is easy to misread as a slow one.

## How to apply

Add `sandbox.network.strictAllowlist` to settings alongside your egress allowlist for scheduled, headless, and background sessions, so unexpected outbound hosts are denied outright. Keep the interactive prompt behaviour for hands-on sessions, where the prompt is information rather than a stall.

> "Added `sandbox.network.strictAllowlist` setting to deny non-allowlisted hosts for sandboxed commands without prompting", Claude Code CHANGELOG 2.1.219

## Related

[[harden-always-on-agents-least-privilege-and-capable-models]]
