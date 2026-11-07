---
id: upgrade-a-struggling-haiku-log-analysis-subagent-to-sonnet
created: 2026-09-01
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# If a Haiku Subagent Can't Find the Relevant Error in Logs, Upgrade It to Sonnet

## TL;DR

When a log-analysis subagent running on Haiku fails to correctly identify the relevant error, switching that subagent's model to Sonnet resolves it in many cases.

## Why it matters

Haiku is fine for simple log fetch-and-report tasks, but sifting through logs to find the one relevant error line requires more reasoning than Haiku reliably provides.

## How to apply

Run your log-exploring subagent (e.g. a dedicated OS-specific Log Explorer subagent) on Haiku by default. If it repeatedly fails to surface the actual relevant error, bump that subagent's model to Sonnet.

