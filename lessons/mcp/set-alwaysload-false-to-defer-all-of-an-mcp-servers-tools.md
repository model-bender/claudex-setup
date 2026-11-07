---
id: set-alwaysload-false-to-defer-all-of-an-mcp-servers-tools
created: 2026-10-02
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21287
---

# Defer every tool of an MCP server with `alwaysLoad: false`

## TL;DR

Setting `alwaysLoad: false` on a server entry now puts all its tools behind tool search, so none of its schemas cost context up front.

## Why it matters

It gives per-server control of context cost for a noisy server without removing it. 2.1.285 adds that a tool setting its own `_meta['anthropic/alwaysLoad']` to false stays deferred even when the server is set to `alwaysLoad`.

## How to apply

Add `"alwaysLoad": false` to the server's entry in `.mcp.json` or settings, then check `/context` to see the saving.

Verified: `command grep -c -a 'alwaysLoad' 2.1.287` returned 23. Library grep for `alwaysLoad` found nothing; mcp/stop-pruning-mcp-servers-tool-search-loads-schemas-on-demand covers tool search generally.

> "Changed MCP server `alwaysLoad: false` to defer all of that server's tools behind tool search", Claude Code CHANGELOG 2.1.287
