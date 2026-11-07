---
id: pure-delegator-orchestrator-preserves-context-across-a-long-session
created: 2026-08-07
status: active
supersedes: null
category: agents
tool: claude-code
about: null
sources:
  - transcripts/nate-herk-ai-automation/i-tested-opus-5-vs-fable-5-what-you-need-to-know_2J3uX8iRNng_20260807.txt
---

# Tell an Orchestrator Model to Never Write or Execute Code Itself So It Can Run All Day

## TL;DR

When one model's job is to plan and delegate rather than implement, explicitly forbid it from writing or running code, every token it spends executing is a token it can't spend orchestrating, and a pure delegator can stay well under its context ceiling for a multi-hour or full-day session.

## Why it matters

A long-lived orchestrator that also does hands-on work (editing files, running commands) burns through context fast, forcing resets that lose the big picture. Keeping it to reasoning and delegation only, reading results, deciding next steps, spinning up sub-agents or a cheaper execution model for the actual work, lets it run for hours without approaching its context limit, since delegation output is tiny compared to implementation output.

## How to apply

When assigning a model the coordinator/orchestrator role in a multi-agent setup, state the constraint directly: "you should not be writing any code or executing anything yourself, only tell [the executor] what to do." Route the actual file edits and command execution to sub-agents or a separate execution-focused model, and reserve the orchestrator's context budget for tracking state and making decisions across the whole session.

## Related

[[route-long-projects-to-fable-and-single-prs-to-opus-5-medium]], [[give-orchestrator-broad-goals-not-narrow-checklists]]
