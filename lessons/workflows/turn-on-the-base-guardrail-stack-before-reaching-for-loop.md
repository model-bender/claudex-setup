---
id: turn-on-the-base-guardrail-stack-before-reaching-for-loop
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://x.com/bcherny/status/2077929390806073807
---

# Turn on the base guardrail stack before reaching for /loop, /batch and dynamic workflows

## TL;DR

Claude Code's head of product splits the feature set into a base tier (self-verification, auto mode, default-on code review and security review, a multi-agent view) that comes first and an advanced tier (/loop, /batch, dynamic workflows, subagent worktree isolation) that only pays off once the base tier is in place.

## Why it matters

The archive holds a lesson for nearly every one of these features individually but none on their ordering, and the ordering is the claim: the advanced primitives multiply throughput, so adopting them before the verification and review guardrails multiplies unreviewed output instead. NOTE for the lead: this is a sequencing lesson layered over already-covered features, so it is the weakest of the four on non-obviousness. Its parent tweet (2077929379661844559) is already in the ledger but produced no lesson file; this sub-tweet was not mined.

## How to apply

Audit which tier your setup is on. If auto mode, automated code review and security review are not defaulted on and Claude has no end-to-end way to verify its own work, fix that before adding /loop, /batch, dynamic workflows or subagent worktrees.

> "In practice that means giving Claude ways to verify its own work end to end. It means enabling auto mode for permissions, defaulting on automated code review and security review, and using interfaces that let you manage multiple agents at once (Agent view in CLI, Desktop app, iOS and Android apps, Tag). To get to higher levels it means /loop, /batch, dynamic workflows, and worktree isolation for subagents. It's not about a single feature, but rather using the right features with the right guardrails that enable Claude to automate entire classes of work in a way that your team can trust the output.", Boris Cherny
