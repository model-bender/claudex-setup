---
id: write-acceptance-criteria-as-when-then-pairs-to-judge-an-unattended-build
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/sean-kochel/why-your-agentic-workflows-don-t-work_ILKrUq_8aC4_20260820.txt
---

# Write Spec Acceptance Criteria as When-This-Happens-Then-That Pairs, They Are What Judges a Long Unattended Build

## TL;DR

Per-behaviour criteria in when-then form are the only thing that lets you decide whether a fifteen-hour unattended run actually delivered, so write them before the run rather than reconstructing a standard afterwards.

## Why it matters

A long autonomous build hands you a diff and a confident summary, and without a written standard your review degrades into spot-checking whatever you happen to open. When-then pairs are checkable one at a time and by someone other than the author, including the agent itself, which turns the judgement into a pass or fail per behaviour instead of an overall impression. The parent lesson names the proposal as the most important artifact and the spec's role gets one clause in its body.

## How to apply

For each behaviour in the feature, write the trigger and the expected result as a pair: when a user submits an expired token, then the request is rejected with a 401 and the session is cleared. Keep them in the repo next to the plan, hand them to the run as its definition of done, and walk them as the review checklist when it finishes. Distinguish them from the design document, which answers what the system is, and the proposal, which answers why.

## Related

[[write-a-proposal-artifact-the-model-can-be-sent-back-to]]
