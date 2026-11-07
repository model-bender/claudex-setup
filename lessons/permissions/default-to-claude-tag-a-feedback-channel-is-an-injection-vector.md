---
id: default-to-claude-tag-a-feedback-channel-is-an-injection-vector
created: 2026-07-25
status: active
supersedes: null
category: permissions
source_type: post
tool: claude-code
sources:
  - https://simonwillison.net/2026/Jul/21/cat-and-thariq/
---

# Don't Build Your Own AI Slackbot by Default: a Feedback Channel Is an Attacker-Controlled Input

## TL;DR

A Claude Code engineer's explicit build-vs-buy call: a self-hosted Slack agent inherits every prompt-injection vector in your channels, and Claude Tag is worth using specifically because it routes through auto mode and your existing permissions.

## Why it matters

The build case for a custom Slack harness is real, extra CLIs, a second model provider, your own skills, but it is normally argued purely on capability, with the security cost unpriced. Thariq Shihipar names the concrete failure mode: any channel users can post into becomes attacker-controlled input to an agent with your tools. The hosted product has a mitigation (auto mode) that a DIY bot does not get for free.

## How to apply

Default to Claude Tag for Slack-driven agents. Only build your own when a tool the hosted integration genuinely can't hold is worth owning the injection surface for, and if you do, sandbox it, run it on an injection-resistant model with auto mode, and keep it out of channels that accept arbitrary user input. This is the security counterweight to the capability case for a custom harness; both are true, and the security cost is the tiebreaker.

> "This is also the reason Claude Tag is so good — Claude Tag uses auto mode. I've heard a lot of build-versus-buy questions about a Slackbot, and I'm like: please, you probably shouldn't build your own AI Slackbot. There are so many attack vectors. You have a feedback channel that users can post feedback into, and now your bot is reading it.", Thariq Shihipar (via Simon Willison)

## Related

[[build-your-own-slack-harness-when-claude-tag-cannot-hold-your-tools]], [[auto-mode-is-not-injection-containment-isolate-the-session]], [[harden-always-on-agents-least-privilege-and-capable-models]]
