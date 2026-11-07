---
id: build-internal-tools-on-the-agent-sdk-with-your-cached-cli-login
created: 2026-08-22
status: active
supersedes: null
category: automation
tool: [codex, claude-code]
sources:
  - transcripts/mark-kashef/this-ai-hack-could-save-you-thousands_JlXfoZvTwzk_20260820.txt
---

# Power Internal Tools With the Codex/Claude SDK on Your Cached CLI Login Instead of a Metered API Key

## TL;DR

Construct the Codex SDK (or Claude Agent SDK) client with no arguments so it picks up the login your CLI already cached, and every button in your self-built internal tool runs a headless worker on the subscription you already pay for - no API key, no second credit card.

## Why it matters

The usual shape of a self-built replacement for a SaaS subscription is: you cancel a $50/month tool, build the replacement, then wire in an API key so every click costs metered money. Mark Kashef's swap removes only that layer: the SDK acts as a bridge to a headless session of the subscription, so a meeting-analyser, a thumbnail generator, or an email triage tool runs for no marginal cost. Anything the subscription can do is available through the bridge - model choice, reasoning-effort tiers, and image generation (his thumbnail lab drives GPT image 2 through the same path). The constraint that makes or breaks this: both the Codex and Claude SDK terms restrict it to personal and internal use. Building a public SaaS on rotated subscription accounts is a ToS violation - he notes companies are doing it and that it can get you in trouble. Pair that with [[dont-wire-max-account-into-third-party-agent-runners]]: first-party SDK, internal use, is the sanctioned version of the same instinct.

## How to apply

In the build prompt, make the auth path the defining constraint rather than an afterthought: 'Build a complete runnable local-first internal tool. All AI calls go through the SDK using my cached login, so there is no API key anywhere. Do not ask for an API key. The SDK finds the authorization on its own when constructed with no arguments.' Then give it the architecture, the localhost server, and the file skeleton, with the SDK wrapper as file one. Have Codex or Claude Code help write this prompt once, then reuse it - the same swap retrofits onto existing internal tools by replacing the API-key call layer. Keep the scope to internal tools, workflows, and integrations; for anything you sell, go back to metered keys. To share a local tool with a small team without deploying it, a mesh VPN (he uses Tailscale) exposes the localhost URL to named teammates.

## Related

[[dont-wire-max-account-into-third-party-agent-runners]], [[share-a-local-internal-tool-over-a-mesh-vpn-instead-of-deploying-it]]
