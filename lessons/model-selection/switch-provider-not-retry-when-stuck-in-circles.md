---
id: switch-provider-not-retry-when-stuck-in-circles
created: 2026-09-01
status: active
supersedes: null
category: model-selection
tool: [claude-code, codex]
sources:
  - transcripts/ray-amjad/my-claude-code-workflow-for-2026_20260307.txt
---

# Switch to a Different Provider When a Model Loops on the Same Bug

## TL;DR

When your primary model gets stuck going in circles or fails outright on a hard bug, switch to a different provider's tool entirely (e.g. from Opus in Claude Code to a GPT model in Codex CLI) rather than continuing to retry the same model.

## Why it matters

Different models are trained differently and carry different biases, so a model that has failed can still be unblocked by a different one seeing the same problem fresh; this is reported as a common pattern among practitioners, not a one-off.

## How to apply

If a model loops or fails on a bug, hand the same problem to a different provider's CLI (e.g. Codex) with high or extra-high reasoning effort, instead of re-prompting the stuck model again.

