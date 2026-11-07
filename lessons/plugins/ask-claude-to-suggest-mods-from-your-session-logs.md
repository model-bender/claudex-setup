---
id: ask-claude-to-suggest-mods-from-your-session-logs
created: 2026-10-11
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-code-mods-are-game-changers-set-up-these-5-now_9hetShMMp2s_20261009.txt
---

# Ask Claude to read your session logs and propose the top five mods to build

## TL;DR

Mods ship inside plugins and are built in natural language, so have Claude mine your own session history for repeated phrases and tasks and name the five best mods for your workflow.

## Why it matters

Nate Herk did this first: he asked for mods that would help his workflow, save money, move faster and stay organized. He did not take every suggestion, but it showed him what mods could do before he built his own.

## How to apply

Ask Claude Code: look through my session logs, understand what I do and what I constantly say or repeat, and find the top five mods I could build now. Then pick the useful ones and ask Claude to build each. Install or manage them via /plugin in the CLI or desktop app, and ask Claude 'how do I turn that on and off' once built.

Checked: Binary 2.1.296: command grep -c -a 'plugin_dev_mods' style check found mods plumbing (grep -c -a '"mods"' = 48 hits incl. a mods directory constant and dev-mods path); /plugin appears as a command string. Mod behavior itself is described only by the speaker; not tested.

## Related

[[enable-function-hooks-to-unlock-plugin-authoring]]
