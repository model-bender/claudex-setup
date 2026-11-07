---
id: sandbox-plus-http-proxy-domain-allowlist-for-skip-permissions
created: 2026-09-01
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Pair Sandbox Mode With Your Own HTTP Proxy Script to Domain-Allowlist Internet Access

## TL;DR

Instead of running dangerously-skip-permissions with unrestricted internet, enable the sandbox and write an HTTP proxy script that only allows a specific list of domains.

## Why it matters

Most people who run permissions-bypassed locally never restrict internet access, leaving the agent free to hit any site including ones that could carry prompt injections.

## How to apply

Enable Claude Code's sandbox, then build (or have Claude Code build) an HTTP proxy script that whitelists only the domains relevant to the current task (e.g. company sites, trusted docs), and route the sandboxed session's traffic through it.

## Related

[[sandbox-network-strict-allowlist-for-unattended-runs]], [[sandbox-mode-for-safe-exploration]]
