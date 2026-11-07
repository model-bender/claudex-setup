---
id: test-your-mcp-by-driving-the-other-agents-app-with-computer-use
created: 2026-09-12
status: active
supersedes: null
category: mcp
tool: [codex, claude-code]
sources:
  - transcripts/mark-kashef/gpt-6-astra-s-computer-use-is-ridiculously-good_tU-fO6cADvQ_20260910.txt
---

# Test Your Own MCP Server by Having One Agent Drive the Other Agent's App With Computer Use

## TL;DR

Point Codex's computer use at Claude Desktop or Claude Code, have it install your MCP server, run a real multi-turn session against it, and report back. That is the first-user journey you cannot test from inside your own repo.

## Why it matters

Mark Kashef names the gap this closes: 'if you've ever created or worked on your own MCP, you know that the hardest thing to do is simulate testing, what does it look like for someone to take your MCP server, hook it up to their Claude or Codex, spin it up, and use it for the first time?' Unit tests exercise your handlers, not the install, the tool descriptions, the latency, or whether a model picks the right tool unprompted. His run came back with both usability feedback and a code-level finding about two functions causing latency, from watching the actual tool calls expand in the UI. The same trick verifies that a skill written for one agent behaves in the other.

## How to apply

Prompt with the app, the tab, the task and the verification: 'use computer use to open Claude Desktop, switch to the Claude Code tab, check the <name> MCP is connected, then ask it to <realistic task>, show the actual tool call and check one claim against the source.' Add 'have a few back and forths so we can make sure the user journey is as smooth as possible', since a single turn will not surface routing problems. Expect it to take real time (his ran about 20 minutes) and read the transcript, not just the verdict.

## Related

[[probe-mcp-servers-with-mcp-explorer-before-adopting]], [[point-computer-use-at-a-product-s-docs-to-self-configure-it]], [[run-a-skill-cold-to-verify-it-still-triggers]]
