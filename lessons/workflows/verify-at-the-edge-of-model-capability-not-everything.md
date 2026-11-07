---
id: verify-at-the-edge-of-model-capability-not-everything
created: 2026-11-06
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/ray-amjad/openai-and-anthropic-agree-on-what-comes-after-loops_yrRpnx_iugY_20261106.txt
---

# Spend Verifier Agents on Work at the Edge of What the Model Can Do, Not on Routine Work

## TL;DR

An Anthropic article from March 2026 found an evaluator adds lift only on parts of the build near the generator's limit. Verify a hard feature like offline-online sync; skip a routine contact form.

## Why it matters

Ray quotes the article: on Opus 4.6, whose raw capability had increased, tasks inside the generator's capability make the evaluator unnecessary overhead, while tasks at the edge still gain. Every harness component encodes an assumption about what the model cannot do, and those assumptions go stale as models improve.

## How to apply

1. Per feature, ask whether it is at the edge of what your current model does well.
2. Run a verifier (for example a browser-driving agent) for edge features such as merging offline changes when a mobile app reconnects.
3. Skip or lightly check simple features.
4. Re-test these assumptions on each new model.

