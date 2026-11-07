---
id: agent-team-teammates-dont-inherit-conversation-history
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/simon-scrapes/how-to-use-claude-code-agent-teams-in-13-mins-opus-4-6_20260307.txt
  - transcripts/simon-scrapes/every-claude-code-concept-explained-for-normal-people_20260307.txt
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
---

# Agent-Team Teammates Don't Inherit Your Main Conversation History, Even Though They Share the Team Task List

## TL;DR

Spinning up teammates doesn't hand them the conversation history from your main session; you have to make sure Claude passes them enough context to actually do their job.

Unlike a forked subagent, each teammate spun up in an agent team receives only a sample of the accumulated context, not the complete history of the main conversation.

Agent-team teammates load your CLAUDE.md and MCP servers but never receive the main session's conversation history, so anything you've already discovered has to be explicitly copied into the tasks you hand them.

## Why it matters

Without this awareness, you might assume a teammate knows everything discussed in the lead session so far, when in fact it starts with only whatever the lead explicitly gives it plus the shared task list.

If you expect every teammate to know everything the main session has discussed, you'll be surprised when one is missing nuance another has; plan what each teammate needs explicitly instead of assuming shared context.

A teammate spawned mid-session starts blind to everything you and the orchestrator worked out beforehand, which produces answers that ignore your prior findings.

## How to apply

When spawning an agent team, verify (or explicitly instruct) that the team lead passes a generous, specific amount of relevant context to each teammate at spawn time, since none of the prior conversation carries over automatically.

When briefing an agent-team teammate, restate the specific facts or decisions it needs rather than assuming it inherited the full main-session context the way a forked subagent would.

Before kicking off an agent team, ask the orchestrator to embed all the important code pointers or facts gathered so far into the tasks so each teammate's task description carries the needed context.

## Related

[[agent-teams-agent-should-not-touch-same-files]], [[agent-team-teammates-now-inherit-the-leader-s-model-name-the]]
