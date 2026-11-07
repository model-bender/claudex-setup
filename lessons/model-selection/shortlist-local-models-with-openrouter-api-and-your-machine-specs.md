---
id: shortlist-local-models-with-openrouter-api-and-your-machine-specs
created: 2026-08-31
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/mark-kashef/how-to-finally-use-local-ai-in-45-minutes_84POiAUhtSI_20260724.txt
---

# Shortlist Local Models by Having Claude Pull OpenRouter's Catalogue and Read Your Machine Specs

## TL;DR

Instead of web-searching for the best local model, prompt Claude Code to pull the current open-source model catalogue from OpenRouter's public models API as filterable JSON, then have it read your actual chip, memory, and storage and flag what you are eligible to run and what would run too slowly.

## Why it matters

Web search surfaces stale listicles, while OpenRouter's public models API returns the live catalogue as JSON that Claude can filter by recency and modality. Checking eligibility against your real specs (chip, unified memory, usable memory, storage) before downloading avoids fetching a huge model you cannot run, or one too slow for agent loops.

## How to apply

Prompt Claude Code to query OpenRouter's public models API: 'pull the latest open source models from the past 6 months as of today's date, categorized text-only vs multimodal', and filter the JSON it dumps. Follow up with 'go through my current OS specs and tell me what I'm eligible to run, and flag anything that would run too slowly'; it reads your chip, unified memory, usable memory, and storage, and checks Hugging Face for a downloadable build. Prefer an MLX build on Apple Silicon and GGUF everywhere else, since GGUF works out of the box with llama.cpp and therefore Ollama and LM Studio.

## Related

[[size-local-models-by-half-params-and-keep-a-quantization-floor-for-tool-use]]
