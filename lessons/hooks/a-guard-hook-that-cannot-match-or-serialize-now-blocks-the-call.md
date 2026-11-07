---
id: a-guard-hook-that-cannot-match-or-serialize-now-blocks-the-call
created: 2026-10-11
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# When a Tool Call Is Blocked and No Rule Explains It, Check the PreToolUse Hook Matcher First

## TL;DR

Since 2.1.288, if matching a PreToolUse or PermissionRequest hook fails, or the tool input cannot be serialized to JSON, the call is blocked instead of the hook being skipped.

## Why it matters

This closes a hole where a guard hook silently did not run. The flip side is a new symptom: calls blocked with no deny rule responsible, caused by a malformed matcher.

## How to apply

When a tool call is blocked unexpectedly, inspect the matcher syntax of your PreToolUse and PermissionRequest hooks before looking at permission rules.

> "Fixed PreToolUse and PermissionRequest hooks being skipped when matching them failed or the tool's input could not be serialized to JSON; the call is now blocked", Claude Code CHANGELOG 2.1.288
