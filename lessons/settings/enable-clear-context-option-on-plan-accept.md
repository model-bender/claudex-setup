---
id: enable-clear-context-option-on-plan-accept
created: 2026-11-22
status: active
supersedes: null
category: settings
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Set showClearContextOnPlanAccept so approving a plan can drop the planning exploration

## TL;DR

Add `"showClearContextOnPlanAccept": true` to settings.json. The plan approval menu then gains an option that approves the plan and clears the context used to make it.

## Why it matters

Planning burns tokens and all the exploration (file reads and so on) stays in context afterwards. The plan itself survives; only the exploration behind it is cleared.

## How to apply

In settings.json add `"showClearContextOnPlanAccept": true`. When a plan is presented, pick the first option, 'Yes, clear context and ...'.

Checked: Claude Code 2.1.330 binary: the settings schema describes `showClearContextOnPlanAccept` as 'When true, the plan-approval dialog offers a "clear context" option. Defaults to false.' Live docs fetched 2026-11-22: settings-reference.md says the key adds a first option, 'Yes, clear context and ...', that 'approves the plan, clears the conversation context, and starts implementing from the plan alone'; permission-modes.md says the same of the plan approval list.

