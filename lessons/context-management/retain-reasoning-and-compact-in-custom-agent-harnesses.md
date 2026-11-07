---
id: retain-reasoning-and-compact-in-custom-agent-harnesses
created: 2026-08-29
status: active
supersedes: null
category: context-management
source_type: canonical
tool: codex
sources:
  - https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/
---

# When Building a Custom Agent Harness on OpenAI Models, Retain Reasoning and Use Compaction, Never Rolling Truncation

## TL;DR

A harness that discards reasoning between tool calls or truncates old history cripples the model: retained reasoning plus compaction took GPT-5.6 Sol from 13.3% to 38.3% on ARC-AGI-3 while cutting output tokens 6x.

## Why it matters

Any bespoke agent loop (SDK tools, eval runners, internal bots) that rebuilds context per step silently forces the model to re-derive its plan every turn. The fix is two settings, not a better model, and OpenAI's recommendation is explicit: use the Responses API rather than legacy Chat Completions, retain reasoning, and use compaction.

## How to apply

On the Responses API, pass the previous response ID so reasoning is retained across tool calls and turns, and enable the documented compaction feature instead of dropping oldest messages at a size cutoff.

> "In the case of ARC-AGI-3, we discovered that turning on two API settings we use in ChatGPT and Codex—retained reasoning and compaction—tripled scores and cut output tokens by 6x on the public task set.", OpenAI engineering post

## Related

[[build-internal-tools-on-the-agent-sdk-with-your-cached-cli-login]]
