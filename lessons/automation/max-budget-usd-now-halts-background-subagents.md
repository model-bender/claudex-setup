---
id: max-budget-usd-now-halts-background-subagents
created: 2026-07-25
status: active
supersedes: null
category: automation
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# `--max-budget-usd` Is Now a Real Hard Stop for Background Subagents, Not Just the Main Loop

## TL;DR

Until 2.1.217, `--max-budget-usd` did not stop background subagents, an unattended fan-out could run straight through the cap. It now denies new spawns and halts running background agents once the cap is reached.

## Why it matters

Anyone who set a budget cap on a headless fan-out before 2.1.217 had a guardrail that failed to guard the most expensive part of the run, which is exactly the part nobody is watching. Worse, that experience teaches the wrong lesson, that the flag doesn't work, and people stop reaching for it.

## How to apply

Pass `--max-budget-usd <amount>` to headless and background fan-out runs; on 2.1.217+ it bounds background subagent spend as well as the main loop. If you tried it before and concluded it was useless, re-test on a current version.

> "Fixed `--max-budget-usd` not stopping background subagents: once the cap is reached, new spawns are denied and running background agents are halted", Claude Code CHANGELOG 2.1.217

## Related

[[pin-subagent-spawn-depth-the-default-flipped-twice]], [[workflow-size-medium-now-means-under-10-agents]]
