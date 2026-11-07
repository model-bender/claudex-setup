---
id: guard-skill-env-secrets-with-skill-scoped-hooks
created: 2026-08-31
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-their-internal-skills-strategy_20260424.txt
---

# Guard a Skill's .env With Skill-Scoped Hooks and a Read-Only API Key

## TL;DR

When a skill's bundled scripts need an API credential, store a read-only key in the skill's own .env and add skill-scoped hooks that block Claude from reading the .env directly or making unapproved web requests; the scripts use the key, the model only sees their output.

## Why it matters

A skill that fetches data needs a credential, and the naive setup leaves that key readable by the model and usable for arbitrary requests. Making the key read-only bounds what any misuse could do, and hooks scoped to the skill enforce the boundary mechanically for exactly that workflow instead of relying on instructions or global project config.

## How to apply

Put the API key the skill's pre-built scripts use into the skill's .env and issue it read-only at the provider. Add hooks scoped to that skill which deny reading the .env file and block web requests the scripts are not approved to make. The scripts keep working because they read the key themselves; the model just calls them and consumes the results.

## Related

[[skills-add-scripts-to-avoid-repeated-api-scaffolding]]
