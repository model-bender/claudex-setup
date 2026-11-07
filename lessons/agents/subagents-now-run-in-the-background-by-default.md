---
id: subagents-now-run-in-the-background-by-default
created: 2026-08-07
status: active
supersedes: null
category: agents
tool: claude-code
source_type: post
sources:
  - https://x.com/bcherny/status/2071647677591466098
---

# Ask for the Foreground Explicitly When You Need a Subagent's Result This Turn

## TL;DR

Ordinary subagents now run in the background by default so you can keep talking to Claude while they work. Any workflow that assumed a dispatch blocks until its result lands inline needs to say it wants the foreground.

## Why it matters

This is a different default from the `/fork` versus `/subtask` split and from the spawn-depth flip-flop, and it is easy to conflate them. It affects plain Task-tool dispatches, so a pattern like "dispatch a reviewer, then act on its verdict in the same turn" quietly stops working as written: the turn continues without the verdict rather than erroring.

## How to apply

If a workflow needs a subagent's result before continuing in the same turn, tell Claude to run it in the foreground (or set the background flag to false where the API exposes it). Otherwise expect detached execution and an explicit check-back, and design orchestration prompts to wait on the notification rather than assuming inline delivery.

> "In the next version of Claude Code: subagents run in the background by default, so you can keep talking to Claude while your subagents work. If you want your agent to run in the foreground, just tell Claude", Boris Cherny

## Related

[[set-background-false-on-forked-skills-you-need-inline]], [[fork-is-now-a-background-session-subtask-is-the-in-session-fork]], [[cross-session-sendmessage-spans-machines-but-holds-for-approval]]
