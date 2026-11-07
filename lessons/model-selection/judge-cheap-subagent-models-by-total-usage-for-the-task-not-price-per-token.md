---
id: judge-cheap-subagent-models-by-total-usage-for-the-task-not-price-per-token
created: 2026-10-25
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/simon-scrapes/5-claude-tips-everyone-recommends-but-shouldn-t_v9YVQoeSp-I_20261022.txt
---

# Before Moving Explore Subagents to Haiku, Run the Same Task Both Ways and Compare Total Usage

## TL;DR

A model that is far cheaper per token can cost more per finished job if its wrong answers go back to the main model for fix rounds. Measure total usage and time for one real task on each setup before committing.

## Why it matters

Simon cites a Reddit user who moved subagents to the cheap model and went back to Opus for everything because tasks needed two to three fix rounds, using more tokens and time. The saving per word was outweighed by checking and rework.

## How to apply

Pick one representative task. Run it once with the cheap model on your explore subagents and once with your main model. Compare total usage and elapsed time at the end, not the per-token price, and include your own checking time. Keep the cheap routing only if the whole job comes out cheaper. Checked: n/a (a measurement method). The transcript's benchmark scores and the '40 times cheaper' figure are the creator's and were not verified; they are not used in the lesson. The Reddit anecdote is single-source.

## Related

[[stop-comparing-models-on-dollars-per-million-tokens-tokenizers]], [[explore-subagents-run-on-your-main-model-route-cheap-search-to-your-own-haiku-agent]]
