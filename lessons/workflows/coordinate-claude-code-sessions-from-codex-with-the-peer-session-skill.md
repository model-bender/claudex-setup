---
id: coordinate-claude-code-sessions-from-codex-with-the-peer-session-skill
created: 2026-08-16
status: active
supersedes: null
category: workflows
tool:
  - claude-code
  - codex
sources:
  - transcripts/ray-amjad/claude-code-just-made-subagents-feel-obsolete_oqp6D-ugtX4_20260810.txt
---

# Point the Same Peer-Session Skill at Codex and Let Codex Coordinate Your Claude Code Sessions

## TL;DR

The peer-session mechanism runs over a socket, so the coordinator does not have to be Claude Code. Install the same skill in Codex, swap "pane" for "thread", and Codex can list your running Claude Code sessions, message one, and collect its progress report.

## Why it matters

You end up sitting in whichever tool suits the task in front of you while your running work is spread across both, and migrating a session just to reach it defeats the point. Making the coordinator role portable means you ask from wherever you already are.

It also composes with the existing routing split: Codex can hold the cheap coordination thread while Claude Code sessions do the hook-heavy and subagent-heavy execution, which is the direction each is already better at.

## How to apply

Port the peer-sessions skill into Codex as a **skill** rather than a slash command (Codex has no custom slash commands), replacing pane vocabulary with thread vocabulary, since Codex already spins up many threads from one coordinator.

Then ask in plain language: "what sessions are running on my machine?" and "go to the worker-fix session and tell it to send you a progress report." Reachability caveats apply from Codex too, and are reported as a reachable/non-reachable count rather than as an error.

## Related

[[route-work-between-claude-code-and-codex-by-task-type]], [[codex-has-no-custom-slash-commands-port-them-as-skills]], [[peer-session-invisible-check-remote-control-and-version-skew]], [[wrap-your-terminal-cli-in-a-skill-so-claude-code-spawns-peer-sessions]]
