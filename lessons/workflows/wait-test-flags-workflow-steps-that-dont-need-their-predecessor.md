---
id: wait-test-flags-workflow-steps-that-dont-need-their-predecessor
created: 2026-08-29
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/you-re-prompting-claude-wrong-use-this-stanford-method-instead_5nB8Rs4l0_M_20260824.txt
---

# Run the wait test: parallelize any workflow step that doesn't need its predecessor's output

## TL;DR

Walk your skill or workflow step by step and ask of each: does this step actually need the result of the one before it? Every "no" is a false dependency. Restructure those steps to run simultaneously (a fan-out or "diamond" shape) instead of a serial chain.

## Why it matters

People default to chaining steps one after another because it mirrors how they'd do the task by hand, so most Claude skills and automations are slower and more brittle than they need to be: each step waits on a predecessor whose output it never reads, and one broken step kills the whole run. The transcript's example is a research-report workflow where "research YouTube" and "research Google" ran serially; neither consumed the other's output, so running them as parallel subagents roughly halved wall-clock time while "create report" correctly stayed downstream of both. The test gives you a mechanical, per-edge audit rather than a vague instinct to "parallelize more".

## How to apply

Take an existing skill or workflow and step through it: at each step ask "does this need the result of the previous step?". If yes, keep the sequential edge; if no, mark it and have Claude restructure those steps to fan out simultaneously and feed a downstream join step (the transcript calls this the diamond shape, implemented via subagents). The creator also runs a periodic audit prompt over his whole system that flags every step that is waiting on something it doesn't need. Apply the same test before fanning out: a step that secretly depends on a sibling's output fails the wait test and should stay serial.

## Related

[[fan-out-subagent-steps-fail-silently-reserve-them-for-cheap-errors]], [[subagents-for-noisy-tool-calls-not-large-edits]]
