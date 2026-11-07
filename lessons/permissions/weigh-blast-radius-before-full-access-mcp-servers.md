---
id: weigh-blast-radius-before-full-access-mcp-servers
created: 2026-09-01
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/andrew-codesmith/900-hours-of-learning-claude-code-cursor-in-10-minutes_20260307.txt
---

# Weigh the Blast Radius Before Granting an MCP Server Full Database Access

## TL;DR

A convenient MCP server like Supabase's gives Claude broad access to your project, including the theoretical ability to delete or corrupt your entire database schema, so the productivity gain has to be weighed against that risk.

## Why it matters

MCP servers are marketed as a plug-and-play data connector, but connect to real data often means grant broad write and delete permission, not a scoped read-only view.

## How to apply

Before adopting a powerful data-access MCP, check what operations it exposes (read vs write vs delete/schema changes) and decide if a narrower-scoped credential or read-only mode is available before wiring it into a live project.

## Related

[[narrow-mcp-tool-surface-over-shell-for-sensitive-work]], [[keep-credentials-out-of-the-agent-sandbox]]
