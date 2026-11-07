---
id: deny-read-secrets-with-a-wildcard-rule-wildcard-denies-only
created: 2026-08-22
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Deny-Read Secrets With a Wildcard Rule: Wildcard Denies Only Became Rename-Proof in 2.1.236

## TL;DR

On macOS, a wildcard sandbox read-deny such as `**/.env` did not take precedence inside an allowed read region and could be bypassed by renaming the file, until 2.1.236.

## Why it matters

Same failure shape as the archive's trailing-slash deny bug: the rule is present, syntactically valid, and produces no warning while the path stays readable, so every config audit passes. Anyone protecting secrets with a `**/` pattern on macOS had a hole for as long as they were on an earlier version.

## How to apply

Upgrade to 2.1.236+, then re-test the denies that matter by asking Claude to read a denied path (and a renamed copy of it) and confirming refusal; don't assume a wildcard deny holds because it is present.

> "Sandbox: on macOS, wildcard read-deny rules (e.g. `**/.env`) now take precedence inside allowed read regions, cover matched directories' contents, and can't be bypassed by renaming the denied file", canonical: Claude Code CHANGELOG 2.1.236
