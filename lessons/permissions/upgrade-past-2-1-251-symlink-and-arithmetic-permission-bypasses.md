---
id: upgrade-past-2-1-251-symlink-and-arithmetic-permission-bypasses
created: 2026-08-29
status: active
supersedes: null
category: permissions
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Upgrade Past 2.1.251: Symlinks and Arithmetic Assignments Bypassed Permission Checks

## TL;DR

2.1.251 closes three separate permission bypasses: symlinked search paths dodged `Read(...)` deny rules in Grep/Glob, a symlink swapped after the check let file tools read or write outside the approved location, and Bash auto-approved arithmetic variable assignments like `OPTIND=1/0`.

## Why it matters

Anyone relying on `Read` deny rules to keep secrets out of context (the standard `.env` deny pattern) had a hole that no audit of the rules themselves would reveal: the rules were correct, the enforcement path was not. It matters most in repos with symlinked directories and in any session touching untrusted content.

## How to apply

Upgrade to 2.1.251 or later before trusting deny rules in a repo containing symlinks. The companion fixes in the same release: "Fixed file tools (Read, Write, Edit) following a symlink swapped inside the working directory after the permission check, which could read or write outside the approved location" and "Fixed Bash permission checks auto-approving commands that assign an arithmetic expression to an integer shell variable (e.g. `OPTIND=1/0`, `RANDOM=2+2`); these now prompt for approval".

> "Fixed Grep and Glob not applying `Read(...)` deny rules to files reached through a symlinked search path", Claude Code CHANGELOG 2.1.251

## Related

[[avoid-write-glob-permission-rules-use-edit-read]]
