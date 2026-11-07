---
id: agent-team-bypass-permissions-propagate-restrict-reviewer-explicitly
created: 2026-09-01
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/simon-scrapes/how-to-use-claude-code-agent-teams-in-13-mins-opus-4-6_20260307.txt
---

# Agent-Team Permissions Propagate: A Bypassed-Permissions Session Passes That to Every Teammate

## TL;DR

If the team lead starts with dangerously-skip-permissions on, every spawned teammate inherits that same unrestricted permission level, including a reviewer teammate you wanted to keep read-only.

## Why it matters

Without knowing this, you can accidentally give a review-only teammate full edit access just because the lead session was started with bypass permissions on.

## How to apply

If you need a teammate (e.g. a reviewer) to stay read-only while running the team lead with bypass permissions, explicitly ask Claude to restrict that specific teammate's permissions after spawning; don't assume role-based intent alone limits it.

## Related

[[agent-teams-agent-should-not-touch-same-files]], [[scope-team-tasks-small-add-adversarial-reviewer]]
