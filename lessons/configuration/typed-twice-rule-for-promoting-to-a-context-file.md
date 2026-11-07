---
id: typed-twice-rule-for-promoting-to-a-context-file
created: 2026-09-01
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/simon-scrapes/the-only-claude-cowork-setup-busy-entrepreneurs-actually-need_BMEaJTl3Vo0_20260820.txt
---

# Promote Any Fact You've Typed Into Chat Twice Into a Referenced File

## TL;DR

A concrete threshold for deciding what belongs in a context file: if you've typed the same piece of information into a Claude chat more than twice, turn it into a file and reference it from CLAUDE.md instead.

## Why it matters

Retyping context repeatedly wastes time and risks inconsistency between sessions; a hard numeric rule ('twice') is easier to act on in the moment than a vague 'if it's reused a lot' heuristic.

## How to apply

Track information you re-paste into chats; the second time you paste the same fact, stop and put it in a file under your context folder, then add a line in CLAUDE.md telling Claude to read that file for that kind of task.

## Related

[[move-repeated-prompt-constraints-into-agents-md]]
