---
id: agent-teams-require-explicit-request-not-auto-selected
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-workflow-explained-u0026-when-to-use-each_20260424.txt
  - transcripts/simon-scrapes/every-claude-code-concept-explained-for-normal-people_20260307.txt
---

# You Must Explicitly Ask for an Agent Team, Claude Won't Auto-Select One

## TL;DR

Unlike Explore/Plan/general-purpose subagents which Claude delegates to automatically based on task complexity, Agent Teams is never chosen on its own; you must say in your prompt that you want an agent team.

Claude Code will spawn ordinary subagents on its own when it judges them useful, but it will not form an agent team unless you explicitly ask it to.

## Why it matters

The transcript contrasts this directly: 'you must still specify that you want to use an agent team, not like sub agents where it will choose those automatically.' This matters because someone could describe a complex multi-part task and get a single-session split-and-merge response instead of a team, purely because they didn't ask for a team by name.

Agent teams cost more since each teammate is a full separate Claude Code instance sharing a task list, so the harness requires deliberate opt-in rather than the casual auto-delegation used for regular subagents.

## How to apply

When you want cross-agent collaboration (teammates that can message each other and share a task list), state it directly, e.g. 'set up an agent team with a frontend dev, backend dev, and tester' rather than just describing the task and hoping Claude escalates to a team on its own.

For a complex multi-role build (e.g. an API developer, a frontend developer, and a tester who need to coordinate), explicitly ask Claude Code to spin up an agent team rather than assuming a big task will trigger one automatically.

## Related

[[agent-teams-for-cross-domain-collaboration]]
