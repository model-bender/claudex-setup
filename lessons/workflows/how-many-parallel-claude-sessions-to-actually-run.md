---
id: how-many-parallel-claude-sessions-to-actually-run
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
  - transcripts/john-kim/how-i-use-claude-code-meta-staff-engineer-tips_20260307.txt
  - transcripts/ray-amjad/my-claude-code-workflow-for-2026_20260307.txt
---

# Run 3-5 Parallel Sessions Per Project, and Expect About Four to Be Your Own Supervision Ceiling

## TL;DR

Instead of running one Claude Code session at a time, keep 3-5 instances per project (10-12 total across projects) running in parallel so you're never idle waiting on one agent.

Default to Opus when you can, and hide its slower response time by juggling several Claude Code instances/panes so you keep giving other instances work while one is thinking.

A single person can realistically supervise about four parallel CLI coding sessions (Claude Code or Codex) before context-switching fatigue sets in; claims of running ten or more in parallel likely include sessions doing low-effort background busywork.

## Why it matters

A single session at a time is slow because you sit and wait for it to finish. With several running, there is almost always one that has a question, needs a decision, or has finished something to review, which shifts your bottleneck from single-session speed to how well you design your pipeline.

John Kim says all the stronger models are 'a little bit slower' but that it doesn't matter because his workflow is to give a command, switch to another instance, give another command, and so on, so no instance idles his attention.

Named as a concrete, lived ceiling: beyond four active sessions, the reported experience is exhaustion within a few hours and an inability to do anything else (like listen to music) while switching between them.

## How to apply

Open 3-5 Claude Code sessions per active project (more across multiple projects), and cycle between them as each one surfaces a question or completes a task, rather than running and waiting on a single session.

Open multiple terminal panes/instances of Claude Code, prefer the strongest model you can afford per-instance, and round-robin your attention across instances instead of waiting on one to finish before issuing the next command.

When planning how many parallel sessions to run yourself (as opposed to unattended subagents), budget for roughly four before expecting diminishing returns from your own attention.

## Related

[[parallel-sessions-with-system-notifications]], [[strongest-model-is-faster-overall]]
