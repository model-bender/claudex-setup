---
id: turn-reasoning-off-on-local-coding-models
created: 2026-07-25
status: active
supersedes: null
category: model-selection
source_type: post
tool:
  - claude-code
  - codex
sources:
  - https://martinfowler.com/articles/exploring-gen-ai/local-models-for-coding-factors.html
---

# Turn Reasoning Off on Local Coding Models: It's Faster and Scored the Same or Better

## TL;DR

Small local models ship with reasoning on by default and loop inside the chain of thought ("Wait, ...", "Actually, ...", "But wait, ..."), burning generation time and context for no quality gain on coding tasks.

## Why it matters

This is a measured result from an automated eval setup, not a preference, same-to-slightly-better scores with reasoning disabled. On a local model the chain of thought is paid for twice: generation time on your own hardware, and KV-cache RAM that competes with the context window you just enlarged. The author's published default setup runs with reasoning disabled.

## How to apply

In LM Studio: Inference > Settings Custom Fields > Enable Thinking > disable. The author's stated default is qwen3.6-35b-a3b at 4BIT, reasoning off, max context, driven by OpenCode or Pi. Re-test on your own tasks before generalising this to a larger local model.

> "So I also did a few runs of my automated setup with reasoning off - and lo and behold, it's not only faster (which was to be expected), but also performed the same to slightly better!", Birgitta Böckeler (Thoughtworks)

## Related

[[raise-local-runtime-context-length-to-at-least-32k]], [[size-local-models-by-half-params-and-keep-a-quantization-floor-for-tool-use]], [[max-effort-is-a-trap-quality-plateaus-at-high]]
