---
id: swap-mcp-connectors-for-api-keys-before-deploying-an-app
created: 2026-10-02
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/jono-catliff/full-claude-code-masterclass-beginner-to-expert-in-2-hours-2026_R3mx8XHX8ns_20261002.txt
---

# Swap MCP connectors for API keys before you deploy an app Claude built

## TL;DR

MCP connectors work inside Claude Code only. A deployed site or app cannot use them, so its integrations need API keys.

## Why it matters

Jono Catliff built a personal dashboard using Gmail, Google Calendar and ClickUp connectors, kept it on localhost, and warns that pushing it live means replacing each connector with an API key, which Claude can walk you through.

## How to apply

Before deploying, list every connector the app relies on and ask Claude to replace each with the vendor's API and a key stored as a host environment variable.

Verified: Claude Code 2.1.287 was not run for this. The claim that a deployed site cannot use Claude connectors is the creator's, and follows from connectors being attached to Claude sessions; treat the mechanism as the lesson's inference.

