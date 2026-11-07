---
id: gate-agent-prs-on-a-test-that-fails-without-the-patch
created: 2026-08-29
status: active
supersedes: null
category: automation
source_type: post
tool: claude-code
sources:
  - https://newsletter.pragmaticengineer.com/p/inside-anthropic
---

# Gate Agent-Authored PRs on a Test That Fails Without the Patch and Passes With It

## TL;DR

Before an agent may open a PR, require it to produce a red/green test pair: failing on the unpatched build, passing on the patched one; PRs with no test are auto-rejected.

## Why it matters

This converts "the agent says it fixed it" into machine-checkable proof, and it is how the Bun team (which maintains Claude Code's runtime) runs agent PRs at scale, paired with dual AI reviews (Claude Code review plus CodeRabbit arguing on the PR).

## How to apply

In your PR automation (hook, CI check, or the agent's PR skill), enforce: run the new test against the released/system build expecting failure, then against the patched build expecting success, and auto-reject the PR if no test is attached.

> "The agent tasked with submitting a PR has to write a test that fails in the system version (the one without the patch) of Bun, and passes in the debug build with the patch, before it is allowed to submit a PR", Gergely Orosz (reporting Jarred Sumner, Bun)

## Related

[[make-every-autonomous-pr-carry-its-own-proof]], [[trigger-a-repro-only-agent-on-every-filed-issue]]
