---
id: share-a-local-internal-tool-over-a-mesh-vpn-instead-of-deploying-it
created: 2026-09-12
status: active
supersedes: null
category: remote-access
tool: [codex, claude-code]
sources:
  - transcripts/mark-kashef/this-ai-hack-could-save-you-thousands_JlXfoZvTwzk_20260820.txt
---

# Share a Localhost Internal Tool Over a Mesh VPN Rather Than Deploying It

## TL;DR

To let a couple of teammates use an internal tool you built to run locally, put them on a mesh VPN (Tailscale) and hand them the localhost URL, instead of deploying it, adding auth, and paying for hosting.

## Why it matters

Self-built internal tools are usually local-first: a localhost server plus a local agent session. The moment a second person wants one, the default move is to deploy it, which drags in hosting, a domain, and an auth layer for a two-person audience. A mesh VPN skips all of that: the tool stays on your machine, the network grants access per named device, and nothing about the tool changes. It also keeps a tool that runs on your cached CLI login off the public internet, where exposing it would be both a security and a terms problem.

## How to apply

Install the mesh VPN on your machine and on each teammate's, add them to your network, and share the localhost URL as-is. Keep the audience explicitly named rather than open, and keep anything you intend to sell off this path entirely.

## Related

[[build-internal-tools-on-the-agent-sdk-with-your-cached-cli-login]]
