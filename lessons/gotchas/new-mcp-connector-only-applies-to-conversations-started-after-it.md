---
id: new-mcp-connector-only-applies-to-conversations-started-after-it
created: 2026-09-12
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/jono-catliff/claude-code-seo-audit-fix-your-whole-website-in-1-prompt-steal-this_M2KJ5-sFbbg_20260910.txt
---

# A Newly Added MCP Connector Only Reaches Conversations Started After It, Re-Paste Your Prompt Into a Fresh One

## TL;DR

Adding an MCP connector while a conversation is already open does nothing for that conversation. Copy your prompt, open a new chat or session, and run it there.

## Why it matters

Jono Catliff hits this mid-build: he wires the Semrush connector in settings, then explicitly stops to move his prompt into a new conversation because 'anytime we add a new MCP connector, it only works on new conversations moving forward'. The failure is silent, the connector's tools simply are not offered, so the agent works around the gap with whatever it already has and you get a plausible answer built on missing data instead of an error.

## How to apply

Wire the connector first, before you start the task. If you added it mid-task, copy the prompt out, open a new conversation or restart the session, and confirm the connector's tools are listed before you rely on them. Same shape as the CLAUDE.md and Codex MCP restart gotchas: configuration changes are read at session start.

## Related

[[claude-md-edits-are-invisible-until-restart-clear-or-compact]], [[set-connector-tool-access-to-load-tools-when-needed]]
