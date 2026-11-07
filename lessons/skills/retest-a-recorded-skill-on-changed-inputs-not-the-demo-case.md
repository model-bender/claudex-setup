---
id: retest-a-recorded-skill-on-changed-inputs-not-the-demo-case
created: 2026-07-25
status: active
supersedes: null
category: skills
tool: claude-code
about: claude-cowork
sources:
  - transcripts/simon-scrapes/anthropic-just-solved-claude-cowork-s-biggest-limitation-goodbye-mcp_9QSumbWubZ4_20260724.txt
---

# Validate a Recorded Skill by Deleting the Demo Artifact and Re-Running It With Changed Inputs

## TL;DR

A skill generated from a screen recording can pass by replaying what it watched instead of generalizing. Prove it generalized: delete whatever the recording produced, change a key input value, open a fresh chat, and give the skill only a goal-level instruction.

## Why it matters

In the demo the creator deleted the ManyChat automation the recording had created, changed the trigger keyword from "fable" to "Fable_123", opened a new chat with only the skill attached, and said "do this for the latest video." That is the test that distinguishes a skill that learned the process from one that memorised a 61-step trace, and it caught a real ambiguity, because the skill had to reason about which reel to attach (it picked the matching "stop using Fable 5" video rather than blindly taking the latest) and asked which Notion row to use when two dates were close. Re-running the identical case would have shown none of this, and would have shipped a skill that breaks the first time reality differs.

## How to apply

After saving a recorded skill: (1) delete or reset the artifact the recording created, so a replay can't silently succeed on stale state; (2) change at least one value the skill must read from a data source rather than from the recording, a keyword, a name, a row; (3) start a fresh chat that has the skill attached but no recording context; (4) prompt at goal level only ("do this for the latest video"), never restating steps; (5) watch the live browser to see which decisions it makes rather than trusting the completion message, and refine the skill where it guessed. This is a generalization test, complementary to running a skill cold to check whether its description routes at all.

## Related

[[record-a-narrated-screen-demo-to-author-a-cowork-skill-for-ui-only-software]], [[run-a-skill-cold-to-verify-it-still-triggers]]
