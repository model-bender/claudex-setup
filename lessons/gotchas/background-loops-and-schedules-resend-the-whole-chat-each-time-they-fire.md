---
id: background-loops-and-schedules-resend-the-whole-chat-each-time-they-fire
created: 2026-11-15
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-pros-don-t-pay-for-max-they-do-these-5-things-instead_ZRKAw472Nmk_20261108.txt
---

# Check what is still running before you walk away: every loop, schedule or goal firing resends the chat

## TL;DR

Anything that starts a new turn in a session (a /loop, a scheduled task, a goal, a message from another session) sends the whole conversation again, so a forgotten one keeps spending after you leave.

## Why it matters

The transcript lists these as the hidden cost of leaving a session open: each one starts a new turn, and each turn sends the whole chat into Claude. After the cache expires that is full price.

## How to apply

Before you leave a session, either finish the step or write a handoff file and close the chat, and stop any loop or schedule you no longer need. In /usage, a running loop gets its own row showing tokens used each time it fires, so you can tune long-running tasks specifically.

Checked: `/usage` exists in Claude Code 2.1.325; the per-loop row the transcript describes was not found in the binary, so treat that part as the transcript's claim.

## Related

[[prompt-cache-what-breaks-it]]
