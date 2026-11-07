---
id: set-a-subagent-effort-level-through-the-agent-tool
created: 2026-10-11
status: active
supersedes: null
category: agents
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Ask for a Subagent's Effort Level in the Delegation: the Agent Tool Takes an effort Parameter

## TL;DR

Since 2.1.292 the Agent tool has an `effort` parameter, so Claude runs a subagent at the effort level you ask for instead of the session's.

## Why it matters

This applies "drop effort, not the model" per worker: a cheap lookup at low, a reviewer at high, without a model switch for either.

## How to apply

Name the effort when you delegate ("spawn a subagent at low effort to list the call sites"). Keep retrieval-heavy subagents at medium or above, since low effort makes a model less likely to search. Checked: `effort` appears in the live Agent tool schema of a 2.1.296 session.

> "Added an `effort` parameter to the Agent tool, so Claude runs a sub-agent at the effort level you ask for", Claude Code CHANGELOG 2.1.292

