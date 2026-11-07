---
id: mobin-design-inspiration-mcp-in-claude-design
created: 2026-08-07
status: active
supersedes: null
category: mcp
tool: claude-design
sources:
  - transcripts/sean-kochel/i-fed-claude-code-600-000-designs-here-s-what-happened_LnNmQ_bzahQ_20260807.txt
---

# Wire the Mobin Design-Reference MCP Into Claude Design via a Claude Desktop Connector

## TL;DR

Mobin's MCP server (500k+ real app screens) has no "add MCP" path inside the Claude Design web UI. Connect it in Claude Desktop instead (Settings > Connectors > Browse > Mobin) and it becomes usable from Claude Design projects, so you can ask for specific named screens, elements, or whole flows as generation input.

## Why it matters

Without a live reference source, Claude Design invents generic UI from scratch. Querying named real-app references gives it concrete structure and interaction patterns to work from, not just a palette. This is a different workflow from manually screenshotting a reference into Claude Code with a colour-only constraint: the references are queried on demand, by name, from inside the design tool.

## How to apply

1. Get a Mobin paid plan (roughly $45/month and up) and enable its MCP server in Mobin's settings.
2. In Claude Desktop, go to Settings > Connectors > Add Connector > Browse, search "mobin", and connect. This makes it available inside Claude Design too, since Design has no separate MCP-add UI.
3. Use its three tools: search screens, search UI elements and sections, search flows.
4. Prompt with a named target, for example "use the Mobin MCP to pull Whisperflow's onboarding flow", "pull a highly rated time-picker component", or "pull distinct UI directions for this category". Combine the result with your own chosen direction and feature list.

## Related

[[reference-real-products-and-state-negatives-instead-of-adjectives]], [[split-brand-and-structure-sources-in-one-design-prompt]], [[feed-claude-design-a-reference-gallery-url-or-its-prompt]]
