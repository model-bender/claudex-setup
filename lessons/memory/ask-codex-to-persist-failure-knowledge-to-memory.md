---
id: ask-codex-to-persist-failure-knowledge-to-memory
created: 2026-09-01
status: active
supersedes: null
category: memory
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/master-97-of-codex-in-1-hour-full-course_3TdD8Qv5Tk8_20260626.txt
---

# After a Codex Failure, Ask It to Write Down What It Learned So It Doesn't Repeat It

## TL;DR

When Codex hits and works around an error (like a broken connection method), explicitly tell it to save that knowledge to a file in the project so future sessions don't rediscover it the hard way.

## Why it matters

A fresh Codex chat in the same project won't remember what it learned mid-conversation unless it's written to disk; treating a failure as 'golden knowledge' and asking it to record it prevents the same mistake in later runs.

## How to apply

After Codex resolves an error, say something like 'make sure you don't run into that issue again, write what you learned to a file in this project's memory' and let it append to AGENTS.md or a dedicated notes file.

