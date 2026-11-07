---
id: fan-out-subagent-steps-fail-silently-reserve-them-for-cheap-errors
created: 2026-08-29
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/austin-marchese/you-re-prompting-claude-wrong-use-this-stanford-method-instead_5nB8Rs4l0_M_20260824.txt
---

# Fanned-out subagents fail silently, so reserve fan-outs for steps where one worker's failure is cheap

## TL;DR

Unlike a serial chain, where any broken step halts the run visibly, a fan-out keeps going when one subagent fails, so you may never notice the gap. Fan out only steps where a single worker's silent failure won't ruin the result, and start new workflows as chains before parallelizing.

## Why it matters

The transcript names two failure modes specific to the fan-out ("diamond") shape: false independence (each subagent has its own context and doesn't know what siblings are doing, so two agents duplicate work or miss context that was actually shared, burning tokens) and silent failures, where the graph "won't break if one of the subagents fails", making it much harder to know when and what broke versus a chain where any issue becomes obvious. This is the counterweight to the parallelize-everything instinct: the debuggability you lose is real.

## How to apply

Choose fan-out tasks where the cost of an individual error is low (e.g. multi-source research, per-angle review passes like a security audit) rather than tasks where one missing branch corrupts the deliverable. Verify genuine independence with the wait test before splitting. And start almost every new workflow as a plain sequential chain first: it is the easiest shape to test and experiment with, and failures surface immediately. Then convert the proven steps to parallel once behavior is understood.

## Related

[[wait-test-flags-workflow-steps-that-dont-need-their-predecessor]], [[pair-worker-subagents-with-observer-watchdog-agents]], [[agent-teams-agent-should-not-touch-same-files]]
