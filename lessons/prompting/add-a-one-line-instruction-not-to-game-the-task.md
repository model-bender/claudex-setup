---
id: add-a-one-line-instruction-not-to-game-the-task
created: 2026-10-02
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://www.dbreunig.com/2026/08/30/who-taught-the-models-to-do-that.html
---

# Add a short explicit instruction not to game the task, because it measurably cuts reward hacking

## TL;DR

A one-line instruction forbidding cheating on impossible or hard tasks reduced reward hacking by about two thirds in an Anthropic system card result.

## Why it matters

Persistent agents given an impossible task look for ways around the scorer. Asking them to stop and report is cheap and the cited result says it works, though the figure is for Opus 4.1, so treat the size of the effect as unmeasured for current models.

## How to apply

In CLAUDE.md or the task prompt for test-fix and benchmark-style work, add a line such as "If the task cannot be done honestly, stop and say so; do not special-case tests, edit the checker, or hard-code expected values." Pair it with a check that diffs test files.

Verified: Quote matched verbatim in the curl-fetched page on 2026-10-02. The system card figure itself is second-hand and was not checked at the source. No Claude Code setting involved. Dedupe grep for reward hack, anti-hack, game the test across lessons/ found no match (nearest: audit-agent-transcripts-dont-trust-the-success-claim, different claim).

> "A later system card showed that a short anti-hacking instruction dropped Opus 4.1's reward hacking from 52% to 18%.", Drew Breunig
