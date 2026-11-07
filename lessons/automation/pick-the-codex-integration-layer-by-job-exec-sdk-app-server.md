---
id: pick-the-codex-integration-layer-by-job-exec-sdk-app-server
created: 2026-08-29
status: active
supersedes: null
category: automation
source_type: canonical
tool: codex
sources:
  - https://developers.openai.com/blog/codex-as-a-platform
---

# Pick the Codex Integration Layer by Job: codex exec for CI, the SDK for Code, App-Server for Products

## TL;DR

Codex documents a three-layer integration ladder: `codex exec` for bounded non-interactive runs with structured output, the Codex SDK to start, resume, and stream tasks from application code, and app-server when the agent lifecycle is part of the product itself.

## Why it matters

Choosing too heavy a layer (embedding app-server for what a `codex exec` call does) or too light (shelling out where you need streamed events and approval handling) is a common integration mistake; the post states the routing rule explicitly, including "Use Codex app-server when the agent is part of the product itself."

## How to apply

Route one-off and CI work through `codex exec` (non-interactive, structured output), programmatic start/resume/stream through the official Codex SDK, and persistent conversations with event streams, interrupts, and approval requests through app-server.

> "For a script, CI job, or one-off background task, codex exec can run a bounded agent workflow and return structured output.", OpenAI developers blog

## Related

[[codex-mcp-server-is-removed-not-just-deprecated]], [[build-internal-tools-on-the-agent-sdk-with-your-cached-cli-login]]
