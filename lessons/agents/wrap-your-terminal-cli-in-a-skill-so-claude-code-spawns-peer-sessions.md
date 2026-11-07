---
id: wrap-your-terminal-cli-in-a-skill-so-claude-code-spawns-peer-sessions
created: 2026-08-16
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-just-made-subagents-feel-obsolete_oqp6D-ugtX4_20260810.txt
---

# Wrap Your Terminal's CLI in a Skill So Claude Code Launches and Steers Its Own Peer Sessions

## TL;DR

Claude Code can now message other Claude Code sessions but cannot open one. Pair that with a terminal that exposes a CLI (cmux: new workspace, split pane) and teach both halves in a skill, so one prompt fans work out into named panes you can watch, message, and follow up on.

## Why it matters

`SendMessage` used to reach only subagents and agent-team peers; it now reaches other sessions, so the missing half is spawning.

Panes beat both existing fan-out options for work you will want to revisit. A subagent disappears from view once it returns, which makes follow-up questions impossible. `claude --bg` spawns but cannot be steered mid-run - the exact ceiling the fire-and-forget lesson names. With panes you can see the entire path a session took and keep talking to it.

Claude Code does not know your multiplexer's commands, so the skill is what turns a raw capability into a single prompt.

## How to apply

Make sessions addressable first: `claude --name <name>` at launch, `/rename <name>` for a running one, and `ListAgents` to list this session's subagents plus every other reachable session.

Then write a skill (the creator's is `/peer-sessions`) that teaches Claude Code your multiplexer's commands (`cmux new workspace`, `cmux split pane`) plus the messaging protocol - including telling each spawned session "when done, send me a message back".

Dispatch at goal level: "for all the open PRs, open a new pane and do a code review of each one in a new worktree." The same primitive covers handoffs - a session that has been monitoring production logs for hours can hand a bug to a fresh named worker instead of fixing it inside its own loaded context.

## Related

[[name-your-sessions-so-they-can-message-each-other]], [[peer-session-invisible-check-remote-control-and-version-skew]], [[one-session-per-plan-phase-chained-as-stacked-prs]]
