---
id: use-goal-for-unfolding-work-then-redo-it-from-a-distilled-spec
created: 2026-07-17
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/ray-amjad/the-codex-feature-that-s-going-viral-right-now_20260603.txt
---

# Point /goal at Unfolding Work, Then Throw the Branch Away and Rebuild From What It Learned

## TL;DR

Use `/goal` for work whose solution shape you can't predict ("cut P95 checkout latency 20%") rather than pre-decomposable ticket work. Give it the surface it needs to measure itself, and treat the resulting diff as a scrappy spike, distill the lessons into a PRD and re-implement cleanly.

## Why it matters

Well-defined work you can already decompose is better served by a PRD and a task list. The goal loop earns its keep exactly where you *can't* write the plan up front, because it will try many things over hours until something wins.

Two things bite:

- **A goal can only chase a metric it can actually observe.** Without logs or a staging environment it has nothing to converge against.
- **A multi-hour run leaves scar tissue**: debug prints, hacks, abandoned experiments, that Codex doesn't clean up once the goal is met.

Run this way, the goal discovers a spec that couldn't have been written in advance. That spec is its real output, not the diff.

## How to apply

Ask first: do I know what a good solution looks like? If yes, write the PRD and decompose it. If no, set a goal with an observable stopping condition and hand it real resources, logs, a staging or globally distributed cluster, flame graphs, metrics, cost constraints, the codebase.

Brainstorm the goal statement with Codex before firing it: a vague goal ("make this better") runs forever, and a multi-hour run is expensive to get wrong.

When it lands, read the diff for what it learned, write that up as a spec, discard the branch, and re-implement.

Run genuinely risky goals on a VPS rather than your own machine.

Pairs with another lesson, a goal, like a verifier, is only as good as the surface it can act on.

## Related

[[goal-verifiable-finish-lines-with-safety-caps]], [[brainstorm-the-goal-statement-with-the-agent-before-firing-the-run]], [[run-a-genuinely-risky-goal-run-on-a-vps-not-your-own-machine]]
