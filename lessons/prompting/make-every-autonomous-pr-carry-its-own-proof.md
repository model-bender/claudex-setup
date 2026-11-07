---
id: make-every-autonomous-pr-carry-its-own-proof
created: 2026-08-16
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://x.com/bcherny/status/2088022665017901167
---

# Make Every Autonomous PR Carry Its Own Proof - Require `/verify`, a Repro, and a Truth Table

## TL;DR

Write the acceptance evidence into the routine prompt itself - run the real app with no mocks, and make every PR run `/verify` and post a repro plus a truth table - so reviewing is reading evidence rather than re-deriving it.

## Why it matters

This is the verbatim prompt behind a routine that landed 180 merged PRs, and its load-bearing clause is the **evidence requirement**, not the task description. The author notes explicitly that modern models don't need "super specific instructions" - which means your specificity budget is better spent on the proof obligation than on describing the work.

Without it, an autonomous PR arrives as a diff plus a claim, and the reviewer has to reconstruct whether it actually works. With it, the PR arrives with the reproduction and the state matrix already attached.

## How to apply

In any unattended or scheduled prompt, add a clause of the form:

> each pr must run /verify and post a repro and truth table to the pr

Pair it with "use workflows to run the real apps (no mocks)" and a named output thread for status. The full original:

> "lets start new daily routines for crash fuzzing ios, android, and desktop apps e2e. make routines for each that use workflows to run the real apps (no mocks) and fuzz them to trigger crashes, then put up fix prs for those crashes. each pr must run /verify and post a repro and truth table to the pr. post updates in a new top level Fuzzer thread in this channel", Boris Cherny

## Related

[[run-a-portfolio-of-daily-maintenance-routines]], [[audit-agent-transcripts-dont-trust-the-success-claim]], [[explicit-numeric-receipts-for-automations]], [[make-video-proof-mandatory-for-ui-changing-prs]]
