---
id: ask-for-a-subagent-only-when-output-is-huge-and-name-what-it-returns
created: 2026-11-15
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-pros-don-t-pay-for-max-they-do-these-5-things-instead_ZRKAw472Nmk_20261108.txt
---

# Ask for a subagent only when a job produces huge output, and tell it exactly what to return

## TL;DR

Subagents draw from the same usage limit as the main chat, so a small job gains nothing from one; use one when output is large and say what the report must contain.

## Why it matters

A subagent on a small job is just extra context overhead. On a big-output job it keeps the bulk out of the main chat, but only if the report is narrow. The transcript also says to drop custom role agents unless critical and let Claude decide when to split work.

## How to apply

Leave subagent use to Claude by default. Ask for one explicitly when a task floods context (a full test run, Anthropic's own example) and specify the return, for example: run the test suite in a subagent and report only the failing tests with their error messages. Then check /usage to see whether subagents are a big share of your week, and review custom agents first if they are.

## Related

[[run-slow-waits-from-the-main-session-not-a-big-context-subagent]], [[judge-cheap-subagent-models-by-total-usage-for-the-task-not-price-per-token]], [[subagents-for-noisy-tool-calls-not-large-edits]]
