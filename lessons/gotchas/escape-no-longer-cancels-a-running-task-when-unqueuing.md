---
id: escape-no-longer-cancels-a-running-task-when-unqueuing
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# Escape With Queued Prompts Now Only Drops the Last Queued Message, It No Longer Cancels the Running Task

## TL;DR

Pressing Escape while you have queued messages used to both remove the last queued message and cancel whatever task was currently running; now it only removes the queued message and leaves the running task alone (unless that queued prompt had already entered the task).

## Why it matters

The old behavior silently killed in-progress work just because you wanted to edit a queued follow-up, which is a costly and easy-to-trigger mistake during fast iterative prompting.

## How to apply

Expect Escape to safely pop only the last queued prompt off the queue; if you actually want to cancel the currently-running task, do that as its own explicit action rather than relying on Escape while messages are queued.
