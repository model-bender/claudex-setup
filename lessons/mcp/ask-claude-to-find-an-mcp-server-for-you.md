---
id: ask-claude-to-find-an-mcp-server-for-you
created: 2026-09-01
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/john-kim/how-i-use-claude-code-meta-staff-engineer-tips_20260307.txt
---

# Ask Claude to Find You an MCP Server Instead of Web Searching Yourself

## TL;DR

You can just say 'find me a good Figma MCP' and Claude will search and usually get it right, saving you the manual lookup.

Once Claude identifies an MCP you want, ask it to install it directly rather than editing MCP config files yourself.

## Why it matters

John Kim uses this as a routine hack, but flags the gotcha: Claude sometimes surfaces an MCP that was popular a while ago rather than doing a fresh web search, so it can be outdated.

John Kim contrasts this with the older Cursor-era workflow where you had to manage MCP configs manually; Claude Code can just do the installation for you.

## How to apply

Ask Claude directly to find an MCP for a given purpose; watch its thinking/tool calls and cancel or redirect if it looks like it's recalling a stale answer instead of actually searching.

After Claude surfaces or you name an MCP server, say 'go ahead and install this for me' instead of hand-editing `.mcp.json` or similar config.

## Related

[[authenticate-mcp-servers-from-the-cli]]
