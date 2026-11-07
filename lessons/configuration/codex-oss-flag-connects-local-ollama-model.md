---
id: codex-oss-flag-connects-local-ollama-model
created: 2026-09-24
status: active
supersedes: null
category: configuration
tool: codex
sources:
  - transcripts/mark-kashef/stop-burning-codex-tokens-on-every-task_575v0WYJQsE_20260920.txt
---

# Connect Codex to a local Ollama or LM Studio model with --oss

## TL;DR

Codex CLI has a built-in reserved 'ollama' model provider. Run codex --oss (add --local-provider ollama for one run, or set oss_provider = "ollama" in config.toml as the default) to point a session at a local model server instead of a cloud model.

## Why it matters

The source connects a local model through the Ollama app (Settings > Apps > add to Codex, in the Codex desktop app). On the CLI the documented route is a flag, which the video does not mention: `--oss` points a session at a local open-source provider without any app-side wiring, which makes a cheap local model an easy per-run choice for work that does not need a frontier model.

## How to apply

Run `codex --oss` and pick the provider for that run with `--local-provider ollama` (or `lmstudio`), or set `oss_provider` in `config.toml` as the default. A custom local server can instead be declared under `[model_providers.<name>]` with `base_url = "http://localhost:11434/v1"`. Checked: `--oss` and `--local-provider <OSS_PROVIDER>` ("lmstudio or ollama") are in `codex --help` on codex-cli 0.156.1; `oss_provider` and the reserved provider IDs are from the Codex advanced-config docs, now at learn.chatgpt.com/docs/config-file/config-advanced (the old developers.openai.com URL redirects there), fetched 2026-09-24.

## Related

[[route-claude-code-to-cheaper-or-local-models]], [[shortlist-local-models-with-openrouter-api-and-your-machine-specs]]
