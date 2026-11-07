---
id: one-launch-alias-per-open-weight-model-via-openrouter
created: 2026-07-25
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/mark-kashef/how-to-finally-use-local-ai-in-45-minutes_84POiAUhtSI_20260724.txt
---

# Give Each Open-Weight Model Its Own Launch Alias via OpenRouter, and Trial Models There Before Buying Hardware

## TL;DR

Rather than editing base-URL settings each time you want a different open-weight model, have Claude Code read OpenRouter's Claude Code integration docs and generate one shell alias per model. `claude` stays on your Anthropic auth; a named alias launches the same harness on Kimi K3, GLM 4.6, or anything else on OpenRouter.

## Why it matters

Switching models by editing config is a per-switch cost, and that cost is exactly what stops you from actually comparing models on your own work. Routing through OpenRouter *first* also inverts the expensive mistake: downloading a 70GB model to discover it's wrong for your workflow costs far more than renting it per-token for an afternoon. The creator's point is that you keep "the harness of Claude Code", plan mode, agents, and subagents all still fire on an open-weight model, while only the brain changes, so the comparison is apples-to-apples with your real setup. Only then commit the winner to local hardware. It also gives cheap work a home: bulk renames, greps, and always-on ambient agents, with the frontier model kept for planning, bug review, and testing.

## How to apply

Open a fresh Claude Code session and paste OpenRouter's Claude Code integration doc URL with: "I want to use OpenRouter's API natively through Claude Code, read the documentation, spin up subagents for the details, and create a full plan, maybe switching the model via an alias." It will come back asking for your primary open-weight model and how to store the OpenRouter API key (keychain or a private, gitignored file, pick one deliberately). The result is one launch shortcut per model that you invoke from a new terminal; the session header then shows e.g. `moonshot/kimi-k3` or `glm-4.6`. Keep the plain `claude` command untouched on Anthropic auth, so routing is a choice of command name rather than a config edit. Two caveats: pointing at a non-Anthropic base URL turns Remote Control off, and this extends cheap-model routing, it doesn't make an open-weight model a substitute for your hardest reasoning.

## Related

[[route-claude-code-to-cheaper-or-local-models]], [[remote-control-off-with-non-anthropic-base-url]], [[size-local-models-by-half-params-and-keep-a-quantization-floor-for-tool-use]]
