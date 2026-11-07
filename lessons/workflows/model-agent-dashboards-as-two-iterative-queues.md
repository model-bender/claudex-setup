---
id: model-agent-dashboards-as-two-iterative-queues
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/simon-scrapes/stop-using-claude-code-in-terminal-it-s-holding-you-back_20260424.txt
---

# Model an Agent Task Board as 'Your Turn' / 'Agent's Turn,' Not a Linear Kanban

## TL;DR

When designing a Kanban-style board for managing agent work, use two facing queues (your turn to review, the agent's turn to act) instead of a one-way not-started/in-progress/done pipeline.

## Why it matters

Agent-assisted work is iterative: you give feedback, the agent updates, you review again; a strictly sequential Kanban flow doesn't represent that back-and-forth and makes you lose track of what's actually pending on you versus the agent.

## How to apply

When building or adopting a task board for agent output, add explicit 'your turn' and 'agent's turn' columns/lanes that a task moves between repeatedly, rather than a single forward-only status pipeline.
