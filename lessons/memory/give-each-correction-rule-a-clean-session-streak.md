---
id: give-each-correction-rule-a-clean-session-streak
created: 2026-11-06
status: active
supersedes: null
category: memory
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1xevkyg/drop_your_best_claude_skills_in_here/19rn9ryzign43/
---

# Give Each Correction Rule a Clean-Session Streak: Retire It After Three, Make It Structural After Two Relapses

## TL;DR

Track every rule you added after a correction with a status and a streak of clean sessions, retire it after three clean sessions, and treat a second relapse as a signal to enforce it in code rather than reword it.

## Why it matters

Rule files only grow because nothing ever marks a rule as learned or as unenforceable in prose, so the file keeps paying context for rules the model now follows and keeps restating the ones it never will.

## How to apply

In the session-close routine, log only your explicit corrections, declared rules and repeats of a known failure, with fields for status, streak, relapses and the affected file; retire on three clean sessions and convert on the second relapse.

> "Lifecycle: 3 clean sessions in a row = retired. A relapse resets the streak. A rule that relapses twice needs a structural fix, not a louder rule.", u/clopz_ on r/ClaudeAI

