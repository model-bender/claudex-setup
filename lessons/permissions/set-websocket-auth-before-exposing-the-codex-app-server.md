---
id: set-websocket-auth-before-exposing-the-codex-app-server
created: 2026-08-07
status: active
supersedes: null
category: permissions
tool: codex
source_type: canonical
sources:
  - https://learn.chatgpt.com/docs/app-server
---

# Configure WebSocket Auth Before Exposing Codex's app-server Remotely

## TL;DR

Codex's app-server can connect to a remote Code Mode host over WebSocket, but non-loopback WebSocket listeners currently accept unauthenticated connections by default during rollout. Turn auth on yourself before exposing one.

## Why it matters

The docs state the gap outright, which makes it a known insecure default rather than a bug: anyone wiring app-server to a second machine or a shared team host is exposed until they act. Defaults that are safe on loopback and unsafe off it are especially easy to get wrong, because the local setup you tested works fine.

## How to apply

Pass `--ws-auth capability-token` with `--ws-token-file /absolute/path`, preferring the token file over a raw bearer token on the command line. Clients then send `Authorization: Bearer <token>` at the WebSocket handshake. Use `wss://` for any remote host and reserve `ws://` for localhost or an SSH-forwarded tunnel.

> "Non-loopback WebSocket listeners currently allow unauthenticated connections by default during rollout, so configure WebSocket auth before exposing one remotely.", OpenAI Codex docs, app-server

## Related

[[secure-mcp-tunnel-for-private-or-laptop-local-servers]], [[codex-projects-are-a-working-directory-not-a-boundary]]
