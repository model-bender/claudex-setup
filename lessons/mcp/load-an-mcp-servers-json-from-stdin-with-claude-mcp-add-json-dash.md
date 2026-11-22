---
id: load-an-mcp-servers-json-from-stdin-with-claude-mcp-add-json-dash
created: 2026-11-22
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21327
---

# Load an MCP server's JSON from stdin with `claude mcp add-json <name> -` to keep tokens out of shell history

## TL;DR

`claude mcp add-json <name> -` reads the server config from stdin instead of an argument.

## Why it matters

A JSON string with a bearer token passed as an argument lands in shell history and the process list.

## How to apply

Pipe the JSON from a file or secret manager into `claude mcp add-json <name> -` in a normal shell, not inside a Claude Code session.

Checked: `claude mcp add-json --help` on 2.1.330 prints: 'Add an MCP server ... with a JSON string, or - to read it from stdin'

> "Added `claude mcp add-json <name> -` to read the server's JSON from stdin, so tokens can stay off the command line; not available inside a Claude Code session", Claude Code CHANGELOG 2.1.327
