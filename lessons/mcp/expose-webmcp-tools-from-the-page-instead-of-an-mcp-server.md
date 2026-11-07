---
id: expose-webmcp-tools-from-the-page-instead-of-an-mcp-server
created: 2026-08-29
status: active
supersedes: null
category: mcp
source_type: canonical
tool: codex
sources:
  - https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex
---

# Expose Browser-Side WebMCP Tools From a Client-Side Web App Instead of Standing Up an MCP Server

## TL;DR

For a static or client-side web app, register agent tools in the page via WebMCP rather than building server MCP infrastructure; Codex and ChatGPT in the desktop app's built-in browser call them as site tools.

## Why it matters

Adding a server solely to expose an MCP endpoint adds infrastructure and moves where the data is handled; WebMCP keeps tools where the app state already lives. Note the platform gate: site tools require GPT-5.6 Sol or Terra and the latest desktop app, and are unavailable with GPT-5.6 Luna and in Enterprise/Edu workspaces.

## How to apply

Register browser-side tools on page load per the WebMCP spec (github.com/webmachinelearning/webmcp; Runme's WebMcpToolRegistrationHost is a working reference), then drive the app from Codex in the desktop app's built-in browser on a supported model.

> "WebMCP lets the application expose its capabilities directly from the browser instead.", OpenAI developers blog (Runme write-up)
