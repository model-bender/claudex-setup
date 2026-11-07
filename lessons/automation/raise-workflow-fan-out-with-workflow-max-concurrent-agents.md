---
id: raise-workflow-fan-out-with-workflow-max-concurrent-agents
created: 2026-09-13
status: active
supersedes: null
category: automation
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Raise the Workflow Fan-Out Cap Only When the Bottleneck Is Inference, Not the Machine

## TL;DR

`CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (1 to 256) lifts the Workflow tool's per-run concurrent agent limit for fan-outs waiting on model inference.

## Why it matters

The ceiling worth raising and the ceiling that crashes your session are different ceilings. This one helps when agents sit idle waiting for responses; it does nothing for a fan-out already bound by local memory, where roughly 6 or more parallel subagents can exhaust the machine.

## How to apply

Set `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS=<1-256>` before a Workflow run whose agents are blocked on model responses. Leave it alone for locally bound work and keep running waves instead. Verified present in the installed 2.1.270 binary (3 occurrences).

> "Added `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (1–256) to raise the Workflow tool's per-run concurrent agent limit for inference-bound fan-outs", Claude Code CHANGELOG 2.1.269
