---
id: check-the-sample-size-before-rerouting-to-a-hyped-model
created: 2026-09-12
status: active
supersedes: null
category: model-selection
tool: [claude-code, codex]
sources:
  - transcripts/john-kim/wtf-ox-alpha-a-free-unlimited-ai-model_YrUVDm88zBw_20260910.txt
---

# Check the Sample Size Before You Re-Route Work to a Hyped New Model

## TL;DR

Ox Alpha's viral 80% score came from a community run over roughly eight questions. On the full set it scored 58.4%, which placed it between Opus 4.8 and Qwen3 Max rather than ahead of Opus 5.

## Why it matters

Stealth launches are marketed through social media, and the first numbers are community-run, unofficial and tiny, which is exactly the regime where a couple of lucky items doubles the headline. Usage on the model spiked and then collapsed once people ran it themselves. Rebuilding a routing table on a number like that costs a week of degraded output before anyone notices.

## How to apply

Before changing a default model, find who ran the eval and over how many items; if it is not an official benchmark with a published set, run the candidate on two or three of your own real jobs and compare against your current default before switching anything.

## Related

[[stop-comparing-models-on-dollars-per-million-tokens-tokenizers]], [[benchmark-skill-mines-chat-history-and-a-personal-rubric]]
