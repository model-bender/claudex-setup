---
id: settle-architecture-choices-by-having-the-agent-build-the
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/guides/agentic-engineering-patterns/better-code/
---

# Settle architecture choices by having the agent build the simulation and load test

## TL;DR

Instead of arguing a technology choice on paper, have agents build throwaway simulations of each candidate and load-test them in parallel, then pick on measurements.

## Why it matters

Willison locates the most expensive technical debt at the planning step, not the coding step, a wrong technology pick is the one mistake refactoring agents cannot cheaply undo later. Prototyping used to be too expensive to run per-option; running N throwaway prototypes concurrently is now cheaper than the meeting.

## How to apply

For a question like "is Redis a good choice for the activity feed at thousands of concurrent users", prompt an agent per candidate to wire up a simulation of the system and run a load test against it to see what breaks, run them in parallel worktrees, and compare the results.

## Staleness

Verified still current, the reasoning is about relative cost of prototyping, which has only moved further in its favour. Adjacent but different: another lesson benchmarks agent tooling; this benchmarks your own stack options.

> "Coding agents can build this kind of simulation from a single well crafted prompt, which drops the cost of this kind of experiment to almost nothing. And since they're so cheap we can run multiple experiments at once, testing several solutions to pick the one that is the best fit for our problem.", Simon Willison
