---
id: size-local-models-by-half-params-and-keep-a-quantization-floor-for-tool-use
created: 2026-07-25
status: active
supersedes: null
category: model-selection
tool:
  - claude-code
  - codex
sources:
  - transcripts/mark-kashef/how-to-finally-use-local-ai-in-45-minutes_84POiAUhtSI_20260724.txt
---

# Size a Local Model at Half Its Parameter Count in GB: and Don't Quantize Below 4-Bit if It Has to Call Tools

## TL;DR

Roughly, GB of RAM needed = parameters in billions ÷ 2, and you want that under about half your machine's memory. Compress downward to the smallest quantization that still passes your own tasks, but heavy quantization destroys tool-calling first, so an over-compressed model is useless in a harness no matter how good the harness is.

## Why it matters

The naive failure is reading the box: 128GB of unified memory is not 128GB available, because your other apps and the harness need theirs, and exceeding ~50% is where problems start. The failure that matters specifically for agentic use is quantization, the creator's point is that as you compress past 4-bit toward 1-bit and below, "the ability to know how to use tools, even with a great harness, become severely prohibited." So a model that still chats acceptably can be quietly unable to drive Read/Edit/Bash, and you'll misdiagnose it as a harness problem. The speed side is just as concrete: 5–10 tokens/sec is roughly a paragraph a minute and unusable for agent loops, while 60–70 tokens/sec is workable (his 70B at ~60 tok/s used about half of 128GB).

## How to apply

Estimate memory as params ÷ 2, a 70B needs ~35–40GB, a 120B ~60GB, a 14B ~5–7GB, and keep it under half your total. To pick a candidate, prompt Claude Code to pull the current catalogue from OpenRouter's public models API rather than web-searching ("pull the latest open source models from the past 6 months as of today's date, categorized text-only vs multimodal"); it dumps JSON you can filter. Follow up with "go through my current OS specs and tell me what I'm eligible to run, and flag anything that would run too slowly", it will read your actual chip, unified memory, usable memory, and storage, and check Hugging Face for a downloadable build. Prefer an MLX build on Apple Silicon and GGUF everywhere else (GGUF is the universal format and works out of the box with llama.cpp, hence Ollama and LM Studio). Then binary-search downward: run your real tasks at each quantization and keep the smallest one that still passes, treating **tool-call reliability, not chat quality**, as the pass criterion.

## Related

[[one-launch-alias-per-open-weight-model-via-openrouter]], [[route-claude-code-to-cheaper-or-local-models]], [[prune-the-system-prompt-when-an-agent-runs-on-a-local-model]], [[shortlist-local-models-with-openrouter-api-and-your-machine-specs]], [[prefer-mlx-builds-on-apple-silicon-and-gguf-everywhere-else]]
