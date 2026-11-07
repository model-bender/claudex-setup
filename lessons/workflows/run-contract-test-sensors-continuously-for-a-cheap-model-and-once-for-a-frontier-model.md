---
id: run-contract-test-sensors-continuously-for-a-cheap-model-and-once-for-a-frontier-model
created: 2026-10-19
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
source_type: post
sources:
  - https://martinfowler.com/articles/are-harnesses-worth-the-cost.html
---

# Run Contract-Test Sensors During Development for a Cheaper Model, but Only Once as a Final Gate for a Frontier Model

## TL;DR

In a 10-run Codex experiment, machine-readable API contracts plus contract tests took a cost-optimized model from 3 of 10 to 10 of 10 accepted runs, while for a frontier model the same harness added cost with no gain.

## Why it matters

The harnessed cheap model reached the frontier model's reliability at lower cost per run, so the sensors are worth running continuously there. For the frontier model they belong at the end as an acceptance check, not inside the loop.

## How to apply

For a cheaper model, give the agent the API specs, request and response examples and a contract-test tool it must run while it works. For a frontier model, run the same checks once after it finishes and accept nothing without a green result. The author's caveat: one greenfield Java service with an unusually detailed brief. Checked: no Claude Code or Codex flag named.

> "What changes with model capability is not whether independent sensors are needed, but when they run.", Naresh Jain (Thoughtworks, Exploring Gen AI)

## Related

[[bookend-each-work-item-with-the-strongest-model]], [[design-agent-output-for-verifiability-before-building-evals]]
