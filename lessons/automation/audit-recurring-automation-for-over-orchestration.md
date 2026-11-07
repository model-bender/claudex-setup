---
id: audit-recurring-automation-for-over-orchestration
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/master-97-of-codex-in-1-hour-full-course_3TdD8Qv5Tk8_20260626.txt
---

# After a Recurring Automation Runs, Ask It to Find Where It's Over-Orchestrated

## TL;DR

Once an automation is working, ask the agent to review its own run and flag steps that don't need full agentic reasoning, like a routine weekly data refresh that could be a plain script.

## Why it matters

Automations built through conversation tend to route every step through the agent loop even when the task is identical each run, which is slower and pricier than it needs to be.

## How to apply

After a scheduled routine completes, ask 'are there opportunities to streamline this automation, e.g. run it with a script instead of the agent doing every step,' and act on concrete suggestions like adding one repo script for a repetitive builder step.

## Related

[[wat-framework-separate-workflows-agents-tools]], [[measure-refactoring-payoff-in-tokens-with-a-fresh-subagent]]
