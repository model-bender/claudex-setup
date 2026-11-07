---
id: code-review-medium-now-reports-cleanup-and-claude-md-convention-findings
created: 2026-10-11
status: active
supersedes: null
category: commands
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Expect /code-review at Medium on Opus 5.5 and Sonnet 5.5 to Also Flag Cleanup and CLAUDE.md Convention Findings

## TL;DR

Since 2.1.290, a medium-effort `/code-review` on models without tuned review settings (including Opus 5.5 and Sonnet 5.5) reports cleanup and CLAUDE.md-convention findings, not only correctness bugs.

## Why it matters

A stale or contradictory CLAUDE.md rule now turns into review findings, and a medium review is longer than it was. If you only want bugs, medium is no longer the level that gives you that on these models.

## How to apply

Keep CLAUDE.md rules current before relying on medium reviews. Use `/code-review low` when you want correctness only, and `/simplify` when you want cleanup on purpose.

> "Changed `/code-review` at medium effort to also report cleanup and CLAUDE.md conventions findings on models without tuned review settings, including Opus 5.5 and Sonnet 5.5", Claude Code CHANGELOG 2.1.290

## Related

[[default-to-code-review-low-it-spawns-no-agents]], [[code-review-line-count-effort-threshold]]
