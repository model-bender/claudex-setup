---
id: tell-the-orchestrator-its-token-price-ratio-instead-of-banning-code
created: 2026-11-15
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1xn0e12/i_tried_to_make_opus_55_cheaper_with_a_cheap/
---

# Tell the orchestrator its tokens cost N times the worker's, instead of banning it from writing code

## TL;DR

In one 12-task benchmark (3 runs each; Opus planning and reviewing, a cheap model coding), stating the price ratio got the same pass rate as an outright "don't write code" ban, at almost half the cost.

## Why it matters

A ban forces delegation even when it costs more, and the orchestrator's cache can expire while it waits on the worker. In the same test, no Opus-led team beat Opus alone (81% at $1.20/task, against 67% at $1.29 with the cheap worker), so delegation is not automatically a saving.

## How to apply

In an orchestration prompt, replace "never write code yourself" with the relative cost ("your tokens cost ~Nx the worker's; delegate when that is cheaper"). Then compare pass rate and cost on a few of your own tasks.

> "How you ask matters. Telling Opus "your tokens cost 20x more than the worker's" instead of banning it from writing code gave the same score at almost half the price.", u/Fabulous_Pollution10 on r/ClaudeAI

## Related

[[delegate-all-execution-off-fable-to-preserve-its-separate-weekly-cap]], [[assign-worker-model-tiers-by-role-in-the-orchestration-prompt]]
