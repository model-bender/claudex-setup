---
id: route-bulk-classification-to-a-cheap-judgment-model
created: 2026-09-24
status: active
supersedes: null
category: model-selection
tool: claude-code
about: jev
sources:
  - transcripts/ray-amjad/jev-claude-code-the-cheapest-agentic-coding-loop-yet_ScvXFi4MUSc_20260920.txt
  - transcripts/simon-scrapes/every-jev-concept-explained-use-with-claude_D-Z5HnLW_ho_20260923.txt
---

# Delegate bulk deterministic classification to a fast judgment model, not to Claude directly

## TL;DR

For triaging large batches of records against fixed criteria (support emails, leads, code comments, PR diffs), have Claude Code write and run a script that calls a fast, cheap judgment-model classifier for the classification/routing/scoring step, and reserve Claude itself for the confidently-flagged subset that actually needs writing or judgment.

## Why it matters

Demonstrated twice with real numbers. In one video, 150 code comments were classified in 9.3 seconds for about 1 cent, with an estimate of about 57 cents to analyse every comment in the codebase and a shortlist of about 1,700 worth rewriting. In the other, 50 support emails were triaged in 4.2 seconds with eight concurrent workers (31 seconds sequentially) for $0.026. The architecture point generalizes beyond the specific classifier product: use the agentic coding tool to write and own the calling code, not to read every row itself.

## How to apply

Ask Claude Code to write a script that sends each record to a fast, cheap classifier with your fixed criteria, runs the calls concurrently, and writes the results to a file; then have Claude work only on the subset the classifier flags. Unverifiable here: the classifier in both videos is a third-party waitlisted product, and the cost and latency figures are the creators' own.
