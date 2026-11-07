---
id: ask-a-peer-session-to-ping-you-when-it-goes-idle-with-notify
created: 2026-08-22
status: active
supersedes: null
category: agents
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Ask a Peer Session to Ping You When It Goes Idle With notify_when_idle Instead of Polling It

## TL;DR

Cross-session SendMessage takes a notify_when_idle flag that makes the other session send exactly one notice when it next goes idle, instead of you polling it for status.

## Why it matters

The usual pattern for "wait for the other session to finish" is a poll loop or repeated "are you done?" messages, both of which burn tokens in both sessions and interrupt the worker mid-turn. This is one-shot and opt-in.

## How to apply

Pass `notify_when_idle` on the cross-session `SendMessage` call to a peer session on the same machine (macOS and Linux only); it fires once, so re-arm it if you need a second checkpoint.

> "Added `notify_when_idle` to cross-session `SendMessage`: ask another Claude Code session on this machine to send one notice when it next goes idle — opt-in, one-shot, no polling (macOS and Linux)", canonical: Claude Code CHANGELOG 2.1.236
