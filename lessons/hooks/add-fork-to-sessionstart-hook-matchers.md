---
id: add-fork-to-sessionstart-hook-matchers
created: 2026-07-25
status: active
supersedes: null
category: hooks
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Add `fork` to SessionStart Hook Matchers: Forked Sessions No Longer Report `resume`

## TL;DR

SessionStart hooks that branch on a `resume` source stop firing for forked sessions, which now report a distinct `fork` source.

## Why it matters

With `/fork` now creating background sessions routinely, forks became a common session-start path, so a matcher written for `startup|resume|clear` has a hole in it exactly where the new workflow lives. Anything you rely on SessionStart for (plan archival, day-of-week reminders, context re-injection) quietly skips every forked session.

## How to apply

Update SessionStart hook matchers to include `fork` alongside `startup`, `resume`, and `clear` wherever the hook should run on any session start. If a hook should deliberately *not* run on forks, a greeting, say, leaving `fork` out is now the way to express that.

> "Changed SessionStart hooks to report source `\"fork\"` when a session begins as a fork instead of `\"resume\"`", Claude Code CHANGELOG 2.1.214

## Related

[[rewrite-single-segment-hook-glob-conditions-for-any-depth]], [[sessionstart-hook-day-of-week-reminders]]
