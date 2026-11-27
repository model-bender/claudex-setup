---
id: plan-feature-gates-and-isolate-integration-before-agents-code
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/john-kim/how-i-review-ai-code-meta-senior-staff-engineer_b2QkhmQ0sT0_20260923.txt
---

# Plan the feature gate and the integration seam before the agent writes code

## TL;DR

At planning time, put the whole new feature behind a gate and split the work into leaf pieces that touch no existing code plus a separately gated integration layer.

## Why it matters

Code that is isolated or fully gated off can land fast with light review, because it cannot change production behaviour and can be switched off. The speaker ties how much he reviews directly to whether he can roll the change back, and says that depends on feature gating. Integration points are where existing behaviour changes, so they get their own gate and the careful review.

## How to apply

In the plan or spec you give the agent, state: the gate that wraps the feature (a plain Boolean flag in the codebase is enough to start; the speaker names LaunchDarkly as a fuller option), which pieces are new leaf code that touches nothing existing, and which pieces are integration into existing code, each behind the gate. Only once that plan and the gating are ready, let agents build the code out as atomic changes.

Checked: No mechanism named (LaunchDarkly is a third-party product named by the speaker, not checked).

