---
id: prefer-mlx-builds-on-apple-silicon-and-gguf-everywhere-else
created: 2026-09-12
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/mark-kashef/how-to-finally-use-local-ai-in-45-minutes_84POiAUhtSI_20260724.txt
---

# Download the MLX Build on Apple Silicon and the GGUF Build Everywhere Else

## TL;DR

When you pick a local model to download, the weight format matters as much as the size: take the MLX build on Apple Silicon and the GGUF build on everything else, because GGUF runs out of the box on llama.cpp and therefore on Ollama and LM Studio.

## Why it matters

Parameter count tells you whether a model fits in memory; the format tells you whether it runs at all. GGUF is the universal format and loads without conversion in llama.cpp and everything built on it (Ollama, LM Studio), while MLX is the Apple-Silicon-native build and is the right pick on a Mac. Choosing the wrong format costs either a conversion step or a download you cannot load, and you find out after waiting for tens of gigabytes. The rule currently sits only in the How to apply sections of two larger lessons, both titled about something else (memory sizing and quantization in one, catalogue shortlisting in the other), so nobody routing by title ever reaches it.

## How to apply

Before downloading, check the model's Hugging Face page for an MLX build if you are on Apple Silicon and a GGUF build otherwise. If only one format is published, that constrains which runtime you can use, so settle it before committing to the download rather than after. When you have Claude shortlist candidates from the OpenRouter catalogue, make 'has a GGUF build' (or MLX on a Mac) part of the filter rather than a later check.

## Related

[[size-local-models-by-half-params-and-keep-a-quantization-floor-for-tool-use]]
