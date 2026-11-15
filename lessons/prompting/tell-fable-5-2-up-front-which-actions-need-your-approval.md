---
id: tell-fable-5-2-up-front-which-actions-need-your-approval
created: 2026-11-15
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://x.com/alexalbert__/status/2119869724247077229
---

# Tell Fable 5.2 Up Front Which Actions Need Your Approval and That the Rest Is Its Call

## TL;DR

In the first prompt, name the few actions that require your sign-off (for example deletions) and say everything else is the model's decision.

## Why it matters

It removes the stop-and-ask turns on routine steps while keeping a human gate on the destructive ones, which is what lets a long run go unattended.

## How to apply

Add one line to the kickoff prompt or project instructions: "Ask me before deleting or overwriting anything; for everything else, decide yourself." Pairs with a permission mode or allowlist for the hard gate.

> "Tell it up front what needs your approval (e.g. deleting things) and that the rest is its call", Alex Albert (Anthropic) on X
