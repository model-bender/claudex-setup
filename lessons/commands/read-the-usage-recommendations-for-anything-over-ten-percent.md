---
id: read-the-usage-recommendations-for-anything-over-ten-percent
created: 2026-11-22
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-pros-don-t-pay-for-max-they-do-these-5-things-instead_ZRKAw472Nmk_20261108.txt
---

# Read the /usage recommendations: one row for every behaviour behind 10% or more of your usage

## TL;DR

Under the breakdown, /usage lists specific recommendations for anything at 10% or more of recent usage, for example trimming a CLAUDE.md that costs 49,000 tokens per request.

## Why it matters

The rows name the exact file or setting and the size of the cost, so they are directly actionable.

## How to apply

Run /usage and work through the recommendation rows. Starting with the largest share is this lesson's suggestion, not the video's; the docs note that a row's share is how much usage it applies to, not what the change saves.

Checked: Live docs at code.claude.com fetched with curl on 2026-11-22, costs page: each recommendation row starts with a share of recent usage of at least 10%, with the example '25%  Trim ~/code/api/CLAUDE.md · 49k tokens per request'. The share says how much usage the row applies to, not how much the change saves.

## Related

[[run-insights-for-a-usage-report-card-and-pipe-into-automation]]
