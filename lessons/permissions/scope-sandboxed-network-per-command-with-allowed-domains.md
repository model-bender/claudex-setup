---
id: scope-sandboxed-network-per-command-with-allowed-domains
created: 2026-09-24
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Scope Auto-Mode Sandbox Network Access Per-Command With allowed_domains

## TL;DR

Bash, PowerShell, and Monitor tool calls in sandboxed auto mode can now carry a per-command allowed_domains list, reviewed alongside the command itself, so network access is scoped to exactly the hosts that one command needs rather than a session-wide allowlist.

## Why it matters

Without this, sandboxed network access in auto mode tends toward either "block everything" (breaking legitimate calls) or a broad allowlist that stays open for the rest of the session; per-command scoping means a command that legitimately needs api.example.com gets exactly that host, once, instead of widening what every later command can reach.

## How to apply

When a sandboxed Bash/PowerShell/Monitor command needs network access in auto mode, expect (or explicitly request) allowed_domains scoped to that call; per the 2.1.281 changelog's related fix, if such a command is later forced to run outside the sandbox, it now refuses to run rather than silently losing that enforcement ("This command was approved with allowed_domains but would now run outside the sandbox, which cannot enforce them; it was not run"). Checked: `allowed_domains` confirmed present in the installed 2.1.281 binary as a real schema field name and in permission-prompt/error text (command grep -a -o, including the exact "would now run outside the sandbox" refusal string quoted above).

> "Added per-command `allowed_domains` to Bash, PowerShell and Monitor in auto mode with sandboxing: the hosts a command needs are reviewed with it and opened for it alone; other hosts are refused", Claude Code CHANGELOG 2.1.271
