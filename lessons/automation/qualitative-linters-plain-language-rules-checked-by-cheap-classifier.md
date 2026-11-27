---
id: qualitative-linters-plain-language-rules-checked-by-cheap-classifier
created: 2026-11-22
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/ray-amjad/jev-claude-code-the-cheapest-agentic-coding-loop-yet_ScvXFi4MUSc_20260920.txt
---

# Write qualitative lint rules as plain-language questions and have a cheap classifier run them on every PR

## TL;DR

For rules a conventional linter cannot express, write the rule as a question (for example 'does the name describe everything this function does, including the side effects?') and have a fast, cheap classifier answer it for each unit of code on every PR. This is a proposed, untested pattern: the speaker describes it as now possible but does not build or run it in the video.

## Why it matters

The speaker's argument is that long hand-written linter code misses cases and breaks on complicated code, while a fast, cheap and fairly smart classifier can apply a judgement-style rule cheaply enough to run on every single PR. What he did run was a one-off pass over a codebase's comments (150 comments in 9.3 seconds for about 1 cent); the per-PR linter is his extrapolation from that, so cost and reliability as a PR gate are unproven.

## How to apply

List the judgement rules you care about as yes or no (or categorical) questions, have your coding agent wire them into a script that sends each function or log line to the classifier, and fail or warn the PR based on the returned probability.

Checked: No Claude Code mechanism named (workflow). Jev is a third-party classifier model (from TypeSafe AI) with its own API and skill; it has no page in the Claude Code docs index (fetched 2026-11-22) and no readable mention in the 2.1.330 binary, so its speed and price figures are the transcript's and were not verified.

## Related

[[move-repeated-review-comments-into-review-md]], [[route-bulk-classification-to-a-cheap-judgment-model]]
