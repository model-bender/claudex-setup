---
id: trust-type-safe-stacks-more-in-diff-review
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/ray-amjad/my-claude-code-workflow-for-2026_20260307.txt
---

# Trust Agent Diffs More on a Type-Safe Stack

## TL;DR

When reviewing an agent's diff by its shape rather than line-by-line, trust the result more on a type-safe stack (e.g. tRPC, Prisma) because a type error will surface a shape mismatch automatically.

## Why it matters

Type safety acts as a second, mechanical check on top of a human's shape-based review, catching the class of mistake a quick visual diff scan would miss.

## How to apply

When deciding how much scrutiny a shape-based diff review needs, spend less time reading individual lines on projects built on type-safe tooling, and more on loosely-typed code.

