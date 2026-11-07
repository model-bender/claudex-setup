---
id: prefer-the-playwright-cli-over-the-playwright-mcp-to-keep-pages-out-of-context
created: 2026-10-19
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-tried-100-github-repos-for-claude-these-6-are-the-best_HhZdNYI4pJs_20261013.txt
---

# Use Microsoft's Playwright CLI Instead of an MCP to Click Through Your App Without Dumping Pages Into Context

## TL;DR

Nate Herk says the command-line Playwright opens a real browser, clicks like a customer and writes re-runnable tests, and is lighter on tokens than an MCP because it does not put the whole page in Claude's context.

## Why it matters

Claude will say something works without having clicked the buttons. A real-browser run catches that, and per the transcript the CLI form costs fewer tokens and is faster.

## How to apply

Have Claude drive the Playwright CLI to exercise key flows (such as a booking form) and save tests to rerun. Checked: not installed or run here; the token claim is the transcript's and unmeasured.

## Related

[[cli-tools-over-mcp-for-tokens]], [[have-claude-verify-a-responsive-site-with-the-playwright-plugin]]
