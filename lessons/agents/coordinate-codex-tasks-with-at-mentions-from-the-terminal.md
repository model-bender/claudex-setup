---
id: coordinate-codex-tasks-with-at-mentions-from-the-terminal
created: 2026-08-29
status: active
supersedes: null
category: agents
source_type: canonical
tool: codex
sources:
  - https://developers.openai.com/codex/changelog
---

# Coordinate Codex Tasks by @-Mentioning Other Tasks Instead of Pasting Context Between Them

## TL;DR

Codex CLI 0.150.0 makes tasks first-class objects: @-mention another task in the composer, and instruct an agent to read, create, or message tasks itself.

## Why it matters

The director-thread pattern (one thread triaging others) previously required manual copy-paste of context between threads; now the coordinating agent can pull another task's state directly, and orchestration prompts can say "read task X, then message it".

## How to apply

In the 0.150+ TUI composer, type `@` to reference a task; in prompts, ask the agent to use the task tools to read, create, or message other tasks.

> "Reference other Codex tasks with @ mentions, and ask agents to read, create, or message tasks from the terminal.", Codex changelog, CLI 0.150.0

