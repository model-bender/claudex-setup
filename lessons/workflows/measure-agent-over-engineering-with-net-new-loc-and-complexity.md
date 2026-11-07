---
id: measure-agent-over-engineering-with-net-new-loc-and-complexity
created: 2026-09-24
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://hamel.dev/blog/posts/evals-faq/
---

# Measure agent over-engineering with net-new LOC and cyclomatic complexity

## TL;DR

When building an eval or audit for a coding agent's over-engineering tendency, start with two cheap objective metrics: net new lines of code added and cyclomatic complexity, the same starting point Anthropic's own Claude Code team used.

## Why it matters

Over-engineering audits are usually left to vibes or a single skill-based pass; this gives a quantifiable, repeatable signal you can track per PR or per session instead of relying only on a subjective "does this look bloated" read.

## How to apply

In a review script, eval harness, or CI check on agent-authored diffs, compute net new LOC and cyclomatic complexity (e.g. via radon for Python, complexity-report for JS/TS) per change and flag outliers before merging, alongside whatever qualitative audit you already run.

> "Claude Code's team, for example, added evals for file edits and later for over-engineering. There are many approaches to measure file edits and over-engineering but you can start with metrics like net new lines of code added and cyclomatic complexity.", Hamel Husain and Shreya Shankar

## Related

[[pair-an-over-engineering-audit-skill-with-grill-me]], [[run-traces-through-your-coding-agent-before-buying-an-eval-platform]]
