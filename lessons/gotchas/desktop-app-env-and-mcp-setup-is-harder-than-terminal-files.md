---
id: desktop-app-env-and-mcp-setup-is-harder-than-terminal-files
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/stop-using-claude-code-in-terminal-it-s-holding-you-back_20260424.txt
---

# Set Up Env Vars and MCP Servers From the Terminal, Not the Desktop App

## TL;DR

Configuring environment variables and MCP servers in the Claude Code desktop app is more cumbersome than editing the plain .env and settings.json files you'd use in the terminal.

## Why it matters

The desktop app's UI adds steps for config that's a one-line file edit in the terminal-based workflow, so initial setup is faster from a terminal even if you plan to work in the desktop app afterward.

## How to apply

Do first-time env var and MCP server configuration in a terminal (edit .env / settings.json directly), then switch to the desktop app for day-to-day chat if you prefer its interface.

## Related

[[desktop-app-ignores-byo-model-env-use-the-cli]]
