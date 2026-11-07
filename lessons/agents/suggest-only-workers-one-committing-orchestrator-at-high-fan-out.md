---
id: suggest-only-workers-one-committing-orchestrator-at-high-fan-out
created: 2026-08-29
status: active
supersedes: null
category: agents
source_type: post
tool: claude-code
sources:
  - https://newsletter.pragmaticengineer.com/p/inside-anthropic
---

# At High Fan-Out, Skip Worktrees: Suggest-Only Agents Plus One Committing Orchestrator

## TL;DR

For very large parallel runs (Bun's Zig-to-Rust rewrite used 64 agents), have worker agents propose changes without writing files and let a single orchestrator agent apply and commit, instead of giving every agent its own worktree.

## Why it matters

Jarred Sumner set the project up so agents "would not use Git worktrees which he found slow, but worked on different files in the same codebase"; serializing writes through one committer removes merge conflicts without per-agent worktree overhead. This is the pattern behind an 11-day, 64-agent rewrite now shipped in production. Worktree isolation remains the right default at normal fan-out; this is the escape hatch when worktree count itself becomes the bottleneck.

## How to apply

Give worker subagents read-only, suggest-only roles (emit diffs or change proposals to a queue or scratch files), and run one orchestrator agent that applies proposals and creates the commits.

> "He created an orchestration system where each AI agent came up with suggestions of what to change, but did not make a change to the file to avoid conflicts; an orchestrator AI agent created the commits", Gergely Orosz (reporting Jarred Sumner, Bun)

## Related

[[anchor-an-ai-language-port-on-a-runtime-agnostic-test-suite]]
