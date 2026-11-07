---
id: disambiguate-tool-descriptions-with-do-not-use-clauses
created: 2026-07-10
status: active
supersedes: null
category: agents
sources:
  - transcripts/mark-kashef/anthropic-s-new-claude-architect-guide-in-39-minutes_vizgFWixquE_20260704.txt
---

# Disambiguate Overlapping Tool Descriptions With Explicit 'Do Not Use When' Clauses

## TL;DR

The most common cause of an agent calling the wrong tool is ambiguous, overlapping tool descriptions; fix it by having each description say precisely when to use the tool AND when not to - e.g. 'use get_customer for a customer ID and profile; do NOT use it when you have an order number, use lookup_order instead'.

## Why it matters

When two tools have vague overlapping descriptions the model guesses and misroutes, often silently - it can reach the right result only after 3-4 wrong calls, wasting tokens and risking misidentified data. Per Anthropic's Claude Certified Architect guide the tool description IS the tool's interface, making this the single highest-leverage reliability fix, above rewriting prompts.

## How to apply

For each custom tool, MCP tool, or subagent tool, write a specific description with concrete trigger conditions and add negative guidance naming the sibling tool to use instead. Then verify with --verbose or Ctrl+O that the agent isn't taking a detour of failed tool calls before the correct one - a correct final result can still hide inefficient misrouting.
