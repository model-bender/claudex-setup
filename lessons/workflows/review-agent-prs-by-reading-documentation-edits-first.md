---
id: review-agent-prs-by-reading-documentation-edits-first
created: 2026-07-17
status: active
supersedes: null
category: workflows
source_type: post
sources:
  - https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/
---

# Orient on a Large Agent-Written PR by Reading Its Documentation Edits First

## TL;DR

When reviewing a big diff an agent wrote, read the documentation/changelog edits before the code, they're the agent's own summary of intent and give you a map before you dive into implementation.

## Why it matters

A large agent-generated PR is hard to review cold; starting in the code means reconstructing intent line by line. The docs the agent updated state what changed and why in prose, so reading them first builds the mental model you then check the code against.

## How to apply

In your review pass over an agent's PR, open the README/docs/changelog edits first, form your understanding of what the change is supposed to do, then read the code diff against that understanding. Pair it with judging the diff by its shape (see another lesson).

> "I find that reviewing the documentation edits first is an _excellent_ way to build an initial understanding of what has changed", Simon Willison

## Related

[[doc-sync-pass-reconcile-docs-against-diffs]]
