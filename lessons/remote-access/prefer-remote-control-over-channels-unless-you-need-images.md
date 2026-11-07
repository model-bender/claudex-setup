---
id: prefer-remote-control-over-channels-unless-you-need-images
created: 2026-09-01
status: active
supersedes: null
category: remote-access
tool: claude-code
sources:
  - transcripts/john-kim/new-claude-code-updates-are-so-cool_20260424.txt
---

# Prefer Remote Control Over Discord/Telegram Channels Unless You Specifically Need Images

## TL;DR

Claude Code's Channels feature (Discord/Telegram messaging) is experimental and adds setup complexity mainly justified by one benefit over Remote Control: the ability to receive images back in the reply.

Controlling a Claude Code session remotely from phone or web has no way to send images back to you, and it's hard to verify results on the spot, so it's best suited to research-heavy work or tasks you're comfortable reviewing after the fact rather than anything needing visual confirmation.

## Why it matters

For most phone/remote use cases, Remote Control already gives full session control with less setup; Channels' main edge is image replies, which most tasks don't need, and it remains in experimental mode.

The lack of an image channel back to the remote client means you can't verify UI or visual output live; using Remote Control for such work means flying blind until you're back at the original machine.

## How to apply

Default to Remote Control for controlling Claude Code away from your machine. Only set up a Discord/Telegram Channel if you specifically need the bot to send images back, and expect it to require more configuration.

Use Remote Control for read-heavy, research-based, or 'mostly vibed' tasks you'll check the results of later. For anything requiring visual verification (screenshots, rendered UI), do it from the primary machine instead, or plan to review it there afterward.

## Related

[[discord-vs-telegram-channel-persistence-and-accept-edits-default]], [[remote-control-channels-for-phone-access]]
