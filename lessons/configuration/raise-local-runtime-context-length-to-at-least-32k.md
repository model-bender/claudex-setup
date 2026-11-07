---
id: raise-local-runtime-context-length-to-at-least-32k
created: 2026-07-25
status: active
supersedes: null
category: configuration
source_type: post
tool:
  - claude-code
  - codex
sources:
  - https://martinfowler.com/articles/exploring-gen-ai/local-models-for-coding-factors.html
---

# Raise a Local Runtime's Context Length to 32K–64K Before Agentic Coding: the Default Is Far Too Small

## TL;DR

LM Studio / Ollama-style runtimes ship a context length sized for chat, not for an agent doing tool calls, and the slider has to be moved manually, but that headroom comes out of the same RAM budget as the weights.

## Why it matters

"Context window size consumes RAM on top of model weights through the KV cache, which grows with context length", so context length and model size compete for the same memory. That's why a 15–25GB model is the comfortable band on a 48GB machine rather than the largest thing that technically loads. The default setting is the quieter problem: it silently caps agent runs rather than erroring, so the model looks incapable when it is merely truncated.

## How to apply

In LM Studio: Load > Context, and Offload > Context Length, set 64K as your default minimum, and drop the model size a tier if RAM won't take both. Budget the context window *before* picking the model, not after.

> "The default size configured in the runtimes is far too small for agentic coding, it has to be set to at least 32K, if not 64K.", Birgitta Böckeler (Thoughtworks)

## Related

[[size-local-models-by-half-params-and-keep-a-quantization-floor-for-tool-use]], [[turn-reasoning-off-on-local-coding-models]], [[prune-the-system-prompt-when-an-agent-runs-on-a-local-model]]
