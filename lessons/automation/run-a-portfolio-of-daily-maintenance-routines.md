---
id: run-a-portfolio-of-daily-maintenance-routines
created: 2026-08-16
status: active
supersedes: null
category: automation
tool: claude-code
source_type: post
sources:
  - https://x.com/bcherny/status/2088014489438621990
  - https://x.com/bcherny/status/2088022114163130511
---

# Run a Portfolio of Daily Maintenance Routines, and Tune the Routine Rather Than the PR

## TL;DR

Point a set of named daily routines - crash fuzzer, dup unifier, dead-code remover, abstraction police - at your repos via `claude.ai/code/routines` or Claude Tag in one dedicated channel, and when a PR comes back wrong, edit the routine's prompt instead of fixing that PR.

## Why it matters

The corpus already covers routine *mechanics* (lean repo per routine, cloud vs local limits, external memory, secrets and egress) but not what to point routines **at**. These four archetypes are all maintenance work a human never gets around to, and they have a measured hit rate: 388 PRs opened across Anthropic's own repos over a few weeks, 180 merged after Claude Code Review plus human review.

The tuning discipline is the other half. Roughly 1 in 50 PRs is noise, and the response is to fix the generator, not the output - a bad PR is a prompt bug. That is what makes the portfolio compound instead of becoming a queue of near-misses you hand-correct forever.

## How to apply

Create one routine per maintenance archetype at `claude.ai/code/routines` (or ask Claude Code or Tag to set them up), and have them all report into a single dedicated channel so the noise is in one place. Start from these four:

- **Crash fuzzer** - open the app in a simulator, tap around to find crashes, root-cause and fix them
- **Dup unifier** - scan for similar-yet-slightly-divergent abstractions and PR them into one
- **Dead-code remover** - delete statically unreachable code; add logging to *suspected* dead code and remove it the next day if nothing fired
- **Abstraction police** - fix leaky abstractions

When a PR is wrong, change the routine's prompt and expect it to take a few days of tuning to settle.

> "Claude generally gets these PRs right on the first shot, and if it doesn't, we ask Claude to tune its routines so it's better the next day. Sometimes it takes a few days of tuning.", Boris Cherny

## Related

[[dedicated-lean-repo-per-cloud-routine]], [[run-a-standing-refactor-agent-to-pay-down-drift]], [[run-maintenance-routines-on-opus-by-default]], [[prove-suspected-dead-code-with-a-logging-canary-before-deleting]]
