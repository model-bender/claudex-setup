---
id: slack-thumbs-up-as-approval-gate
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Use a Slack Thumbs-Up Reaction as an Approval Gate Before an Agent Builds a Suggested Feature

## TL;DR

When an autonomous agent proposes a feature from monitored feedback, have it wait for a thumbs-up emoji reaction on its Slack message before starting the build, instead of building automatically or requiring a written reply.

## Why it matters

The presenter's Slack-bot ('Percy') monitors feedback and proposes features that may or may not align with the product vision. The simplest gate he describes is: 'can you react with a thumbs up? If you react with a thumbs up, then I'll start implementing it. If not, then I will just ignore it.'

## How to apply

In the automation's instructions, add a step after any proposed-but-unconfirmed feature: post it to Slack and say a thumbs-up reaction means build it, no reaction (or a different reaction) means skip it, then poll for that reaction before proceeding.

## Related

[[dont-pipe-agent-status-posts-into-team-slack]]
