---
id: build-a-cache-countdown-mod-with-one-click-handoff
created: 2026-10-11
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-code-mods-are-game-changers-set-up-these-5-now_9hetShMMp2s_20261009.txt
---

# Build a mod that shows the prompt-cache countdown and offers handoff before it expires

## TL;DR

A desktop mod can show the cache timer, context size and what a cold cache would cost, warn when the cache is about to go cold, and run your handoff skill plus /clear in two clicks.

## Why it matters

Nate says everything in the chat is cached so new messages are not re-read at full cost, and after 60 minutes without a message the whole session must be paid for again. His mod makes that visible and nudges him to reprompt, compact or hand off before the cache goes cold.

## How to apply

Ask Claude to build a mod that (1) shows minutes left on the cache, context tokens, session and weekly limits and the would-be API cost, (2) sends a notification when the cache is about to expire (his example: 5 minutes left) offering reprompt, compact or handoff, and (3) has a button that runs your session-handoff skill, then a 'clear and continue' button that runs /clear and pastes the handoff message.

Checked: Binary 2.1.296: mods plumbing is present (`command grep -c -a plugin_dev_mods` = 4, case-insensitive `mods` = 88); /plugin appears as a command string. Mod behavior itself is described only by the speaker; not tested. Related: 60 minute cache on subscription is already a library lesson.

## Related

[[prompt-cache-is-one-hour-on-subscription]], [[draw-a-live-status-row-from-a-function-hook]]
