---
id: try-gpt-6-1-sol-before-astra-for-long-codex-runs
created: 2026-10-02
status: active
supersedes: null
category: model-selection
tool: codex
source_type: canonical
sources:
  - https://developers.openai.com/codex/changelog
---

# Try gpt-6.1-sol as the Codex default for repeated, long-running work before reaching for Astra

## TL;DR

Sol is the cheaper near-Astra model and became the bundled default model in Codex 0.159.1.

## Why it matters

Long unattended runs burn the most usage, so the cheaper model is the first thing to test there. Availability depends on plan, client and workspace.

## How to apply

Select it with `codex -m gpt-6.1-sol` or `model = "gpt-6.1-sol"` in config.toml, and compare against Astra on one real task before switching routines.

Verified: changelog text quoted from the live page via curl; 0.159.1 entry says "Added GPT-6.1 Sol as the default model in the bundled catalog"; string gpt-6.1-sol found in the installed codex binary (codex-cli 0.160.0). The `-m` flag was not re-run against an account.

> "GPT-6.1 Sol offers near-Astra performance for complex work at a lower cost than Astra. Consider it for repeated, long-running work across code, apps, and documents.", Codex changelog (2026-09-29)
