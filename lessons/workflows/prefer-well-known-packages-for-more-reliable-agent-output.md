---
id: prefer-well-known-packages-for-more-reliable-agent-output
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Prefer Well-Known Packages (e.g. tRPC, Next.js) Over Niche Ones for More Reliable First-Try Agent Output

## TL;DR

Choosing widely-used libraries over niche ones increases the odds Claude Code implements them correctly on the first try, because there is far more training data for them.

## Why it matters

The agent's reliability with a library tracks how much training data exists for it. Well-known packages like tRPC or Next.js get it right first time far more often than obscure or very new libraries.

## How to apply

When there's a choice between an established, popular library and a niche one for the same job, default to the popular one specifically to improve agent reliability, reserving niche/new libraries for cases where you have a strong specific reason.

