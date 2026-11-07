---
id: minimum-viable-model-year-ago-test
created: 2026-07-25
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/austin-marchese/17-tricks-to-build-10x-faster-with-claude_ZzHB2mPHb2g_20260724.txt
  - transcripts/austin-marchese/paste-this-into-claude-never-hit-a-token-limit-again_SFh6MMe-XcM_20260719.txt
---

# Route by Minimum Viable Model: "Could a Model From a Year Ago Do This?"

## TL;DR

Budget consumed is roughly tokens consumed × model cost, so the cheapest lever on a subscription is model choice per task. The decision rule is a single question: if an AI from a year or two ago could have done this task, it does not need a frontier model.

## Why it matters

The creator traced his limit-hitting to subagent fan-out on his default model, every parallel worker inherits the session model unless told otherwise, so cost multiplies by fan-out width and a wide fan-out on a frontier model drains a window fast. The year-ago test is a fast, memorable filter that puts scraping, summarizing, formatting, file fetching, and resource verification firmly in cheap-model territory, where output quality is indistinguishable but spend is an order of magnitude lower. It beats a case-by-case judgment call because you can apply it in a second, across a whole skill library.

## How to apply

For each skill and subagent, apply the year-ago test and pin the resulting model in frontmatter rather than leaving it to inherit the session's. Pair it with the context decision: if the task needs no prior conversation, also fork context so it starts clean, a resource-verifier skill becomes `model: haiku` plus a forked context. Bias the whole table cheaper if you hit limits often, richer if you rarely do. To bootstrap, have Claude audit your skill library and propose a model per skill as a starting table, then correct it where output actually degrades.

## Related

[[let-model-self-select-subagent-model-then-freeze-routing-table]], [[model-selection-opus-sonnet-haiku-use-cases]], [[triage-with-a-cheap-model-before-expensive-work]]
