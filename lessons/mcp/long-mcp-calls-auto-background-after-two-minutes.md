---
id: long-mcp-calls-auto-background-after-two-minutes
created: 2026-07-25
status: active
supersedes: null
category: mcp
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Long MCP Calls Auto-Background After 2 Minutes: Tune `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`

## TL;DR

An MCP tool call that runs past two minutes is detached to the background rather than blocking the session, which keeps you working but means the result arrives out of band instead of in the turn that asked for it.

## Why it matters

Slow MCP servers, scrapers, cloud builds, DB migrations, used to freeze the session outright, so this is a real improvement. But a workflow that assumed the tool result lands inline now has a handoff in it, and a chained step that consumes that result may run before it exists.

## How to apply

Set `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` in the settings `env` block: raise the threshold for MCP servers whose results you need inline, lower it for ones you always want detached. Leave it at the default unless a specific server's timing bites you.

> "MCP tool calls running longer than 2 minutes now move to the background automatically so the session stays usable; configure the threshold or disable with `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`", Claude Code CHANGELOG 2.1.212

## Related

[[set-background-false-on-forked-skills-you-need-inline]]
