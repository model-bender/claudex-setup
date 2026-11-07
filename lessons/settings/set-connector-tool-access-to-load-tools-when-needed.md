---
id: set-connector-tool-access-to-load-tools-when-needed
created: 2026-08-29
status: active
supersedes: null
category: settings
tool: claude-code
sources:
  - transcripts/simon-scrapes/19-claude-code-mistakes_icM0ewXGvAw_20260824.txt
---

# Switch connector tool access from auto-load to "load tools when needed"

## TL;DR

With several connectors enabled and tool access on the default auto setting, the full tool definitions for every connector are loaded into context up front on every single message; flip the chat's connector tool-access setting to load tools only when needed and nothing loads until Claude actually uses that tool.

## Why it matters

This is a silent per-message tax: people have measured thousands of tokens per session going to connector tool definitions they never invoked. Unlike MCP servers in the terminal (where tool search now defers schemas by default), the chat surface's auto tool access still front-loads everything, so a decent connector collection quietly degrades context quality and costs real money over time.

## How to apply

In chat, click the plus icon, then connectors, and inside "tool access" select the load-tools-when-needed option instead of having tools already loaded. Verify the saving afterwards: in a session, run /context and check what the connectors/MCP section now costs from the outset.

## Related

[[context-auditing-slash-context]], [[stop-pruning-mcp-servers-tool-search-loads-schemas-on-demand]]
