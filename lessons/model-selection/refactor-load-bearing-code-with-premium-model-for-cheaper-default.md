---
id: refactor-load-bearing-code-with-premium-model-for-cheaper-default
created: 2026-07-10
status: active
supersedes: null
category: model-selection
sources:
  - transcripts/ray-amjad/cheap-fable-5-ends-this-week-here-s-where-it-actually-matters_B1sYKOWVHR0_20260705.txt
---

# Have the Premium Model Refactor Load-Bearing Code So Your Cheap Default Model Handles the Rest

## TL;DR

When you briefly have a stronger model, don't just have it clear the backlog - have it make architectural changes to the load-bearing / highest-churn files specifically so a weaker default model can close issues more easily afterward.

## Why it matters

A stronger model (Fable 5) sees 4th-6th-order effects and makes better architectural calls; spending that on the substrate permanently raises the floor for the cheaper model (Opus 4.8) you fall back to, and coding agents copy whatever patterns already exist - so improving the load-bearing code pays off on every later run instead of evaporating when the premium model does.

## How to apply

Rank files by git churn x complexity to find tech-debt hotspots, then prompt the strong model 'look through the backlog and make architectural changes that would make it easier for a less powerful model to close these issues' (or 'what architectural fixes reduce complexity in the top 2 files, in light of the backlog'); apply the same move to shared logic (e.g. build a Rust shared-core once for four app targets).
