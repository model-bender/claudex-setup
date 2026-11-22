---
id: test-a-verification-gate-with-a-do-nothing-run-and-a-known-bad-output
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
source_type: post
sources:
  - https://eugeneyan.com/writing/public-evals
---

# Test a Verification Gate With a Do-Nothing Run and a Known-Bad Output Before Trusting Its Green

## TL;DR

Before you let an agent loop against a test or check script, prove the check fails on an empty change and on a known-bad change.

## Why it matters

A check that passes wrong work lets an agent loop report success. Eugene found graders passing wrong or hallucinated work in several public evals because nobody scrutinised passing runs, and Terminal Bench guards against it with a do-nothing agent and an adversarial agent.

## How to apply

Run the gate once against an untouched checkout (it must fail) and once against a deliberately broken change (it must fail), and only then point /goal, a loop or a subagent at it as the finish line.

Checked: no mechanism claim (practice drawn from the post's account of Terminal Bench and a general eval-grader principle)

> "Evals need negative tests to verify that known-bad outputs are rejected.", Eugene Yan

## Related

[[goal-verifiable-finish-lines-with-safety-caps]]
