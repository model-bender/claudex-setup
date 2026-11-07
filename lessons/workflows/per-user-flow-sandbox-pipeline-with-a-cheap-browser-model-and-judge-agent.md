---
id: per-user-flow-sandbox-pipeline-with-a-cheap-browser-model-and-judge-agent
created: 2026-08-07
status: active
supersedes: null
category: workflows
tool:
  - claude-code
  - codex
about: null
sources:
  - transcripts/ray-amjad/openai-made-a-new-kinda-of-ai-coding-possible__eCtUVds3wA_20260807.txt
---

# Verify Every New User Flow After a PR With an Isolated Sandbox, a Cheap Browser Model, and a Judge Agent

## TL;DR

After a PR, have an agent enumerate the user flows it just introduced or changed, then run each through its own throwaway sandbox (own DB) with three roles: one agent seeds the data, a cheap browser-driving model clicks through the flow and records it, and a judge agent grades whether the recording proves it works, retry the sandbox on failure, log to markdown on success.

## Why it matters

Generating code has gotten easy; reliably verifying it is now the bottleneck (the "verification horizon" problem). Self-review by the agent that wrote the change is a conflict of interest, and running everything in one shared environment means parallel checks corrupt each other's state. Splitting seed/drive/judge into separate agents removes the self-grading bias, and per-flow sandboxes let dozens of checks run in parallel without interference. The browser-driving step doesn't need a premium model: on a 106-task browser-use benchmark, GPT-5.6 Luna at extra-high reasoning scored within 2 points of Opus 5 (70% vs 72%) at roughly 1/17th the cost (~$0.14/task vs Opus), so routing that specific step to a cheap model cuts verification cost by an order of magnitude without a meaningful accuracy loss.

## How to apply

1. On each PR, have an agent diff the change and list the new or altered user flows (the concrete click-paths a real user would take).
2. For each flow, spin up an isolated sandbox with its own database/cache so it can be seeded into whatever state the flow needs without touching other checks.
3. Agent 1 seeds that sandbox's data; agent 2 drives Playwright (a cheap high-accuracy browser-use model is enough for this step) through the flow and records the session; agent 3 (the judge) reviews the recording and decides pass/fail against the stated flow.
4. On failure, retrigger the sandbox rather than trusting a partial run; on success, write the result to a markdown log so you accumulate a growing regression suite.
5. Before wiring up a flow that needs an external surface (Slack, WhatsApp, a phone call), check the sandbox actually has that capability, ask the agent what access it needs to verify the flow rather than assuming.
6. Prefer cloud sandboxes over your local machine for long-running verification agents to keep the checks isolated and parallelizable.

## Related

[[separate-evaluator-agent-exercises-the-running-app]], [[drive-playwright-for-browser-automation-and-authed-scraping]], [[triage-with-a-cheap-model-before-expensive-work]]
