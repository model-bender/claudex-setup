---
id: narrow-mcp-tool-surface-over-shell-for-sensitive-work
created: 2026-08-16
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: post
sources:
  - https://simonw.substack.com/p/stateless-mcp-has-recaptured-my-interest
---

# Prefer a Narrow MCP Tool Surface Over Shell Access When the Agent Touches Sensitive Data

## TL;DR

For agent work on sensitive data or in an open network environment, hand the agent a fixed MCP tool list rather than a shell - an enumerable tool surface is auditable in a way arbitrary commands are not.

## Why it matters

The corpus already argues MCP-vs-CLI on **token cost**, where the CLI wins decisively. This is the other axis - **blast radius** - and it flips the choice for sensitive builds. You can read a tool list and reason about what could go wrong; you cannot do that for "the agent has Bash."

Neither lesson supersedes the other. Reach for a CLI when you control the integration and cost is the constraint; reach for a narrow MCP surface when the question is what happens if the agent is wrong or manipulated. A useful side effect: the narrower surface is simple enough that small local models still drive it correctly.

## How to apply

Expose the capability as a stateless HTTP MCP server - one HTTP request per call, `MCP-Protocol-Version: 2026-07-28` - instead of granting Bash. Probe it from the terminal before adopting it:

```
uvx mcp-explorer list <url>
uvx mcp-explorer inspect <tool>
uvx mcp-explorer call <url> <tool> -a <name> <value>
```

> "Something I've come to appreciate about MCP is that it's much easier to reason about agent capabilities and what might go wrong than with arbitrary command execution in an open network environment.", Simon Willison

## Related

[[cli-tools-over-mcp-for-tokens]], [[scope-tool-access-not-just-the-prompt-to-restrict-agent-actions]], [[probe-mcp-servers-with-mcp-explorer-before-adopting]]
