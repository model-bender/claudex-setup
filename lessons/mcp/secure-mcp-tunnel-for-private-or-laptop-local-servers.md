---
id: secure-mcp-tunnel-for-private-or-laptop-local-servers
created: 2026-07-25
status: active
supersedes: null
category: mcp
source_type: post
tool: codex
sources:
  - https://developers.openai.com/blog/connect-private-mcp-servers-to-openai-products
---

# Reach a Private or Laptop-Local MCP Server With Secure MCP Tunnel Instead of Exposing a Public Endpoint

## TL;DR

Secure MCP Tunnel inverts the connection direction, a customer-run open-source client sitting next to the MCP server dials out over HTTPS, so ChatGPT and Codex get a normal MCP request path without the server ever accepting inbound traffic.

## Why it matters

The usual three options are all worse for a narrow integration: a public endpoint weakens the boundary, a third-party tunnel adds a vendor to your security review and procurement, and a VPN or peering link "solve reachability by creating broad network connectivity, which is often too much machinery for a narrow MCP integration." It also covers the everyday case of wiring up an MCP server running on your own laptop.

## How to apply

Run the tunnel client alongside the private MCP server with explicit destination configuration; it long-polls the OpenAI-hosted tunnel endpoint over outbound HTTPS, which enterprise firewalls and proxies already permit, and relays streamed SSE results back. Access binds to your existing OpenAI org/workspace context rather than becoming a separate network path with its own access model.

> "Customers run a small client inside their private environment that establishes an outbound HTTPS connection to OpenAI. The client: Receives MCP requests, Forwards them to an approved local server, Returns responses and notifications through the same connection.", Denys Kurylenko, OpenAI

