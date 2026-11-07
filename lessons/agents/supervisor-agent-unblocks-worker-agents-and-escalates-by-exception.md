---
id: supervisor-agent-unblocks-worker-agents-and-escalates-by-exception
created: 2026-07-25
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Run a Supervisor Agent Whose Job Is Unblocking the Workers, Escalating Only What It Can't Fix

## TL;DR

Give one agent a queue and let it spawn a fresh worker agent per item in a shared channel, then keep watching: answer the workers' questions itself, push each to a PR, and notify you on your phone only when it genuinely cannot unblock one.

## Why it matters

Fan-out alone doesn't scale, because every worker that hits a question stalls until a human sees it, so the wall-clock win evaporates into your inbox. The distinguishing move here is that the supervisor's primary job is *answering the workers*, not just reporting on them. The creator's supervisor loaded all Sentry issues affecting more than 10 users, spawned one worker per issue in a Slack channel, and answered their questions while they ran; around ten agents worked to open PRs with him reading only the exceptions. The escalations turned out to be the most valuable output: the workers surfaced a missing Xcode/Swift toolchain, which is a harness gap he then fixed permanently.

## How to apply

Prompt the supervisor with six things: the source (Sentry issues over N users, an issue-tracker query), the per-item instruction (verify the bug exists first, then go all the way to opening a PR), the isolation rule (each item gets a new agent instance), the unblock rule (help stuck workers continue), the escalation rule (if you can't unblock it, send me a phone notification saying which one and why), and the exit condition (continue until all PRs are open). Put it on a short interval loop so it re-checks. Watch the first batch closely, the creator saw one worker emitting nonsense and flagged it before running the next batch, and pair it with a stall watchdog and retry cap so a wedged worker doesn't burn tokens indefinitely.

## Related

[[give-orchestrator-broad-goals-not-narrow-checklists]]
