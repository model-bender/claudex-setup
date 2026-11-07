---
id: general-purpose-subagent-runs-full-tool-sonnet
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-workflow-explained-u0026-when-to-use-each_20260424.txt
---

# The Built-In 'general-purpose' Subagent Runs on Sonnet With Full Read/Write Tools

## TL;DR

Besides Explore (read-only, and since 2.1.198 on your main model rather than Haiku) and the plan-mode research agent, Claude Code has a third automatic built-in subagent called general-purpose that runs on Sonnet with full tool access, and Claude delegates to it on its own for complex multi-step tasks that need both exploring the codebase and editing across multiple files.

## Why it matters

The transcript states these three built-in subagents (explore, plan, general-purpose) exist and are chosen automatically based on task complexity, without the user asking, keeping the main conversation's context window clean. Not knowing general-purpose exists means missing why some requests spin up a full-access sub-session unprompted.

## How to apply

Give Claude a task that needs both reading around the codebase and making changes in several files (not just a lookup); watch the terminal for a 'general-purpose' tool invocation running under its own context window with read+write access. No configuration needed; it is automatic.

## Related

[[explore-subagents-run-on-your-main-model-route-cheap-search-to-your-own-haiku-agent]]
