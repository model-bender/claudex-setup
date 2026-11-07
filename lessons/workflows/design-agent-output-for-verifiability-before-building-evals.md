---
id: design-agent-output-for-verifiability-before-building-evals
created: 2026-07-17
status: active
supersedes: null
category: workflows
source_type: post
sources:
  - https://hamel.dev/blog/posts/eval-smell/
---

# Design the Agent's Output to Be Verifiable Before You Build Evals

## TL;DR

When an agent's output is painful to verify, treat "hard to eval" as a design smell, redesign the artifact so correctness is confirmable at a glance before you jump to writing evals.

## Why it matters

Artifacts that are hard for you to verify are usually hard for users too, and hard-to-check agent work forces you to redo it from scratch to trust it. Making the output self-verifiable is upstream of eval-building: it's cheaper, and it's the thing that lets you actually accept the agent's work.

## How to apply

Before building evals for an AI feature (or accepting a Claude Code change), make the output self-verifiable, have the agent emit a short screen recording/GIF of the change, a before/after data diff, a runnable demo, or explicit screenshots, so you confirm the work at a glance instead of reproducing it by hand.

> "Cursor and Devin both record a short video of the UI changes they make, so you can confirm the work is right without reproducing it yourself.", Hamel Husain

## Related

[[error-analysis-before-llm-judge-no-blanket-score]], [[shift-verification-to-the-cheapest-rung]]
