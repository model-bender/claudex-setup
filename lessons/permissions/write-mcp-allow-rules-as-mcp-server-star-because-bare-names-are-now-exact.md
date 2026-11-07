---
id: write-mcp-allow-rules-as-mcp-server-star-because-bare-names-are-now-exact
created: 2026-10-19
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21299
---

# Write MCP Allow Rules and Agent tools: Entries as mcp__<server>__*, Because a Bare mcp__<server> No Longer Covers Similar Names

## TL;DR

Since 2.1.299 `mcp__a` allows only the server named `a`, not `a__b` or `a_`, so a rule that leaned on prefix matching may silently stop covering the server you meant.

## Why it matters

Prefix rules used to leak permission to similarly named servers. After the change the leak is closed, but a server whose normalized name contains `__` is only reached by its whole name, in both allow rules and agent `tools:` lists.

## How to apply

Audit `permissions.allow` and subagent `tools:` lists for MCP entries and write each as `mcp__<whole normalized name>__*`. Checked: rule syntax only, no new setting name.

> "Changed MCP allow rules to reach only the server they name: `mcp__a` no longer allows a server named `a__b` or `a_`; write `mcp__<server>__*` with the server's whole normalized name", Claude Code CHANGELOG 2.1.299

## Related

[[hook-matchers-exact-match-not-substring]]
