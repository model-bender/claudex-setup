---
id: stop-comparing-models-on-dollars-per-million-tokens-tokenizers
created: 2026-08-22
status: active
supersedes: null
category: model-selection
tool: [claude-code, codex]
source_type: post
sources:
  - https://x.com/thsottiaux/status/2088866513008873560
---

# Stop comparing models on dollars per million tokens: tokenizers differ by ~35%, so measure price per successful outcome

## TL;DR

Identical text costs a different number of tokens on each vendor's tokenizer, so a lower published price per token can still produce a higher bill; the only comparison that holds is cost per completed task on your own workload.

## Why it matters

Every model-routing table (this repo's included) is built on per-token prices treated as a standardized unit, and a ~35% tokenization gap is large enough to invert a routing decision. It also reframes the escalate/de-escalate rule: the metric that matters is price per successful outcome, not per token, so a pricier model that one-shots the task can be the cheaper row.

## How to apply

When choosing between vendors for a workload, run the same representative task on each and compare total spend to completion, not the published $/Mtok. Tibo: "What actually matters is price per successful outcome, and for that you can use benchmarks as a starting point, but really you have to try it and measure on your own use cases."

> "In one small comparison spanning English, technical, multilingual, and numerical text, the tokenizer we use for GPT-5.6 Sol used 766 tokens versus an estimated 1,170 for Claude Opus 5. That's a very significant difference of about 34.5% fewer tokens.", Thibault (Tibo) Sottiaux
