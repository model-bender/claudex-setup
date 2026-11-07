---
id: on-windows-a-shell-less-guard-hook-now-blocks-without-git-for-windows
created: 2026-10-19
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21299
---

# On Windows, Install Git for Windows or Set a Hook's shell: a Guard Hook That Names No Shell Now Blocks Without It

## TL;DR

Before 2.1.299 a PreToolUse or PermissionRequest hook with no `shell` was silently skipped on a Windows machine without Git for Windows; now the failed guard denies the call.

## Why it matters

A security hook could do nothing on such a machine with no warning. After the fix the same machine blocks the tool call, which can look like an unexplained denial.

## How to apply

Install Git for Windows, or set the hook's `shell` explicitly. On older versions, do not read a quiet guard as a passing one. Checked: existing hook `shell` field, no new name.

> "Windows: Fixed PreToolUse and PermissionRequest hooks that set no shell failing open when Git for Windows isn't installed; a guard that fails now blocks the call", Claude Code CHANGELOG 2.1.299

## Related

[[a-guard-hook-that-cannot-match-or-serialize-now-blocks-the-call]]
