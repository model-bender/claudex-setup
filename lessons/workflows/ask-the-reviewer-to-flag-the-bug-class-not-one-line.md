---
id: ask-the-reviewer-to-flag-the-bug-class-not-one-line
created: 2026-10-19
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: canonical
sources:
  - https://claude.dev/blog/solving-code-review-at-anthropic/
---

# Tell Your AI Reviewer to Flag the Class of Bug So Every Instance Gets Fixed, Not One Line

## TL;DR

A finding that names the bug class makes the author fix every instance in one round instead of one line per review pass.

## Why it matters

An agent author and an agent reviewer can loop for many rounds, and the post reports most of the extra rounds kept finding old code one bug at a time. The team says class-level findings, with diff-only re-review and a round cap, cut mean reviews to pass from 2.08 to 1.32.

## How to apply

Add to your review prompt or skill: name the bug class and list every instance of it, not only the first. Pair it with your existing round cap. Checked: no mechanism named.

> "Flag the class of bug, so the author fixes every instance, not one line.", Claude Code team blog (Addy Osmani, Morgan Westlee Lunt, Qing Wang)

