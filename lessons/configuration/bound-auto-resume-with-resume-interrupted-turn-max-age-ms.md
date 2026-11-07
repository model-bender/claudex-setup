---
id: bound-auto-resume-with-resume-interrupted-turn-max-age-ms
created: 2026-09-13
status: active
supersedes: null
category: configuration
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Bound `CLAUDE_CODE_RESUME_INTERRUPTED_TURN` With a Max Age So Stale Turns Do Not Resurrect

## TL;DR

Auto-resume could re-run a turn that failed hours earlier; `CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS` caps how stale a turn can be, with a 6 hour default cutoff.

## Why it matters

An old failed turn re-firing long after you stopped watching is both surprising and a waste of the usage bar, and it lands in exactly the long-lived headless or remote sessions where nobody is present to notice.

## How to apply

Set `CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS=<milliseconds>` alongside `CLAUDE_CODE_RESUME_INTERRUPTED_TURN`. Verified present in the installed 2.1.270 binary (7 occurrences).

> "Fixed `CLAUDE_CODE_RESUME_INTERRUPTED_TURN` re-running a turn that had failed with an API error over 6 hours earlier, or longer ago than `CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS` when set", Claude Code CHANGELOG 2.1.269
