---
id: run-a-genuinely-risky-goal-run-on-a-vps-not-your-own-machine
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/ray-amjad/the-codex-feature-that-s-going-viral-right-now_20260603.txt
---

# Run a Genuinely Risky Autonomous Goal on a VPS, Not on Your Own Machine

## TL;DR

An unattended multi-hour run that is allowed to experiment freely should not have your laptop as its blast radius.

## Why it matters

A goal loop earns its keep by trying many things over hours, which is the same property that makes it dangerous: nobody is watching while it experiments, and the scar tissue it leaves (debug prints, hacks, abandoned experiments) is the visible half of what it did. Moving the run to a disposable host makes the worst case a rebuilt VPS rather than your working environment, and it costs one decision made before the run starts.

## How to apply

For any goal run you would not watch, provision a throwaway VPS, clone the repo there, and run it with whatever permissions it needs. Keep secrets out of that host, and pull back only the diff and the notes when it lands. Reserve your own machine for goal runs whose actions you have already bounded.

## Related

[[use-goal-for-unfolding-work-then-redo-it-from-a-distilled-spec]]
