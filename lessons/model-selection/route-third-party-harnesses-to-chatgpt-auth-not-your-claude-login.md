---
id: route-third-party-harnesses-to-chatgpt-auth-not-your-claude-login
created: 2026-07-17
status: active
supersedes: null
category: model-selection
tool:
  - claude-code
  - codex
sources:
  - transcripts/nate-herk-ai-automation/100-hours-testing-claude-code-vs-chatgpt-codex-honest-results_RLjaUES9P8A_20260627.txt
---

# Run Third-Party Agent Harnesses on ChatGPT Auth: OpenAI Sanctions It, Anthropic Doesn't

## TL;DR

OpenAI publicly allows signing into third-party runners like OpenClaw and Hermes with a ChatGPT subscription, while Anthropic's Agent SDK docs state third-party developers may not offer Claude.ai login or rate limits without prior approval. If you live in those harnesses, run them on Codex.

## Why it matters

This is a licensing difference, not a capability one, and it quietly decides the tool for a whole category of work. The alternative to subscription auth is a metered API key, which is drastically more expensive for always-on agents.

It also gives the positive counterpart to the ban risk in [[dont-wire-max-account-into-third-party-agent-runners]]: instead of just "don't use your Max login", there's a sanctioned, subscription-priced path, it just happens to run on the other vendor.

## How to apply

For OpenClaw, Hermes, or similar wrappers, authenticate with your ChatGPT subscription and route the usage through Codex. Keep Claude subscription auth to first-party Claude Code.

Both vendors' terms move, re-read the Agent SDK page before assuming the restriction still stands.

## Related

[[dont-wire-max-account-into-third-party-agent-runners]], [[route-work-between-claude-code-and-codex-by-task-type]]
