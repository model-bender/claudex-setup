---
id: disable-mcp-server-for-one-project-directory
created: 2026-09-01
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/john-kim/how-i-use-claude-code-meta-staff-engineer-tips_20260307.txt
---

# Disable a Bloated MCP Server for Just One Project, Not Globally

## TL;DR

If `/context` shows an MCP server eating a large share of your tokens, you can disable it for that specific directory instead of removing it everywhere.

## Why it matters

John Kim only installs MCPs he actually needs per project (e.g., an Xcode MCP for an iOS app but not for a Next.js project) precisely because MCPs are 'known to blow up your token usage and your context window.'

## How to apply

Run `/context` to see per-MCP token cost, then scope the MCP off for directories where it isn't needed rather than uninstalling it for every project.

## Related

[[stop-pruning-mcp-servers-tool-search-loads-schemas-on-demand]], [[scope-skills-per-project-not-globally-to-cut-startup-context]]
