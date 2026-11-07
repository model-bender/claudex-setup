---
id: prompt-with-the-goal-the-effort-and-how-to-verify
created: 2026-10-11
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://x.com/bcherny/status/2107565388250874193
---

# Prompt With Three Things: What You Want, How Much Effort to Spend, and How to Verify It

## TL;DR

Boris Cherny: drop heavy scaffolding and tell Claude the goal, the effort you want it to spend, and how it should verify it did the right thing.

## Why it matters

Current models work out the steps themselves; what they cannot guess is how hard to try and what proof of done looks like, and those are the two parts people usually leave out.

## How to apply

State the goal in a sentence, set the effort (in words or with `/effort`), and name the check ("run the tests and show the output"). Stop prescribing the steps for ordinary tasks.

> "Talk to Claude the way you would a coworker. There's no secret to prompting. There's no need to be overly scaffolded or prescriptive for most tasks -- give Claude a goal, and it will figure it out.  Back in the Sonnet 3.5 days, your prompt mattered a lot. Nowadays, it's much more important to communicate to the model:  1. What you want it to do 2. How much effort you want it to spend 3. How it should verify that it did the right thing", Boris Cherny

