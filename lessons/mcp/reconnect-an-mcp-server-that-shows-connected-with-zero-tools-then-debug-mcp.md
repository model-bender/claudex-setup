---
id: reconnect-an-mcp-server-that-shows-connected-with-zero-tools-then-debug-mcp
created: 2026-10-02
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/debug-your-config
---

# When an MCP Server Shows Connected but Lists Zero Tools, Reconnect It From `/mcp`, Then Run `claude --debug=mcp`

## TL;DR

A server that shows connected with zero tools started but is not returning a tool list: select Reconnect in `/mcp`, and if the count stays at zero run `claude --debug=mcp` and read the server's stderr in `~/.claude/debug/<session-id>.txt`.

## Why it matters

The server looks healthy in /mcp, so it is easy to chase config location or key names instead. This is a different failure from a server that never loads, and the docs give a two-step fix plus where the server's own stderr ends up.

## How to apply

In /mcp, select the server and choose Reconnect. If it still lists zero tools, restart with `claude --debug=mcp`, reproduce, and read the server's stderr in the session's debug log under ~/.claude/debug/. For the in-session route see another lesson.

Verified: docs https://code.claude.com/docs/en/debug-your-config.md fetched 2026-10-02: 'A server that shows as connected but lists zero tools has started successfully but isn't returning a tool list. Select **Reconnect** from `/mcp`. If the count stays at zero, run `claude --debug=mcp` and read the server's stderr in the debug log at `~/.claude/debug/<session-id>.txt`.' `claude --help` on 2.1.288 lists `-d, --debug [filter]` with category filtering. Not run live.

## Related

[[put-project-mcp-servers-in-a-root-mcp-json-under-mcpservers]]
