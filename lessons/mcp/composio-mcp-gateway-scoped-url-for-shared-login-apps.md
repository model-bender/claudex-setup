---
id: composio-mcp-gateway-scoped-url-for-shared-login-apps
created: 2026-08-07
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/simon-scrapes/this-setup-gives-your-team-the-same-claude-memory-steal-it_PzaC81yCJg0_20260807.txt
---

# Use Composio's MCP Gateway to Scope Team Access to a Shared-Login App

## TL;DR

For an app with one shared team login and no per-user accounts (a company LinkedIn, an affiliate dashboard), Composio's MCP Gateway API mints a single scoped MCP URL exposing only the tools and permissions you pick. Add it to Claude as a custom connector and the team gets joint access without ever seeing the credential.

## Why it matters

Wiring scheduled tasks through Composio covers OAuth and multiple accounts of one service, but not this case: apps with no per-user auth at all. There, the alternatives are sharing the raw login, which breaks when someone leaves because every place it was pasted needs rotating, or leaving the app inaccessible to the team entirely.

## How to apply

1. Call Composio's API to create a scoped MCP server for one connected account and tool combination (for example "just QuickBooks with these permissions"). The response is an MCP URL.
2. In Claude, choose "Add custom connector", paste the MCP URL, and name it.
3. Anyone with that connector gets exactly the scoped access. Revoking or rotating happens once in Composio, not everywhere the shared login was pasted.

As of this recording there is no dashboard UI for step 1: it is an API call only.

## Related

[[wire-cloud-scheduled-tasks-through-connectors-not-local-files-or-keys]], [[harden-always-on-agents-least-privilege-and-capable-models]], [[secure-mcp-tunnel-for-private-or-laptop-local-servers]]
