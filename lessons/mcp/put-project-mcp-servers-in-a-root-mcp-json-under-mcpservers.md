---
id: put-project-mcp-servers-in-a-root-mcp-json-under-mcpservers
created: 2026-10-02
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/debug-your-config
---

# Put project MCP servers in a root `.mcp.json` under `mcpServers`, with absolute script paths

## TL;DR

Servers silently never load if `.mcp.json` sits in `.claude/`, uses a VS Code style top-level `servers` key, or is declared under `mcpServers` in `settings.json`; relative `command`/`args` paths resolve against the launch directory.

## Why it matters

These are silent failures with no error, and the fix is a location or key change. A server that shows connected with zero tools needs Reconnect in `/mcp`, then `claude --debug=mcp`.

## How to apply

Use `/mcp` to check status and approve project servers, use absolute paths for local scripts (or `CLAUDE_PROJECT_DIR`), and add user-scoped servers with `claude mcp add --scope user`.

Verified: Read live docs debug-your-config.md and mcp.md (CLAUDE_PROJECT_DIR passed to servers). `command grep -c -a -F CLAUDE_PROJECT_DIR` on 2.1.287 = 33. Library has only a-project-mcp-json-headershelper-now-needs-folder-trust-and; no lesson on location, key name or relative paths.

> "Project MCP config goes at the repository root as `.mcp.json`, not inside `.claude/`, with servers under the `mcpServers` key.", Claude Code docs (debug your configuration)

## Related

[[reconnect-an-mcp-server-that-shows-connected-with-zero-tools-then-debug-mcp]]
