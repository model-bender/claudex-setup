---
id: plan-into-task-list-then-choose-subagent-or-team-by-size
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Convert a Long Plan Into a Task List, Then Decide Subagent-Per-Task vs. Agent Team by Its Size

## TL;DR

For a long spec-developer plan, ask Claude Code to turn it into an explicit task list first, then either have it complete each task inside a subagent, or spawn a full agent team when the list is long and complex enough to warrant it.

## Why it matters

An explicit task list gives you a concrete unit to route: small task lists are cheap to run through individual subagents, while large, complex lists justify the extra coordination cost of an agent team.

## How to apply

After a big plan is finalized, say 'turn this into a task list.' For a short list, tell Claude Code to complete each task itself inside a subagent. For a long, complex list, tell it to spawn an agent team to complete the list instead.

## Related

[[agent-teams-for-cross-domain-collaboration]]
