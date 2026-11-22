---
id: keep-a-subagent-only-for-measured-degradation-parallel-work-or-tool-conflict
created: 2026-11-22
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-s-new-subagent-rules-will-change-how-you-build_ybx0mmd22pQ_20261026.txt
---

# Keep a subagent only when a single loop measurably degrades, the work is truly parallel, or tools and instructions conflict

## TL;DR

Default to one agent loop. Per the Anthropic article the video walks through, a subagent earns its place in three cases: the single loop shows a measurable drop in your evals, you have multiple independent tasks that each want a fresh throwaway context, or one agent would struggle to pick the right tools or its system prompt holds instructions that conflict.

## Why it matters

The video stresses the word measurable: the trigger is an actual drop in an eval, not a hunch that the context is getting busy. Outside those cases, the failure modes the video lists from the article are details lost in handoffs between agents, overlapping subagents nobody owns, and system prompts whose rules conflict.

## How to apply

For each subagent you have, ask which of the three cases it serves. A fresh-context verifier still has a place: the article names verification as a subagent strength and lists generator-verifier among the simple patterns to start from. For the rest, use the article's test: build a small end-to-end eval, fold one subagent in at a time, and keep it as a subagent only if the folded version scores worse.

Checked: Article read directly on 2026-11-22 (claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop, dated October 22, 2026). The three 'Use them when' cases and 'keep it as a subagent only if the folded version scores worse' come from it. No Claude Code flag or setting named.

