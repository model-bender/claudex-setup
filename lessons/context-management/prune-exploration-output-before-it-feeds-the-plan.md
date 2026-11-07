---
id: prune-exploration-output-before-it-feeds-the-plan
created: 2026-08-22
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/sean-kochel/why-your-agentic-workflows-don-t-work_ILKrUq_8aC4_20260820.txt
---

# Prune the Exploration Output Before It Feeds the Plan, and Route Good-But-Not-Now Ideas to a Backlog

## TL;DR

Exploration generates far more ideas than belong in this build; run an explicit pruning pass between exploring and planning, discard what has no value and file the rest as backlog issues instead of accepting them into scope.

## Why it matters

The creator calls this build-level context rot and rates it one of the top failure modes. The mechanism is specific: coding agents generate many small extra ideas during exploration, and if that raw output flows straight into planning, the plan inherits every dangling suggestion, so the build balloons and the pieces are not cohesively tied to any stated reason for existing. It manifests conversationally, the model says "since we're refactoring the tool calling, we should probably also refactor all of the system prompts and consider these one or two other things", you hit accept on the question tool, and scope grows another notch. Non-developers are most exposed because they cannot recognise over-engineering when they see it. Pruning also makes the build cheaper and faster, since a lean plan means fewer tokens and less to verify.

## How to apply

Insert a deliberate pruning step between exploration and planning and ask two questions of every generated idea: is this valuable at all, and should it be integrated right now. Discard the first bucket outright. Send the second to a real tracker (GitHub issues, Linear) as backlog rather than letting it enter the plan, and run a separate prioritisation pass over the backlog later. Automate the check with skills: the creator pairs an over-engineering audit skill (a version of the ponytail repo) with a grill-me style interrogation skill so the pruning pass actively attacks scope rather than passively summarising it. Say no by default to mid-conversation scope suggestions from the model.
