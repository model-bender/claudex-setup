---
id: workflow-size-medium-now-means-under-10-agents
created: 2026-09-24
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Dynamic Workflows Default to "Small" on Pro Plans Now, and "Medium" Dropped From 15 to 10 Agents

## TL;DR

The library's existing lesson (sourced from 2.1.219) that dynamic workflows default to "medium" (aim under 15 agents) is now out of date twice over: Pro plans default to "small," and "medium" itself was cut from under-15 to under-10 agents.

## Why it matters

A workflow-authoring run that used to fan out to ~15 agents on medium now quietly caps closer to 10, and Pro-plan users get an even smaller "small" default they may not have explicitly chosen, the same silent-narrowing failure mode the superseded lesson already warned about, just at new numbers.

## How to apply

Set workflowSizeGuideline explicitly (unrestricted/large/medium/small) in settings.json or /config -> Dynamic workflow size if you want a specific fan-out width; don't assume "medium" still means under-15, and don't assume Pro-plan sessions default to medium at all. Checked: `workflowSizeGuideline` confirmed in the installed 2.1.281 binary with the option set `["unrestricted","small","medium","large"]` (command grep -a -o).

> "Changed the default dynamic workflow size to small on Pro plans and lowered the medium size guideline from 15 to 10 agents", Claude Code CHANGELOG 2.1.271
