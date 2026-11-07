---
id: deny-managed-stdio-mcp-servers-explicitly-after-2-1-305
created: 2026-10-25
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21305
---

# List Managed stdio MCP Servers in deniedMcpServers If the Allowlist Was Keeping Them Out

## TL;DR

Since 2.1.305 `allowedMcpServers` no longer filters `managed-mcp.json` stdio servers that use `${VAR}` only in `env`, so one your allowlist left out now loads on upgrade unless it is in `deniedMcpServers`.

## Why it matters

An administrator who relied on leaving a server off the allowlist gets that server started after the upgrade, with no warning.

## How to apply

Add each managed stdio server you mean to keep off to `deniedMcpServers`, then check which servers load after upgrading. Checked: `deniedMcpServers` has 31 matches and `managed-mcp.json` 20 in the installed 2.1.310 binary.

> "Changed `allowedMcpServers` to stop filtering `managed-mcp.json` stdio servers that use `${VAR}` only in `env`: one your allowlist left out now loads on upgrade; use `deniedMcpServers` to keep it off", Claude Code CHANGELOG 2.1.305
