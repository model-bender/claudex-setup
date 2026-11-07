---
id: treat-a-red-build-as-a-stop-signal-when-agents-run-in-parallel
created: 2026-11-06
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
source_type: post
sources:
  - https://martinfowler.com/rachels-ramblings/good-devs-wary.html
---

# Treat a Red Build as a Stop Signal When Agents Run in Parallel, and Fix the Cause Instead of Living With Red

## TL;DR

In an experiment where agents wrote all the code, the app ran but the build was frequently red, which made a green build stop being reassuring too.

## Why it matters

If agents (especially several in parallel, or in big batches) leave the shared build permanently red, nobody and no agent can tell a real regression from noise, so the check stops working as a feedback signal. The post lists likely causes: agents stepping on each other's changes, code not modular enough for separate work, or changes arriving faster than checks finish.

## How to apply

Make the instruction file say a red build or test run is a stop condition: the agent investigates and fixes it before starting new work, and a Stop or PostToolUse hook that runs the check can enforce it. If red persists, cut the number of parallel Claude Code sessions or worktrees touching the same area and shrink the batch size per session.

> "A red build should mean something: stop, investigate, fix it.", Rachel Laycock (Thoughtworks CTO)
