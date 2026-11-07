---
id: probe-mcp-servers-with-mcp-explorer-before-adopting
created: 2026-08-31
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - https://simonw.substack.com/p/stateless-mcp-has-recaptured-my-interest
---

# Probe an MCP Server's Tool Surface From the Terminal With mcp-explorer Before Adopting It

## TL;DR

Before wiring a new MCP server into an agent, run `uvx mcp-explorer list <url>`, `uvx mcp-explorer inspect <tool>`, and `uvx mcp-explorer call <url> <tool> -a <name> <value>` from the terminal to enumerate and exercise its tools first.

## Why it matters

An MCP server's whole advantage for risk reasoning is that its tool list is enumerable, but that only helps if you actually read the list before the agent does. A quick terminal probe shows exactly which tools exist, what each accepts, and what a real call returns, so you adopt the server knowing its blast radius instead of discovering it mid-session.

## How to apply

Run `uvx mcp-explorer list <url>` to enumerate the server's tools, `uvx mcp-explorer inspect <tool>` to read a specific tool's definition, and `uvx mcp-explorer call <url> <tool> -a <name> <value>` to exercise a call with real arguments. Do this before adding the server to any agent configuration, especially when the server will touch sensitive data.

## Related

[[narrow-mcp-tool-surface-over-shell-for-sensitive-work]]
