---
id: done-when-prompt-scaffold-for-codex
created: 2026-07-17
status: active
supersedes: null
category: prompting
tool: codex
sources:
  - transcripts/john-kim/complete-beginner-s-guide-to-openai-s-codex-app_20260424.txt
---

# Write Codex Prompts as Goal, Context, Constraints, Done When

## TL;DR

Codex's documented prompt shape has four parts, and the load-bearing one is the last: `done when` is the keyword that hands the agent its validation criteria, so it can check and heal its own work instead of declaring victory.

## Why it matters

The first three parts are what everyone writes anyway. The fourth is the one people skip, and it's the one that changes behaviour, giving an agent explicit validation criteria improves output quality and self-correction dramatically, because "done" stops being a judgement call.

Not stating how the agent should know it's correct is one of the most common Codex mistakes, and it's invisible: you get a confident completion claim with nothing behind it.

## How to apply

Structure the prompt as:

- **goal**: what you're trying to do
- **context**: relevant files and folders (natural language usually beats @-tagging unless you know exactly where things live)
- **constraints**: framework, architecture, anything not apparent from the code
- **done when**: the observable test

Start in plan mode (shift+tab) and let the four parts shape the plan before any execution.

Constraints you find yourself repeating belong in `AGENTS.md` instead, repetition is the signal.

## Related

[[goal-verifiable-finish-lines-with-safety-caps]], [[move-repeated-prompt-constraints-into-agents-md]]
