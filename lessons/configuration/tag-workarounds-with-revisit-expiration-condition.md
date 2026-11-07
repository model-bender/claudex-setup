---
id: tag-workarounds-with-revisit-expiration-condition
created: 2026-07-10
status: active
supersedes: null
category: configuration
sources:
  - transcripts/ray-amjad/cheap-fable-5-ends-this-week-here-s-where-it-actually-matters_B1sYKOWVHR0_20260705.txt
---

# Tag Every Workaround in CLAUDE.md and Skills With a Revisit/Expiration Condition

## TL;DR

Add a 'revisit if / expires when' tag to every workaround you bake into CLAUDE.md and skills, so stale hacks get re-evaluated on the stated trigger instead of silently persisting long after the underlying problem is gone.

## Why it matters

Workarounds accumulate and quietly outlive their reason (a model limitation a newer model fixed, an upstream bug since patched); with no explicit revisit condition they never get reconsidered and start constraining a model that no longer needs them - nothing 'declassifies' itself.

## How to apply

When you write a workaround, append its revisit condition (e.g. 'revisit if on a model newer than X', 'remove once upstream bug Y is fixed'); periodically, or on every model upgrade, sweep for these tags and re-test whether each is still needed. (Ray Amjad surfaced this from running a 'bitter lesson' overengineering audit of his agent harness with Fable 5.)
