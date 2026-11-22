---
id: add-a-connector-in-claude-ai-to-use-it-in-claude-code
created: 2026-11-22
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/jono-catliff/claude-code-local-seo-agent-automate-everything-500k-earned_vwzV-YsVswA_20261007.txt
  - transcripts/jono-catliff/full-claude-code-masterclass-beginner-to-expert-in-2-hours-2026_R3mx8XHX8ns_20261002.txt
---

# Add a data connector in claude.ai settings and Claude Code can use it too

## TL;DR

Enable a connector such as Semrush under Settings, Connectors on claude.ai and it becomes available to Claude Code, so commands can pull real data from it.

## Why it matters

The creator's commands depend on Semrush for real search volume so that pages and profile services are chosen from what people actually search for, not guessed. Connecting it once on claude.ai is the creator's only setup step for that data.

## How to apply

On claude.ai open Settings, then Connectors, search for the service (Semrush in the video) and install it. Then run the commands in Claude Code signed in with the same account. From the docs: connectors load only when Claude Code's active login is a claude.ai subscription, not when an API key, `apiKeyHelper` or a third-party provider is active, and `/mcp` lists them marked as coming from claude.ai, so check there before relying on one.

Checked: Claude Code docs code.claude.com/docs/en/mcp.md, section 'Use MCP servers from claude.ai' (fetched 2026-11-22): connectors added at claude.ai/customize/connectors are automatically available in Claude Code when logged in with a claude.ai account, and Terminal and VS Code sessions fetch them. Semrush's developer docs (developer.semrush.com/api/basics/semrush-mcp/) list Claude and Claude Code setup for the Semrush MCP. 'Samrush' and 'Seamrush' in the transcript are Semrush.

## Related

[[opt-out-of-claude-ai-skill-and-plugin-sync]]
