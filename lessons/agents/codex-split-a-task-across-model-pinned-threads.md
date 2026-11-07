---
id: codex-split-a-task-across-model-pinned-threads
created: 2026-09-24
status: active
supersedes: null
category: agents
tool: codex
sources:
  - transcripts/mark-kashef/stop-burning-codex-tokens-on-every-task_575v0WYJQsE_20260920.txt
---

# Split a multi-stage task across Codex threads pinned to different models

## TL;DR

For a task with distinct stages, run separate Codex threads each pinned to a different model (a cheap cloud model for research, a local model to shortlist, the frontier model for final synthesis) and explicitly tell Codex to pass results from one thread to the next.

## Why it matters

Demonstrated concretely: a GLM thread researched hardware specs, handed its findings to a local Gemma thread that produced a shortlist, which fed a final Astra summary diagram; the Astra thread spawned the other two itself from one prompt. This keeps the expensive model's involvement to the step that actually needs it instead of running the whole pipeline on one model. The same video shows the enabling move on its own: inside one Codex project the active model is a per-conversation choice, so routine SOP-shaped work (a defined skill or AGENTS.md procedure) can run on a much cheaper model while the frontier model is kept for open-ended work.

## How to apply

Ask the frontier-model thread to spin up one thread per stage, naming the model for each and which thread's output feeds which, or open them yourself and pick the model per thread in the picker. From the CLI, `-m <model>` picks a cloud model per invocation, and a local model needs `--oss --local-provider ollama` (a plain model override cannot reach a local server). Keep the frontier model on the synthesis step only. Checked: `-m, --model`, `--oss` and `--local-provider` are in `codex --help` on codex-cli 0.156.1.
