---
id: let-model-self-select-subagent-model-then-freeze-routing-table
created: 2026-07-10
status: active
supersedes: null
category: model-selection
sources:
  - transcripts/ray-amjad/cheap-fable-5-ends-this-week-here-s-where-it-actually-matters_B1sYKOWVHR0_20260705.txt
---

# Let the Model Pick Its Own Sub-Agent Model, Then Freeze the Routing Into a CLAUDE.md Table

## TL;DR

Tell the orchestrator 'for all coding tasks, use your own judgment to pick an appropriate low-power model and run it in a sub-agent,' add an eval loop that escalates when a sub-agent's output is too weak, and once it stabilizes crystallize the results into a CLAUDE.md model-routing table and drop the loop.

## Why it matters

Per Simon Willison's write-up of a chat with Cat Wu (Claude Code head of product) and an engineer, stronger models route work better when you let them use their own judgment rather than dictating how they work; the self-calibrating eval loop discovers which model fits which task and codebase area so you stop hand-assigning models per call.

## How to apply

Start with the self-judgment prompt; add 'check that sub-agent's output and if it wasn't good enough, use a more powerful sub-agent next time'; let it build a table of which sub-agent to use for which task and which part of the codebase in CLAUDE.md; then remove the per-call evaluation loop and run with the frozen table until the next model generation ships.
