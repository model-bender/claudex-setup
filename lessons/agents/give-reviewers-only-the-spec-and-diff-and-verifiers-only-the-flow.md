---
id: give-reviewers-only-the-spec-and-diff-and-verifiers-only-the-flow
created: 2026-11-06
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-s-new-subagent-rules-will-change-how-you-build_ybx0mmd22pQ_20261026.txt
---

# Hand a Code Reviewer Only the Spec and Diff, and a Verifier Only the Flow to Check

## TL;DR

A review agent in a fresh window should see the original spec and the diff, not the implementer's reasoning. A verifier needs only the user flow to exercise, not even the diff.

## Why it matters

A reviewer that inherits the implementer's reasoning inherits its blind spots. Ray's day-to-day loop is implementer in one window, reviewer in a new window with spec and diff, then verifiers that drive the app against a user-flow test matrix and reset the database or environment between checks.

## How to apply

1. Spawn the code reviewer in a new session with the spec and the diff only.
2. Send its findings back to the implementer.
3. Give the verifier the flows from the test matrix (for a notes app: create, edit, search, share a link, delete) and reset state between checks, or fork one sandbox per flow to run them in parallel.
4. A research subagent needs nothing from the project, only the question.

