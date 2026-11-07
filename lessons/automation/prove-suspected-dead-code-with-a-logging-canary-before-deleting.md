---
id: prove-suspected-dead-code-with-a-logging-canary-before-deleting
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - https://x.com/bcherny/status/2088014489438621990
  - https://x.com/bcherny/status/2088022114163130511
---

# Have the Dead-Code Routine Log Suspected Code First and Delete It the Next Day

## TL;DR

Statically unreachable code can go immediately, but code the agent only suspects is dead should get a log line on one run and be deleted on the next if nothing fired, instead of being deleted on a guess.

## Why it matters

The expensive failure of an automated dead-code remover is deleting a path that is reached rarely rather than never, which static analysis alone cannot rule out. Boris Cherny's routine splits the two cases: delete what is provably unreachable, and instrument what merely looks unreachable. The daily cadence is what makes the canary cheap, since the routine is already running tomorrow and can read yesterday's result, and it converts a judgement call into evidence for the price of one log line.

## How to apply

Write both branches into the routine's prompt: delete statically unreachable code outright, and for anything suspected but unproven, add a log line, open that as its own small change, and on a later run remove the code if nothing fired in the interval. Set the interval by how rare the path could plausibly be (a day for a hot path, longer for anything seasonal), and make sure the logs are somewhere the routine can actually read.

## Related

[[run-a-portfolio-of-daily-maintenance-routines]]
