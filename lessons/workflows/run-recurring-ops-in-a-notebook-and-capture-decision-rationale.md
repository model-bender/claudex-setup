---
id: run-recurring-ops-in-a-notebook-and-capture-decision-rationale
created: 2026-08-29
status: active
supersedes: null
category: workflows
source_type: canonical
tool: codex
sources:
  - https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex
---

# Run Recurring Ops Work in a Notebook the Agent Treats as Its Goal, and Capture Decision Rationale Before Wrap-Up

## TL;DR

For repetitive operational tasks (evals, cluster bring-up), put a short goal cell in a shared notebook, have the agent write its plan there and wait for approval, document commands and output as it works, then end every run by recording why choices were made, so each run makes the next one faster.

## Why it matters

The context that would help the next run normally scatters across terminal history and chat scrollback; making the run itself produce the document is what makes documentation cheap enough to happen. A companion index file (Runme writes `*.index.md`) makes past runs discoverable by the next agent.

## How to apply

Start each run with a goal block like "Review a previous run to understand the workflow / Write a detailed plan in this notebook / Wait for me to review and approve the plan before beginning / Document the commands you run, their output, and how you interpret the results", and add an explicit end-of-run decision-capture step.

> "Before wrapping up, I work with Codex to capture decisions that would otherwise disappear into the conversation: why one option was chosen, which approach is now preferred, and what someone should do differently next time.", OpenAI developers blog (Runme write-up)

## Related

[[explicit-numeric-receipts-for-automations]]
