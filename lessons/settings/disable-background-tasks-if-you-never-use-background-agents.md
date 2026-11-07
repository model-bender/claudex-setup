---
id: disable-background-tasks-if-you-never-use-background-agents
created: 2026-11-06
status: active
supersedes: null
category: settings
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1xin646/claude_code_burns_1520_of_your_tokens_on_a_3word/19ru5vf3mvxk4/
---

# Set CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1 If You Never Use Background Agents: Their Status Summaries Are Model Calls Your Cost Tools Cannot See

## TL;DR

The short background-task status summaries are their own model calls, they do not appear in transcript-based cost tools, and one env var removes them if you do not run background agents.

## Why it matters

The headline figure in the thread (15 to 20 percent of tokens) comes from an agent-heavy setup, so the number is not yours; the durable point is that a whole query class is invisible to ccusage-style tools and measurable only in telemetry.

## How to apply

Group your OTel export by query_source to see what the class actually costs you, then set CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1 if you do not use background agents.

Checked: claude 2.1.318 binary: CLAUDE_CODE_DISABLE_BACKGROUND_TASKS 4 hits, query_source 22 hits.

> "and if you dont use background agents, CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1 stops it with no preload", u/RealFullMetal on r/ClaudeAI
