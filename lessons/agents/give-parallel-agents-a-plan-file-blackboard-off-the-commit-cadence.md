---
id: give-parallel-agents-a-plan-file-blackboard-off-the-commit-cadence
created: 2026-09-13
status: active
supersedes: null
category: agents
source_type: post
tool: claude-code
sources:
  - https://martinfowler.com/articles/exploring-gen-ai/an-accidental-blackboard.html
---

# Coordinate Parallel Agents Through Per-Section Plan Files, Kept Off the Commit Cadence

## TL;DR

A plan file per work-slice that each agent updates as it goes lets the others read live progress, but propagating it through frequent commits overloads CI.

## Why it matters

It is a cheap coordination primitive that emerges naturally, and the trap is equally natural: you reach for commit-and-push to make the updates visible, then have to back off the push frequency for CI reasons and quietly starve the agents of the very signal you built.

## How to apply

Give each agent a small plan or status file scoped to its section (progress, in-progress markers, hand-off notes for dependents) that the others read, and move that channel off git: poll or update it independently of commit frequency rather than forcing frequent commits to carry it.

> "I believe you want this communication channel to be sitting independently of source control.", Giles Edwards-Alexander, Thoughtworks
