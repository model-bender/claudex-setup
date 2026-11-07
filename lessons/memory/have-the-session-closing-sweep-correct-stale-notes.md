---
id: have-the-session-closing-sweep-correct-stale-notes
created: 2026-11-06
status: active
supersedes: null
category: memory
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xjfize/one_question_i_ask_my_coding_agent_before_closing/
---

# Have the Session-Closing Sweep Check Existing Notes for Staleness, Not Just Collect New Ones

## TL;DR

Over 68 logged end-of-session sweeps, 135 candidates surfaced and roughly one in five was a correction to an existing note, because checking whether something was already saved made the agent open the note and see it was wrong.

## Why it matters

Saved notes rot silently (a branch recorded as unmerged after it merged, a retired script still in a to-do, a cost estimate off by 2x), and a next session reads the stale note as fact; the only moment someone can judge it is while that session's context is still live.

## How to apply

In your pre-clear or pre-compact sweep, ask for corrections to existing notes as a named output alongside new items, with the file each one lives in, and apply only what you pick.

> "The surprise was that about one candidate in five was a correction to a note I already had, which the prompt never asks for.", u/Salty_Negotiation876 on r/ClaudeCode
