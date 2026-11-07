---
id: subagent-per-competing-approach-then-main-session-decides
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Spin Up One Subagent Per Competing Implementation Idea, Let the Main Session Pick

## TL;DR

When torn between a few ways to implement something, spawn a separate subagent per approach to research/explore each one, feed all results back to the main session, and have the main session decide and present a single plan rather than exploring every option in the main context.

## Why it matters

Exploring several competing approaches directly in the main conversation bloats context with dead-end research. Isolating each approach in its own subagent keeps the decision-making context clean.

## How to apply

For each candidate approach, spawn a subagent to explore it (codebase search and/or online research). Once all subagents report back, let the main session synthesize a single plan. If you want more detail on one specific approach afterward, resume that specific subagent rather than starting over, since subagents are resumable.

