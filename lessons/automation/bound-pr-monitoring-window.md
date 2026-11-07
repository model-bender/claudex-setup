---
id: bound-pr-monitoring-window
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Bound Autonomous PR Monitoring to a Fixed Window and Act Only on Comment or Merge

## TL;DR

After an agent opens a PR, tell it to watch the PR for a fixed window (e.g. 6 hours) with the Monitor tool, fixing any left comments and ending the session once it's merged or the window expires.

## Why it matters

The presenter's task-lifecycle rule is explicit: 'after notifying the user, monitor the PR for about 6 hours using the monitor tool ... if they leave any comments and you should fix those comments or if they merge it in then you can just end the session.' Without a bound, a monitoring session either ends too early (missing feedback) or runs indefinitely.

## How to apply

Add to your task lifecycle: 'After opening the PR, use the monitor tool to watch it for up to 6 hours. Fix any comments left on it and re-push. End the session once it's merged or the window elapses.'

## Related

[[monitor-watches-expire-at-30-minutes-and-can-drop-events]]
