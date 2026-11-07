---
id: stop-pruning-mcp-servers-tool-search-loads-schemas-on-demand
created: 2026-08-29
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/simon-scrapes/19-claude-code-mistakes_icM0ewXGvAw_20260824.txt
---

# Stop pruning rarely-used MCP servers: tool search loads schemas on demand now

## TL;DR

The long-standing advice to remove infrequently used MCP servers because every schema loaded into every session is out of date: tool search is on by default, so only the tool names load (~120 tokens per server) and full schemas are pulled in on demand, making extra MCP servers nearly free context-wise; verify with /context and /mcp.

## Why it matters

This flips a rule most practitioners still follow and that this corpus itself taught. The old cost model (all MCP schemas up front, prune aggressively, tune a tool-search threshold) no longer describes current behavior, so people are still deleting genuinely useful servers to save tokens they'd no longer spend. The correct residual concerns about MCP servers are security surface and tool-choice confusion, not context cost.

## How to apply

Keep the MCP servers you find useful installed. Run /context to see exactly what your MCP servers cost in tokens; the display marks servers whose tools are loaded on demand, costing nothing at session start (check /mcp for the list). Make pruning decisions on security and tool-routing grounds (read-only keys, overlapping tools), not token-cost grounds.

## Related

[[context-auditing-slash-context]], [[cli-tools-over-mcp-for-tokens]], [[narrow-mcp-tool-surface-over-shell-for-sensitive-work]], [[set-connector-tool-access-to-load-tools-when-needed]]
