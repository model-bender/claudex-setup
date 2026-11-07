---
id: parity-agent-ports-features-across-symmetric-codebases
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
---

# Use a Parity Agent to Port Features Across Symmetric Codebases Like iOS/Android

## TL;DR

When two codebases share the same architecture, e.g. an iOS app and its Android counterpart, spawn one agent-team teammate to read the reference platform's code and generate a task list, then have an executing teammate implement those tasks on the target platform.

## Why it matters

This is one of the more efficient agent-team use cases for feature parity work, as long as the two architectures actually mirror each other.

## How to apply

Give one teammate the reference implementation and ask it to produce a task list describing what the target platform is missing; hand that task list to a second teammate to implement.
