---
id: war-game-plans-with-strongest-model-for-cheaper-executor
created: 2026-07-10
status: active
supersedes: null
category: workflows
sources:
  - transcripts/mark-kashef/do-this-before-you-lose-access-to-fable-5_nuwlyQXrADg_20260705.txt
---

# War-Game the Plan: Have Your Strongest Model Pre-Simulate Failure Paths for a Cheaper Executor

## TL;DR

Instead of a linear plan, ask your most capable model to 'war-game' the task - for each move write the expected success signal, the most likely failure plus its cause/signals, the counter-move, decision forks ('if you observe X, take route Y'), unresolved assumptions to flag, and abort conditions - and save it to a file a cheaper model then executes.

## Why it matters

A normal plan assumes a blue-sky linear path, so when reality throws errors the executor flounders and burns tokens rediscovering them. Pre-simulating action->reaction->counteraction captures the expensive model's failure-mode intuition as a durable artifact, so a cheaper model (or a future model) executes confidently - and it lets you bank a top-tier model's value before you lose subscription access to it. You're bottlenecked by unknown-unknowns, not raw intelligence, and this surfaces them.

## How to apply

Prompt: 'You are war-gaming this mission, not executing it; a cheaper model will run it. Fight it move by move: each move states its expected observation on success, its most likely failure + cause + signals + counter-move, and forks. Flag assumptions you could not resolve. End with abort conditions.' Write each to a war-games/*.md file alongside a success-criteria file and a ledger file that records blocked/undefined variables as placeholders. Fan out across many task files with /goal + /loop, drafting all before polishing. Optionally tag the Claude Code Guide subagent to tailor the war-game to the exact executor model's documented behavior.
