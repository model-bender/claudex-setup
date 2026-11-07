---
id: override-a-built-in-tool-with-a-function-hook
created: 2026-09-12
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Override a Built-In Tool With a Function Hook So You Can Uninstall Its MCP Server

## TL;DR

Intercept WebSearch in a function hook, send the query to the Exa API when the key is present, and fall back to the built-in tool when the key is missing or the call fails. The model keeps calling WebSearch, the results come from your provider, and the MCP server can be removed.

## Why it matters

Telling Claude to prefer an MCP server does not stop it reaching for the built-in tool, so the routing stays probabilistic. Interception makes it deterministic, and dropping the MCP server takes its tool definitions out of every session's context. The same move routes WebFetch through your own proxy when the built-in fetch keeps getting blocked.

## How to apply

Match the built-in tool in the hook, check for the API key, call your endpoint, return the results into the session on success, and let the original tool run on any failure so the fallback path is never dead.

## Related

[[exa-mcp-plus-per-library-official-mcp-for-training-data-gaps]], [[disable-mcp-server-for-one-project-directory]], [[enable-function-hooks-to-unlock-plugin-authoring]]
