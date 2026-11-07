---
id: codex-chrome-extension-instead-of-service-mcp-servers
created: 2026-09-12
status: active
supersedes: null
category: mcp
tool: codex
sources:
  - transcripts/edmund-yong/i-coded-another-profitable-app-from-scratch-everything-i-did-no-bs-step-by-step_kPVsX6lov_I_20260910.txt
---

# Replace Per-Service MCP Servers With the Codex Chrome Extension

## TL;DR

Rather than running Stripe, Vercel and Supabase MCP servers, let Codex drive those dashboards in your own browser through its Chrome extension, using the credentials you are already logged in with.

## Why it matters

Every installed MCP server spends context on its tool definitions before any work starts, and the creator stripped his loadout to a bare minimum this way because too many skills and servers mean more for the agent to filter before it can begin. The browser route also needs no API keys at all, since it acts as you in an existing session.

## How to apply

Install the Codex Chrome extension, log in to each service once in that browser, then uninstall the corresponding MCP servers. Keep MCP for anything that needs to run headless or unattended, because the browser path assumes a live session.

## Related

[[puppeteer-mcp-replaceable-by-claude-in-chrome]], [[disable-mcp-server-for-one-project-directory]], [[be-a-context-minimalist-provision-a-lean-harness]]
