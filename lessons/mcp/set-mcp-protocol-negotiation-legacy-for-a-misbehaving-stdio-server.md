---
id: set-mcp-protocol-negotiation-legacy-for-a-misbehaving-stdio-server
created: 2026-10-11
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Try MCP_PROTOCOL_NEGOTIATION=legacy When a Local stdio MCP Server Connects Slowly or Breaks After 2.1.292

## TL;DR

Since 2.1.292 local stdio MCP connections negotiate protocol version 2026-07-28 by default; `MCP_PROTOCOL_NEGOTIATION=legacy` opts out.

## Why it matters

A home-grown or old stdio server that stalls or fails at connect after the upgrade is likely this change, not your config.

## How to apply

Set `MCP_PROTOCOL_NEGOTIATION=legacy` in the `env` block or shell while diagnosing a slow or failing stdio server. Checked: the variable has 6 hits in the 2.1.296 binary.

> "Changed local (stdio) MCP server connections to negotiate protocol version 2026-07-28 by default on every install, including Bedrock, Vertex and Foundry; `MCP_PROTOCOL_NEGOTIATION=legacy` opts out", Claude Code CHANGELOG 2.1.292
