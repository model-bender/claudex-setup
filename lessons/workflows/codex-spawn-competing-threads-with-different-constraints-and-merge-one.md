---
id: codex-spawn-competing-threads-with-different-constraints-and-merge-one
created: 2026-11-06
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/ray-amjad/the-new-codex-update-that-manages-all-your-agents_3aMWv9FIu4o_20261106.txt
---

# For a Hard Issue, Have Codex Spin Up Three Threads With Different Constraints, Review the PRs, Merge One

## TL;DR

Ask a Codex thread to create three threads for the same issue, such as performance first, minimal diff, and simplest elegant solution (may refactor), then compare the PRs and merge the one you like.

## Why it matters

Ray shows the Codex app's thread-management tools (list, read, send message, create thread locally or in a worktree, retitle, pin, archive) letting one thread do this. It differs from subagents because each thread is a reviewable, mergeable workspace.

## How to apply

1. In a Codex thread say: create three threads for this issue, one performance-first, one minimal diff, one simplest and most elegant even if it needs an architecture refactor.
2. Open each thread's PR and review.
3. Merge the best.
4. Optionally ask Codex for a summary page of what each thread did (Ray notes Claude would design that better).

## Related

[[spin-up-parallel-threads-at-different-effort-levels-from-one-prompt]], [[rename-pin-and-archive-codex-threads-to-track-long-running-work]]
