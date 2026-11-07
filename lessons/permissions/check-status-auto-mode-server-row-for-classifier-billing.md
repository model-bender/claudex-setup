---
id: check-status-auto-mode-server-row-for-classifier-billing
created: 2026-09-24
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/auto-mode-classifier-billing
---

# Check /status's "Auto mode server" Row to See If Your Classifier Billing Is Free

## TL;DR

Since 2.1.278, auto mode's safety classifier runs free on Anthropic's server by default for API/Enterprise/Bedrock/Vertex/Foundry/gateway users; when a gateway strips headers or the platform hasn't rolled it out, Claude Code silently falls back to billed local classifier requests, and /status is the only way to tell which one you're on.

## Why it matters

The fallback is invisible unless you look: it holds the first affected action, shows a one-time notice you can dismiss with Enter, and then bills every classifier check as normal token usage for the rest of that session with no further indication. Pro, Max and Team plans never see this (always free); API/Enterprise/Bedrock/Vertex/Foundry/gateway users are the ones who should check.

## How to apply

Run /status and read the "Auto mode server" row (Enabled = free server-side checks, Disabled = billed local classifier). To force local billing everywhere and suppress the notice, set CLAUDE_CODE_AUTO_MODE_SERVER=0; per the 2.1.281 changelog this variable now also applies on a direct Anthropic API connection ("0 opts out of the server-side auto mode classifier (the local classifier then counts toward usage), 1 opts in"), extending past its original Bedrock/Vertex/Foundry/gateway-only scope from 2.1.278. Checked: `CLAUDE_CODE_AUTO_MODE_SERVER` string present in the installed 2.1.281 binary (command grep -c -a: 7 hits), including the exact billing sentence from the docs page embedded in a spinner/notice string.

> "its Auto mode server row reads Enabled while the server's checks decide the session's actions and Disabled once the session has fallen back", Claude Code docs (auto-mode-classifier-billing)
