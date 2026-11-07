---
id: spline-exports-are-heavy-budget-for-page-weight
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: [claude-code, claude-design]
sources:
  - transcripts/jono-catliff/claude-code-web-design-10-years-covered-in-66-minutes_2Gda_ZvV1V4_20260701.txt
---

# Budget for ~5MB Page Weight When Embedding a Spline 3D Export

## TL;DR

Spline-exported 3D scenes typically add around 5MB to a page, which will slow load time; only add them if you're prepared to trade that off.

## Why it matters

A beautiful animated hero can quietly tank page-speed scores and mobile load times if the asset weight isn't accounted for up front.

## How to apply

Before asking Claude Code to embed a Spline export (or any similarly heavy 3D/video background), confirm the page-weight tradeoff is acceptable for your target device mix, and prefer lighter effects (CSS gradients, static images) if load time matters more.
