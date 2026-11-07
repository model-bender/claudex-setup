---
id: add-bareelicitationcapability-when-an-mcp-server-stops-connecting
created: 2026-10-02
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21287
---

# Add `"bareElicitationCapability": true` when an MCP server stops connecting after 2.1.287

## TL;DR

A server that broke on upgrade has a one-key fix in its MCP config entry.

## Why it matters

The update advertises URL elicitation, and some servers reject the new capability shape and fail to connect. Without knowing the key you would remove the server.

## How to apply

Add `"bareElicitationCapability": true` to that server's entry. 2.1.284 also adds `/mcp reconnect all` to retry every failed or unauthenticated server at once.

Verified: `command grep -c -a 'bareElicitationCapability' 2.1.287` returned 5 and `command grep -c -a 'mcp reconnect' 2.1.287` returned 13. Library grep found neither.

> "Added URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in. If a server no longer connects after this update, add "bareElicitationCapability": true to its MCP config entry", Claude Code CHANGELOG 2.1.287

## Related

[[run-mcp-reconnect-all-to-retry-every-failed-mcp-server]]
