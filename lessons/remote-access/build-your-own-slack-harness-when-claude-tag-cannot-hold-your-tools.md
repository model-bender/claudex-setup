---
id: build-your-own-slack-harness-when-claude-tag-cannot-hold-your-tools
created: 2026-07-25
status: active
supersedes: null
category: remote-access
tool: claude-code
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Build Your Own Slack Bot Harness When Claude Tag Can't Hold the Tools Your Lifecycle Needs

## TL;DR

A custom Slack bot running Claude Code and Codex on a cloud box gives you what the hosted Slack integration can't: extra CLIs, a second model provider, and its own skills, so a two-hour task lifecycle runs in the cloud while your laptop is closed.

## Why it matters

The creator explicitly prefers his own bot over Claude Tag for two concrete reasons. First, a full task lifecycle takes about two hours (build, review, fix loop, verify, PR, recording) and he needs to be able to pack up his computer. Second, his harness needs the LiveKit CLI, Playwright, and Codex for second opinions, none of which the hosted integration lets him install. He notes Stripe (minions) and Shopify (River) run near-identical in-house Slack agents, so this is a shape that survives contact with real engineering orgs. The Slack surface doubles as the review interface: verification recordings and PRs arrive as messages, and you steer with follow-up replies.

## How to apply

Run Claude Code (and Codex) on a cloud host behind a Slack bot that posts as itself. Give the bot skills for the pieces the hosted product can't cover: sending Slack messages, running the verification flow, executing the full task lifecycle, and consulting Codex for a second opinion. Kick work off by messaging it a spec; it returns a PR plus a recording. Reply in-thread to steer, and add "update this yourself so I don't have to remind you next time" when you correct it twice. Reserve this for when you actually need the extra tooling, otherwise the hosted Slack integration is far less to maintain.

## Related

[[encode-the-whole-task-lifecycle-in-claude-md-with-every-stage-in-a-subagent]]
