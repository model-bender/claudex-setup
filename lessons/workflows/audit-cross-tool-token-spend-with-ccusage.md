---
id: audit-cross-tool-token-spend-with-ccusage
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Read Local Agent Logs With ccusage to See Spend Across Every CLI You Run

## TL;DR

ccusage reads the local logs of Claude Code, Codex, Gemini, Goose and OpenCode and reports models, input and output tokens, totals and cost per time period in one place.

## Why it matters

The in-app views only see their own tool, so if you route work across Claude Code and Codex (and anything else) you have no single number for what an experiment actually cost. ccusage gives one table across dates and models, which is what makes a routing change measurable rather than a feeling.

## How to apply

Install the ccusage repo and point it at your local log directories, then read the per-day and per-model breakdown after a week of a new routing rule to see whether the cheaper tier actually absorbed the work.

## Related

[[have-the-agent-drive-agentsview-for-an-in-session-cost-breakdown]], [[run-insights-for-a-usage-report-card-and-pipe-into-automation]]
