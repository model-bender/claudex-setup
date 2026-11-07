---
id: run-mcp-reconnect-all-to-retry-every-failed-mcp-server
created: 2026-10-02
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21287
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21284
---

# Run `/mcp reconnect all` to Retry Every Failed or Unauthenticated MCP Server at Once

## TL;DR

Since 2.1.284, `/mcp reconnect all` in the interactive terminal retries every MCP server that failed to connect or needs authentication in one command, instead of reconnecting them one by one from `/mcp`.

## Why it matters

Several servers can drop together (after an upgrade, a network change or expired tokens), and reconnecting each one from /mcp is slow. The command shipped in 2.1.284 but sat only in the bareElicitationCapability lesson's body, where no title or TL;DR surfaced it.

## How to apply

When /mcp lists several failed or needs-auth servers, run `/mcp reconnect all` in the interactive terminal. If one still fails right after a 2.1.287+ upgrade, add "bareElicitationCapability": true to its entry (see [[add-bareelicitationcapability-when-an-mcp-server-stops-connecting]]).

Verified: Claude Code CHANGELOG 2.1.284: 'Added `/mcp reconnect all` in the interactive terminal to retry every MCP server that failed to connect or needs authentication at once'; `command grep -c -a 'reconnect all'` on the installed 2.1.288 binary returned 6. Not run live.

## Related

[[add-bareelicitationcapability-when-an-mcp-server-stops-connecting]]
