---
id: never-route-a-codex-subscription-through-a-sub2api-bridge-use
created: 2026-08-22
status: active
supersedes: null
category: model-selection
tool: codex
source_type: post
sources:
  - https://x.com/thsottiaux/status/2090675027670978569
---

# Never route a Codex subscription through a sub2api bridge: use Sign in With ChatGPT in the OSS client instead

## TL;DR

The Codex lead confirms sub2api subscription-to-API bridges trip OpenAI's fraud-prevention systems and were the common factor behind users reporting anomalous usage-limit drain, while native ChatGPT sign-in in third-party clients is explicitly sanctioned.

## Why it matters

This closes a live ambiguity: it is not "third-party client bad, official client good", the line is the auth mechanism. People reach for sub2api precisely to plug a subscription into a harness that only speaks the API, and the symptom (limits draining faster) looks like a billing bug rather than an enforcement action, so it gets misdiagnosed.

## How to apply

Drop any sub2api / subscription-to-API-key proxy and authenticate with `Sign in With ChatGPT` in the client itself. Tibo names Pi and OpenCode as OSS clients that support it: "You are completely fine if you use your subscription through Sign in With ChatGPT, either through the official clients or through one of the many OSS clients (Pi, OpenCode, ...) that support signing in with your account and using your included usage."

> "Converting a subscription into api traffic to then re-serve or share across many users is not something we support and this type of usage gets flagged by our fraud-prevention systems.", Thibault (Tibo) Sottiaux
