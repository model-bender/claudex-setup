---
id: puppeteer-mcp-replaceable-by-claude-in-chrome
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-connected-claude-code-to-your-browser_20260307.txt
---

# Replace a Puppeteer MCP Server With Claude in Chrome

## TL;DR

If you're using a Puppeteer MCP server for browser automation, consider replacing it with Claude in Chrome now that it's tightly integrated with Claude Code.

## Why it matters

Claude in Chrome gives Claude Code direct control of tabs, console logs, and page state in one coupled system, which the presenter reports performing better than a separate Puppeteer MCP layer for the same scraping/automation tasks.

## How to apply

For a task currently wired through a Puppeteer MCP server, try running it instead through /chrome-driven Claude in Chrome control and compare reliability before keeping the MCP server around.

## Related

[[chrome-extension-for-browser-testing]], [[narrow-mcp-tool-surface-over-shell-for-sensitive-work]]
