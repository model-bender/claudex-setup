---
id: set-enable-tool-search-true-behind-a-gateway-that-forwards-tool-reference
created: 2026-10-20
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/mcp#configure-tool-search
  - https://code.claude.com/docs/en/prompt-caching#connecting-or-removing-an-mcp-server
  - https://github.com/anthropics/claude-code/issues/102518
---

# Behind a Custom ANTHROPIC_BASE_URL Tool Search Is Off: Set ENABLE_TOOL_SEARCH=true if Your Gateway Forwards tool_reference Blocks

## TL;DR

Claude Code turns MCP tool search off when `ANTHROPIC_BASE_URL` points at a non-first-party host, so every MCP tool schema loads upfront and adding a tool definition mid-session invalidates the prompt cache; `ENABLE_TOOL_SEARCH=true` keeps MCP tools deferred on that host (the model and deployment fallbacks still apply).

## Why it matters

The advice that extra MCP servers are nearly free ([[stop-pruning-mcp-servers-tool-search-loads-schemas-on-demand]]) assumes tool search is on. Behind an `ANTHROPIC_BASE_URL` gateway on a non-first-party host it is off by default, so every server's full schemas cost context on every request, and a server connecting, a tool update that adds tools, or a tool you remove on purpose mid-session invalidates the whole cache. Issue #102518 names `ENABLE_TOOL_SEARCH=true` as the documented switch for this gateway case.

## How to apply

If your gateway forwards the `anthropic-beta` header, `defer_loading` tool fields and `tool_reference` blocks, and its upstream accepts them, set `ENABLE_TOOL_SEARCH=true` in the settings `env` block. Requests fail on proxies that don't support `tool_reference` blocks, so if they start failing, remove it. `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` keeps tool search off whatever `ENABLE_TOOL_SEARCH` says; only an organization's managed settings (v2.1.227 or later) can keep it on under that variable. Checked on 2026-10-20 against the live MCP and prompt-caching docs and the 2.1.304 binary (`ENABLE_TOOL_SEARCH`: 13 hits, `tool_reference`: 20).

> "Claude Code disables it when `ANTHROPIC_BASE_URL` points to a non-first-party host, since most proxies don't forward `tool_reference` blocks.", Claude Code docs (MCP, "Configure tool search")

## Related

- [[mcp-tool-search-threshold-env-setting]]
- [[a-gateway-that-strips-cache-control-bills-every-turn-uncached]]
