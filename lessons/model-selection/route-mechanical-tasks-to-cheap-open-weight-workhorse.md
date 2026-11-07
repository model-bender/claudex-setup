---
id: route-mechanical-tasks-to-cheap-open-weight-workhorse
created: 2026-09-01
status: active
supersedes: null
category: model-selection
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/how-to-finally-use-local-ai-in-45-minutes_84POiAUhtSI_20260724.txt
---

# Keep Closed-Source Models for Planning and Review, Route Mechanical Edits to a Cheap Open-Weight Workhorse

## TL;DR

Use Claude/Codex for detailed planning, bug review, and testing, but deliberately offload small mechanical tasks (renaming a batch of files, grep-style searches) to a cheap open-weight model like GLM accessed via OpenRouter, to cut cost and token spend without touching quality-sensitive work.

## Why it matters

The transcript frames this as a concrete routing rule, not just a preference: 'you can use both where you have the close source, take care of really detailed planning, bug review, testing, and then for small tasks like go and change all the names of these files, go and search for this specific file using GP... You can start to be more intentional with what you offload to what kind of model so you can save on cost and tokens.'

## How to apply

Set up an OpenRouter-backed alias for a workhorse open-weight model (e.g. GLM), and when a request is purely mechanical (bulk renames, simple search/replace, file lookups) direct it to that alias instead of your primary Claude/Codex session; reserve the primary session for planning, review, and testing.

## Related

[[one-launch-alias-per-open-weight-model-via-openrouter]]
