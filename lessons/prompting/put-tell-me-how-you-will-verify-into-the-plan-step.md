---
id: put-tell-me-how-you-will-verify-into-the-plan-step
created: 2026-10-11
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/austin-marchese/7-claude-hacks-that-feel-illegal-and-3-to-avoid_hsbr0IoFZJ8_20261009.txt
---

# Ask for the Verification Method as Part of the Plan on Technical Tasks

## TL;DR

Austin tells the agent 'Tell me how you'll verify the output as part of the plan' so it knows the target finished product.

## Why it matters

Default verification is generic; stating the check up front makes him more confident it understands what done looks like.

## How to apply

Use plan mode (/plan) and add that sentence to the planning prompt; for non-technical work define the output structure ahead of time, as in his script outline skill.

Checked: '/plan' appears 18 times in installed Claude Code 2.1.296 binary (command grep -c -a)

## Related

[[prompt-with-the-goal-the-effort-and-how-to-verify]]
