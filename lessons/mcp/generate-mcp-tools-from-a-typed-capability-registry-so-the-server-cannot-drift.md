---
id: generate-mcp-tools-from-a-typed-capability-registry-so-the-server-cannot-drift
created: 2026-10-19
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1x60bmf/i_built_an_mcp_server_with_claude_code_that_lets/
---

# Generate MCP Tools From the App's Own Typed Capability Registry So the Server Cannot Drift

## TL;DR

When you have Claude Code build an MCP server for your own app, have it first build one typed registry of everything a user can do, generate every MCP tool from that registry, and make leaving a capability out of the MCP a compile error unless the code states why.

## Why it matters

A hand-maintained MCP server quietly falls behind the product: each new feature in the app is one more tool nobody remembered to add, and agents using the server just never see it. Deriving tools from the registry makes coverage automatic, and the required exclusion reason turns a silent gap into a build failure.

## How to apply

Ask Claude Code for the typed capability registry before any tool code, have the tool definitions generated from it, and add an exclusion field (with a required reason) that the type checker enforces. The poster built it one PR per capability, each with integration tests against a real database. The source is a product launch post; the pattern stands apart from the product.

> "Each MCP tool is generated from that registry, so a feature added to the web app shows up in the MCP. If a capability is deliberately kept out of the MCP, the code has to state why or it doesn’t compile.", u/Cojj25 on r/ClaudeAI

## Related

[[expose-webmcp-tools-from-the-page-instead-of-an-mcp-server]]
