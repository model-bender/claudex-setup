---
id: assign-worker-model-tiers-by-role-in-the-orchestration-prompt
created: 2026-09-12
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-had-fable-5-1-and-5-build-me-the-same-app_5FukkI4fbiU_20260910.txt
---

# Name Which Model Tier Handles Which Worker Role in the Orchestration Prompt

## TL;DR

Do not just tell the orchestrator to delegate, tell it which tier gets which kind of work: the stronger model for architecture, product and design direction, hard problems and independent reviews, the cheaper one for implementation, research, testing, debugging and iteration.

## Why it matters

Nate Herk put exactly that split in one long orchestration prompt and the post-run breakdown shows it was obeyed: the orchestrator itself was about 3% of tokens, Opus workers 57%, Sonnet workers 40%. The same prompt given to the other model produced 80% Sonnet and a visibly cheaper, slightly weaker result at roughly half the cost and a third of the time. The point is not which model won, it is that the worker mix is the cost and quality dial, and if you leave the mapping to the orchestrator's judgement it varies run to run, so you cannot tell a model difference from a routing difference.

## How to apply

In the first prompt, after the delegation constraint, write the mapping explicitly: 'primarily use Opus workers for architecture, product and design direction, difficult problem solving and independent reviews, primarily use Sonnet workers for implementation, research, testing, debugging and iteration.' Add the accountability clauses that make it act on weak output: 'give workers clear ownership, prevent conflicting edits, replace or redirect workers when results are weak, worker failure is still your responsibility.' Check the per-model usage breakdown afterwards to confirm the split you asked for is the split you got.

## Related

[[delegate-all-execution-off-fable-to-preserve-its-separate-weekly-cap]], [[pure-delegator-orchestrator-preserves-context-across-a-long-session]], [[check-the-per-model-usage-breakdown-after-a-long-autonomous-run]]
