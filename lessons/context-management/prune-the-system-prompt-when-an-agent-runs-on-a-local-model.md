---
id: prune-the-system-prompt-when-an-agent-runs-on-a-local-model
created: 2026-07-25
status: active
supersedes: null
category: context-management
tool:
  - claude-code
  - codex
sources:
  - transcripts/mark-kashef/how-to-finally-use-local-ai-in-45-minutes_84POiAUhtSI_20260724.txt
---

# On a Local Model, a Bloated System Prompt Is a Latency Tax: Prune It and Compress the KV Cache

## TL;DR

Every token of an agent's system prompt is re-processed by your own hardware on each turn, so a mammoth system prompt that costs you nothing noticeable on a hosted model can turn a local model's reply to "hi" into a two-minute wait. Diagnose the prompt, cut what that agent doesn't need, and summarize old turns.

## Why it matters

The creator ran a Hermes agent on a 14B model on a Mac Mini and it took around two minutes to answer "hi". A diagnostic showed the agent's system prompt was "humongous and a lot of it I didn't actually need"; pruning it dropped the response to about 30 seconds, a 4× latency win from deleting instructions, with no model or hardware change. The mechanism is the KV cache: the system prompt plus every accumulated multi-turn exchange and tool call sits on the same desk and is paid for on every turn, and tool-calling harnesses accumulate it fastest. This is the local-inference reason to do what context minimalism already recommends for quality reasons, here it shows up as wall-clock rather than as degraded answers.

## How to apply

When a local-model-backed agent is *slow* rather than *wrong*, run a diagnostic on what is actually being pushed through the model per turn before touching hardware or model size. Then three levers, cheapest first: (1) cut the agent's system prompt to what that specific agent needs, generic scaffolding is pure latency here; (2) keep per-instruction context small, don't write an essay where a line does; (3) compress the cache itself, quantize it, or summarize every ~20 messages into one persisted message so the conversation stops dragging its full history forward. Note that MiniMax-style sparse attention (the model chooses which past tokens to attend to) attacks the same problem at the model level, so it becomes a selection criterion if your workload is long-context.

## Related

[[be-a-context-minimalist-provision-a-lean-harness]], [[size-local-models-by-half-params-and-keep-a-quantization-floor-for-tool-use]]
