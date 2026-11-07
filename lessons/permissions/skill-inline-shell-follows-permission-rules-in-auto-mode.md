---
id: skill-inline-shell-follows-permission-rules-in-auto-mode
created: 2026-09-24
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Auto Mode No Longer Classifier-Reviews a Skill/Command's Inline ! Shell Lines

## TL;DR

An inline `!command` shell line inside a skill or slash-command definition used to be judged by auto mode's safety classifier like any other Bash call; as of 2.1.271 it instead follows your default-mode permission rules (allow/ask/deny), and only falls back to a reviewed tool call when no rule decides it.

## Why it matters

This changes which mechanism actually gates a skill/command author's embedded shell commands in auto mode, your explicit allow/deny rules now take precedence over the classifier's judgment for these specifically, which can mean either fewer classifier prompts (if you have a matching allow rule) or a hard deny where the classifier might previously have approved something.

## How to apply

If you author skills or slash commands with inline `!` shell lines and rely on auto mode to gate them, check your default permission rules (not just trust in the classifier), an unmatched command now becomes a reviewed tool call rather than a classifier judgment call.

> "Changed auto mode so that a skill's or slash command's inline `!` shell commands follow default-mode permission rules instead of the classifier; a command no rule decides runs as a reviewed tool call", Claude Code CHANGELOG 2.1.271

