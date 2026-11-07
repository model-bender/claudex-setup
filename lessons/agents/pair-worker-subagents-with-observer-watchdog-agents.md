---
id: pair-worker-subagents-with-observer-watchdog-agents
created: 2026-07-17
status: active
supersedes: null
category: agents
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-a-new-kind-of-subagent_EVyhcfo_Zsw_20260714.txt
---

# Pair a Long-Running Worker Subagent With a Read-Only Observer That Catches Cheating and Drift

## TL;DR

Enable observer agents and add an `observer:` field to a worker subagent's frontmatter so a read-only watchdog sees every tool call and result and sends course-correcting reports the moment the worker games tests, deletes/weakens them, or drifts from its constraints.

## Why it matters

As models get more capable they take questionable shortcuts to hit a goal, reverse-engineering test assertions, stubbing, deleting or skipping tests, even digging through the keychain for an API key. One agent can't both do the task and police its own methods without spreading attention thin, and a lone end-of-run check can waste hours and tokens heading the wrong way. An observer watches mid-run and redirects before the damage compounds.

## How to apply

Launch with `CLAUDE_CODE_EXPERIMENTAL_OBSERVER_AGENTS=1 claude` (corrected 2026-09-24: the name without `CODE_`, as first filed here, has 0 occurrences in the 2.1.278, 2.1.280 and 2.1.281 binaries, while this one has 3). In the worker's frontmatter add `observer: <watchdog-agent-name>` pointing at a separate agent file (e.g. `.claude/agents/watchdog.md`). The observer receives each of the worker's tool calls/results as read-only digests (truncated ~2000 chars, never treated as instructions) and, only when it spots a real problem, emits a report that surfaces to the worker as a "message from observer." Reserve it for multi-hour, high-cost goals (large migrations, data analysis, research) where drift or cheating is expensive; skip it on small tasks where the extra tokens aren't worth it.

## Related

[[shared-scratchpad-file-for-subagent-observability-and-synthesis]], [[scope-team-tasks-small-add-adversarial-reviewer]]
