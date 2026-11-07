---
id: agent-team-idle-and-task-complete-hooks
created: 2026-09-01
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
---

# Hook Into Agent-Team-Specific Lifecycle Events: Teammate-Idle and Task-Complete

## TL;DR

Beyond the standard Claude Code hooks, agent teams expose their own hook events for a teammate going idle and for a task completing, letting you trigger side effects on team lifecycle changes.

## Why it matters

These events let you react programmatically, e.g. post to Slack, Notion, or Jira, exactly when a teammate finishes work, instead of writing custom polling logic.

## How to apply

Wire a hook to the teammate-idle or task-complete event in your hooks config to fire a notification, log entry, or downstream automation when it triggers.
