---
id: reset-the-session-when-a-long-run-fixates-compaction-does-not-cure-it
created: 2026-10-19
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: post
sources:
  - https://www.dbreunig.com/2026/10/14/context-inertia.html
---

# Reset the Session When a Long Run Keeps Pursuing a Wrong Idea: Compaction Does Not Cure Context Inertia

## TL;DR

When a long session keeps chasing a wrong hypothesis, have it write a short note of state, findings and dead ends, then start a fresh session with only the repo and that note, instead of relying on compaction.

## Why it matters

Breunig cites recent papers where agents anchored on their own past attempts, with one finding the inertia persists despite periodic compaction, because the summary keeps the in-progress work that drives the fixation.

## How to apply

Check `/context` when the model starts flailing, ask for the note, then `/clear` or open a new session and give it only the codebase and the note. Checked: `/context` 14 hits in the 2.1.303 binary.

> "For agentic programmers, there's an easy solution: reset your context.", Drew Breunig

## Related

[[diagnose-context-failure-mode-before-fixing-it]]
