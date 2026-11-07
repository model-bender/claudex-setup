---
id: trigger-a-repro-only-agent-on-every-filed-issue
created: 2026-08-29
status: active
supersedes: null
category: automation
source_type: post
tool: claude-code
sources:
  - https://newsletter.pragmaticengineer.com/p/inside-anthropic
---

# Trigger an Auto-Reproduce Agent on Every Filed Issue, Then Fix in a Fresh Container

## TL;DR

Wire issue-filed events to a repro-only Claude run; only a successful reproduction spawns a second, isolated container that attempts the fix and submits the PR.

## Why it matters

Splitting reproduce from fix filters non-bugs cheaply before spending fix tokens, and the fresh container gives the fixer clean context and isolation. This is a running production automation on a major OSS project (Bun), not a demo.

## How to apply

On the issue-created webhook (GitHub Actions), launch a headless Claude Code run whose only goal is reproduction; on success, start a second containerized run seeded with the repro to fix and submit the PR, which then hits the failing-test gate.

> "Every time someone files an issue, Claude runs to try and reproduce the issue. If it succeeds, it starts another container, which then tries to fix the issue and submit a PR.", Gergely Orosz (reporting Jarred Sumner, Bun)

## Related

[[gate-agent-prs-on-a-test-that-fails-without-the-patch]], [[run-a-portfolio-of-daily-maintenance-routines]]
