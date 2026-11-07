---
id: codex-subagents-dont-auto-invoke
created: 2026-07-17
status: active
supersedes: null
category: agents
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/how-to-use-your-claude-code-projects-in-codex-in-5-mins_kB9iMD0EjT8_20260627.txt
  - transcripts/nate-herk-ai-automation/100-hours-testing-claude-code-vs-chatgpt-codex-honest-results_RLjaUES9P8A_20260627.txt
  - transcripts/john-kim/complete-beginner-s-guide-to-openai-s-codex-app_20260424.txt
---

# Codex Subagents Never Auto-Invoke: Name Them Explicitly or They Don't Run

## TL;DR

Codex's docs state it won't spawn a subagent unless you explicitly ask, while Claude Code decides on its own to spin up planner/explorer/reviewer agents. A workflow ported to Codex that relied on auto-delegation quietly runs single-threaded in the main context.

## Why it matters

This failure is silent. Nothing errors, the work just happens in the parent thread, so you lose both the parallelism and the context isolation the subagent existed to provide, and the main thread fills with the noise you were trying to keep out.

It's the single biggest behavioural difference to catch when moving a Claude Code setup across, because the config ports cleanly and the behaviour doesn't.

## How to apply

Say it in the prompt, "spawn a subagent to investigate X", and pin the model while you're there, since an explicit spawn is the natural place to drop to a cheaper one:

> spawn a subagent to investigate colour theory for this app, use GPT-5.4-mini for this task

If a delegation should always happen, write it into `AGENTS.md` as an instruction rather than hoping for it.

Use subagents in Codex for the same two reasons as anywhere else: parallel work, and keeping noisy output out of the parent thread.

## Related

[[port-a-project-between-claude-code-and-codex-by-layer]], [[route-work-between-claude-code-and-codex-by-task-type]]
