---
id: claude-bare-now-skips-config-mcp-servers-and-system-reminders
created: 2026-10-02
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21286
---

# Treat `claude --bare` as truly bare now: named MCP servers only, no system reminders, no background tasks

## TL;DR

`--bare` runs now drop config-file MCP servers, system reminders and background tasks, and timed-out shell commands are killed instead of backgrounded.

## Why it matters

Scripts that relied on `--bare` still loading MCP servers from config, or on a long command continuing in the background, now behave differently.

## How to apply

Pass every needed server explicitly with `--mcp-config`, and give long shell steps a larger timeout instead of expecting them to background.

Verified: `claude --help` on 2.1.287 shows `--bare` ("Minimal mode: skip hooks ..."). Library grep for `--bare` found nothing active.

> "Changed `--bare` to connect only the MCP servers named on the command line, send the model no system reminders, and start no background tasks; under `--bare`, a shell command that reaches its timeout now stops instead of moving to the background", Claude Code CHANGELOG 2.1.286
