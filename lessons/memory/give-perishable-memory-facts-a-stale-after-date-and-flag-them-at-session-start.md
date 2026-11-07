---
id: give-perishable-memory-facts-a-stale-after-date-and-flag-them-at-session-start
created: 2026-10-25
status: active
supersedes: null
category: memory
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xbxoza/my_claude_code_setup_it_runs_like_a_small/
---

# Give Perishable Memory Facts a stale_after Date and Have a SessionStart Hook Flag the Expired Ones

## TL;DR

Keep each memory fact in its own file with frontmatter, give facts that age (versions, addresses, prices, owners) a `stale_after` date, and have a SessionStart hook list the ones past their date so they are re-checked before use.

## Why it matters

A stale memory is believed as confidently as a fresh one. A per-fact expiry turns silent decay into a visible re-check list.

## How to apply

Add `stale_after: YYYY-MM-DD` to the frontmatter of memory files that hold perishable facts, and write a SessionStart hook that prints the paths whose date is before today. `stale_after` is the poster's own convention, not a Claude Code feature; SessionStart is a real hook event (present in the installed 2.1.310 binary). The poster says the post was drafted with Claude.

> "At session start, a hook flags stale facts so they get re-checked before anyone relies on them.", u/aaraujo666 on r/ClaudeCode

## Related

[[track-per-layer-decay-cadence-in-a-rot-md-file]]
