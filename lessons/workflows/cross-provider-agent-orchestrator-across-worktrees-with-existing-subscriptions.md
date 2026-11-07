---
id: cross-provider-agent-orchestrator-across-worktrees-with-existing-subscriptions
created: 2026-08-07
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/sean-kochel/the-easiest-way-to-use-codex-and-claude-code-together_ZDh1005AOtM_20260807.txt
---

# Use a Cross-Provider Orchestrator to Run Claude Code and Codex Side by Side

## TL;DR

Tools like Orca sit above multiple CLI coding agents (Claude Code, Codex, Gemini CLI, Cursor CLI), running each task in its own git worktree from one UI, authenticating with your existing subscriptions rather than API keys, syncing with your issue tracker, and shipping an orchestration skill that lets one agent hand work to an agent on a different provider mid-thread.

## Why it matters

Managing several parallel agent sessions across models is the bottleneck now, not model quality. A shared projects-to-worktrees hierarchy with issue-tracker sync removes the context-switching of juggling separate terminals, and the orchestration skill turns a manual copy-paste handoff between two CLIs into a one-line instruction ("have 3 Codex subagents review these findings"). It is a multi-worktree, multi-project, schedulable version of the manual cross-CLI review pattern.

## How to apply

1. Install the orchestrator and add each provider CLI you already subscribe to.
2. Create a project, spin up a worktree per task or branch, and pick which agent runs it. Multiple worktrees and projects run concurrently.
3. Install its orchestration skill so any session can hand a task to a different worktree or provider.
4. Use the automations tab to schedule a goal-style prompt that spins a fresh worktree, runs one agent, then chains a cross-provider review step (Codex reviewing Claude's fix) before opening a PR.

**Caution.** Routing a paid subscription login such as Claude Max through a third-party runner carries the ToS and ban risk covered in [[dont-wire-max-account-into-third-party-agent-runners]]. That warning and this recommendation come from different single sources and point opposite ways, so verify current ToS before wiring your subscription in.

## Related

[[dont-wire-max-account-into-third-party-agent-runners]], [[route-third-party-harnesses-to-chatgpt-auth-not-your-claude-login]]
