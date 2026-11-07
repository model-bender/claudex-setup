---
id: default-to-a-deterministic-script-reserve-the-agent-sdk-for-unbounded-loops
created: 2026-09-24
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/how-to-build-gpt-6-astra-automations-that-don-t-eat-your-usage-limit_FqnNL8fnUWo_20260920.txt
---

# Default an Externally-Hosted Automation to a Deterministic Script, Reserve the Agent SDK for Genuinely Unbounded Tasks

## TL;DR

Most automations are a fixed sequence of steps with AI needed at only one or two of them, build those as a script that calls AI just at those points. Only reach for a full agent-SDK-hosted loop when the task needs actual unbounded iteration (check logs, decide whether to research more, loop back); the SDK route is billed per API credit and costs more than a subscription.

## Why it matters

A full agentic loop gives an automation the freedom to keep going back and forth indefinitely, which is exactly what some tasks need and exactly what most don't. Reaching for it by default means paying API-credit rates for work a fixed script could have done deterministically and more cheaply, and gives the automation more room to behave unpredictably than the task requires.

## How to apply

Before building, map the automation's steps and mark which ones are genuinely non-deterministic (need judgment, produce a different result each run). If the flow is a fixed sequence with AI needed at only a couple of those steps, have Codex build it as a script that calls the model just there. When the task does need to loop back on itself an unknown number of times, the default is still the subscription: run it as a Codex scheduled task. Move to a Codex-SDK-hosted loop only when it must run programmatically and at scale, and expect API-credit rates rather than subscription rates for it.

## Related

[[ask-the-wrong-primitive-question-before-building-a-skill]], [[host-recurring-codex-automations-externally-not-as-scheduled-tasks]]
