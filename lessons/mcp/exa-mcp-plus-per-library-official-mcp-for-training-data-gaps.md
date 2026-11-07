---
id: exa-mcp-plus-per-library-official-mcp-for-training-data-gaps
created: 2026-09-01
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Enable Exa MCP Globally, and Install Official Per-Library MCP Servers for Heavily-Used New Libraries

## TL;DR

Keep the Exa MCP server enabled across all projects so Claude Code can search online for docs on niche or very recent libraries, and additionally install a library's own official MCP server (e.g. trigger.dev's) when you use that library heavily.

## Why it matters

Libraries you want to use that are recent or niche often lack enough training data for the agent to use correctly from memory; live search and library-specific MCP tools (like a search-docs tool) close that gap, including for debugging.

## How to apply

Enable the Exa MCP server project-wide as a default fallback for finding documentation on unfamiliar packages. For any library you use heavily and that changes often (e.g. trigger.dev), install its dedicated official MCP server so tools like search-docs are available directly in /mcp.

## Related

[[context-7-mcp-for-up-to-date-docs]]
