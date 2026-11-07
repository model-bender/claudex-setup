---
id: plan-with-the-big-model-and-execute-with-the-cheaper-sibling
created: 2026-10-11
status: active
supersedes: null
category: model-selection
tool: codex
sources:
  - transcripts/mark-kashef/i-tested-gpt-6-1-sol-vs-astra-here-s-what-i-d-use_ZJJrUSfMyko_20261007.txt
---

# Plan with the larger model and spend the build tokens on the cheaper sibling, then use the big one to clean up

## TL;DR

Mark Kashef's test (GPT-6.1 Sol vs Astra on a Codex build): similar time, $203 vs $43, so he recommends Astra plans and Sol executes.

## Why it matters

Each model failed differently: Astra's research citations were broken and Sol needed 5 to 6 extra prompts for voice input, so Astra serves as the cleaner afterwards. The best build came from Astra planning with Sol executing across eight phases.

## How to apply

Authorise the lead thread to spawn Codex threads per phase; plan with the bigger model; run build threads on the cheaper one; use the bigger model for fixes. Mark says this suits $20 or $100 plans.

REVISIT: model pricing changes.
