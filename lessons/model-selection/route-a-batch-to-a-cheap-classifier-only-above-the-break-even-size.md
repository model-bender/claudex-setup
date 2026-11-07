---
id: route-a-batch-to-a-cheap-classifier-only-above-the-break-even-size
created: 2026-10-25
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xbxoza/my_claude_code_setup_it_runs_like_a_small/
---

# Route a Batch of Judgments to a Cheap Classifier Only Above the Break-Even Size

## TL;DR

Each tool round trip to a cheap judgment model re-sends the orchestrator's context, so on a small batch offloading costs more of the expensive model than reading the items directly; the poster's break-even was about 45 to 60 issues.

## Why it matters

"Delegate bulk classification to a cheap model" saves tokens only past a batch size. The poster measured a 14-issue backlog costing more Opus tokens through the classifier than without it, and 267 issues dropping Opus usage from 9.5M to 1.7M tokens.

## How to apply

Estimate the item text first and send a pile through the cheap classifier only above roughly 15 to 20k tokens of item bodies (the poster's figure). Make it one tool call that reads the files on the server side and returns a short accept, look or decide table, and have the orchestrator read only the decide rows. These are one person's measurements.

> "Each extra round trip resends 60-75k tokens of context to the orchestrator.", u/aaraujo666 on r/ClaudeCode

## Related

[[route-bulk-classification-to-a-cheap-judgment-model]]
