---
id: escalate-model-then-effort-then-claude-md-when-output-misses-the-bar
created: 2026-10-02
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://x.com/bcherny/status/2098217573276131577
---

# When Claude's code misses your quality bar, escalate model, effort, then CLAUDE.md and skills before rewriting

## TL;DR

Boris Cherny gives an ordered ladder for fixing low-quality output on production code: newest model, higher effort, then CLAUDE.md and skills, then more steering, then have Claude pay down debt.

## Why it matters

It replaces ad hoc re-prompting with a fixed escalation order, and it says production code needs guardrails (lint, tests, Claude-driven end-to-end tests, daily fuzzers, automated code and security review) while throwaway prototypes can be treated as black boxes.

## How to apply

Switch to the newest frontier model, run `claude --effort xhigh` (or `/effort`), then tighten CLAUDE.md and skills; keep throwaway prototypes unreviewed but gate production code with lint, tests and Claude Code Review.

Verified: fxtwitter returned the full text, created_at Fri Sep 11 2026 01:10 UTC. `claude --help` on 2.1.287 lists `--effort <level>` (low, medium, high, xhigh, max); `command grep -c -a xhigh` on the 2.1.287 binary gives 31. Not in ledger (the Simon Willison quote of the same post is, this status URL is not). Library grep found no lesson with the ladder or the "hold the bar" framing.

> "If Claude’s code doesn’t meet the bar, try: - Using the latest frontier model (Opus 5 or Fable 5.1) - Increase effort to high or xhigh - Invest in your CLAUDE.md and skills to succinctly teach Claude how to work in your codebase", Boris Cherny

## Related

[[sharpen-the-spec-before-reaching-for-more-effort]]
