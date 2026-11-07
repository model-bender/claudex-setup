---
id: prompt-bouncer-mod-rejects-vague-prompts-before-the-main-model-runs
created: 2026-10-19
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/ray-amjad/most-claude-code-mods-are-toys-these-are-for-agentic-engineers_Od9706XIXcc_20261013.txt
---

# Reject Vague Prompts With a Haiku 'Prompt Bouncer' Mod Before They Cost a Full Turn

## TL;DR

A mod can send each prompt to Haiku first and bounce it back with a reason if it is too unclear (for example 'fix the thing on the settings page'), and can use a project glossary to say which term to use.

## Why it matters

Ray Amjad's reasoning: a vague prompt written when tired makes the agent do the wrong work and wastes far more tokens than the small classification would. With a glossary the bounce is specific ('this project calls it the billing page'). He expects prompts to get clearer over time, at the price of early annoyance.

## How to apply

1. Ask Claude for a mod that classifies each submitted prompt with a small model and blocks unclear ones with a one-line reason. 2. Give it a project glossary file so it can name the right terms. 3. Expect many rejections at first. Checked: claude 2.1.303 binary: plugin API has model.classify and prompt-related calls (prompt.read, prompt.compose); the behaviour is the speaker's demo, not tested.

## Related

[[gate-a-fork-behind-a-small-model-classifier-after-every-turn]], [[learn-technical-vocabulary-for-precise-prompts]]
