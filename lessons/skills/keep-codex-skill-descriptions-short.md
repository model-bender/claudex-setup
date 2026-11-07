---
id: keep-codex-skill-descriptions-short
created: 2026-08-16
status: active
supersedes: null
category: skills
tool: codex
source_type: canonical
sources:
  - https://github.com/openai/codex/pull/34732
  - https://github.com/openai/codex/pull/34997
---

# Keep Codex Skill Descriptions Short - a Long One Steals Budget From Every Other Skill

## TL;DR

Codex renders the skill catalog into a fixed metadata budget scaled to the model's context window; under pressure it shortens descriptions round-robin, then drops descriptions entirely, then omits whole skills - so one verbose description degrades the catalog for all of them.

## Why it matters

A skill the model cannot see does not exist. This degradation used to be completely silent: you would write a skill, install it correctly, and it would simply never fire, because a different skill's essay-length description had eaten the budget before the catalog reached yours.

Codex only recently started warning at all. It now emits the omitted-skill count, and warns separately when description shortening averages more than 100 characters per skill - a threshold that also tells you roughly how much description budget you actually have.

## How to apply

Budget roughly one short sentence per skill description, and prune disabled skills so names, locators, and full descriptions all fit. When Codex prints the omitted-skill or shortening warning, treat it as a signal to cut the catalog rather than as noise.

> "Long skill descriptions can consume the catalog's metadata budget before later skills are listed, hiding otherwise usable skills from the model.", openai/codex#34732

## Related

[[put-every-skill-one-level-under-skills]], [[codex-has-no-custom-slash-commands-port-them-as-skills]]
