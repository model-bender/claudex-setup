---
id: mine-screen-history-with-a-find-loops-loop
created: 2026-07-25
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Point a Daily "Find Loops" Loop at Your Own Screen History to Discover What to Automate

## TL;DR

Identifying *which* of your repetitive habits is worth turning into a loop is the hard part. Enable Codex's Chronicle screen capture and run a scheduled loop that reads that history and recommends candidate loops back to you every day.

## Why it matters

You automate what you notice, and you don't notice your own routine. The creator's find-loops loop surfaced something he would never have written down, that he checks LinkedIn DMs daily for feedback on shipped features, and proposed the loop for it: pull the DMs, generate HTML mockups of what each request would look like in the app, and message him so he can approve one for the build agent. Screen history is the only source that captures habits living outside your repo and your ticket tracker, which is exactly where the un-automated work hides.

## How to apply

In Codex, enable Chronicle under Settings → Personalization (research preview) so it screenshots your monitors periodically, then create a scheduled loop that reads the recent history and emits daily loop candidates with the trigger, the data source, and the proposed output. Read the trade-offs before enabling it, Chronicle stores unencrypted local screenshots, consumes image-input rate limits, and is a live prompt-injection surface, and note it is unavailable in the UK/EU. Treat its output as candidates only: prove each one as a hand-run skill before promoting it to an automation.

## Related

[[loops-as-abstraction-over-prompts]]
