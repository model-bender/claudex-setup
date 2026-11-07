---
id: cross-repo-parallel-fix-one-subagent-per-project
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/my-claude-code-workflow-for-2026_20260307.txt
---

# Fix the Same Bug Across Sibling Projects With One Subagent Per Project

## TL;DR

When you spot a bug in one project that you know exists in several other projects derived from the same template, fix it in parallel by spinning up one subagent per project.

## Why it matters

Because each subagent works in its own separate project directory, there is no risk of two subagents colliding on the same files, which is the usual failure mode of parallel subagent edits.

## How to apply

Identify every sibling project derived from the same template that has the bug, then launch one subagent per project with the same well-defined, small fix instruction.

