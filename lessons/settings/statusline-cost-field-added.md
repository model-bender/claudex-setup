---
id: statusline-cost-field-added
created: 2026-09-01
status: active
supersedes: null
category: settings
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-connected-claude-code-to-your-browser_20260307.txt
---

# A New Cost Field Was Added to Statusline Input

## TL;DR

Claude Code's statusline input now includes a cost/currency usage field, so a custom statusline can display an accurate running cost, not just token or context counts.

## Why it matters

Before this field existed, a custom statusline could not surface accurate cost information because the data simply wasn't passed to it.

## How to apply

When building a custom statusline with /statusline, reference the new currency/cost field in the input JSON to show real spend alongside other metrics like context usage.

