---
id: enumerate-forbidden-actions-when-computer-use-drives-a-live-account
created: 2026-09-12
status: active
supersedes: null
category: permissions
tool: codex
sources:
  - transcripts/mark-kashef/gpt-6-astra-s-computer-use-is-ridiculously-good_tU-fO6cADvQ_20260910.txt
---

# Enumerate the Forbidden Actions When Computer Use Touches a Live Account

## TL;DR

Before turning computer use loose on a real signed-in account, list the actions it must not take (no messages, nothing destructive, settings only) in the prompt itself. On a phone or a consumer app there is no permission layer to fall back on.

## Why it matters

Mark Kashef's Instagram prompt is explicit: 'take control of my Instagram, not send any form of DMs, don't do anything destructive, but go and optimize all of the easy settings that you can.' The reason the prompt has to carry the guardrail is that this class of target has no sandbox: the agent is driving the real account through a mirrored phone, every action is live and public, and there is no approval prompt between it and a sent message. Naming the prohibited actions also narrows what it considers in scope, so it stays in settings instead of improvising engagement.

## How to apply

Write the prohibition list before the goal: no sending or replying, no deleting, no posting, no purchases, no permission changes, settings only. Then state the goal and ask for a checklist of what it changed at the end so you can reverse anything you disagree with. Treat this as the weakest form of containment, use it where an environment boundary genuinely does not exist, and prefer a sandboxed or throwaway account where one does.

## Related

[[contain-agents-at-environment-layer-not-permission-prompts]], [[run-computer-use-agents-inside-a-vm-so-they-stop-stealing-your]]
