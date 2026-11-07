---
id: crons-watch-models-act
created: 2026-08-16
status: active
supersedes: null
category: automation
tool: claude-code
source_type: post
sources:
  - https://yegge.ai/essays/the-shape-of-things-to-come/
---

# Split Unattended Work as "Crons Watch, Models Act" - Put Detection in launchd/systemd

## TL;DR

Standing agent setups need a large layer of dumb, deterministic OS-level wiring whose only job is to notice a condition and wake an agent; the model should be invoked for judgment, never for polling.

## Why it matters

An always-on agent that watches for its own triggers burns tokens and context on work a cron does for free and more reliably. The scale is the surprising part: a working fleet needed roughly **45 launchd/systemd units** of non-model plumbing - reapers, durability flush, patrols, queues - to keep the model layer doing only judgment.

That ratio is the lesson. If your "autonomous agent" is mostly a loop that checks whether anything happened, you are paying frontier-model prices for `test -f`.

## How to apply

For each recurring concern, write the detector as a scheduled unit (launchd, systemd, or cron) that evaluates the condition cheaply, and only then invokes `claude -p` or a background session with the specific situation already identified. Resist the instinct to hand the whole watch loop to the agent.

> "I have about 45 launchd/systemd units across the mini and the VM that wake an agent when something needs judgment. The rule is: crons watch, models act.", Steve Yegge

## Related

[[no-session-persistence-for-batch-headless-runs]]
