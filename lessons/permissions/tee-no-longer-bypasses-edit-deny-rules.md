---
id: tee-no-longer-bypasses-edit-deny-rules
created: 2026-09-13
status: active
supersedes: null
category: permissions
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Stop Treating `Bash(tee:*)` as an Escape Hatch Around `Edit()` Deny Rules

## TL;DR

Before 2.1.269 a `Bash(tee:*)` allow rule let `tee` write past an `Edit()` deny rule and outside the working directories; that hole is now closed.

## Why it matters

This cuts both ways. A deny list that looked airtight had a real `tee` gap until 2.1.269, and any workflow that leaned on that gap deliberately stops working on upgrade. If your permission rules guard secrets, they only actually held from this version.

## How to apply

Do not use `Bash(tee:*)` or similar shell-redirection allow rules as a deliberate way around an `Edit()` deny rule. On 2.1.269 and later, `tee` destinations are checked against the same deny rules and working-directory scope as `Edit` and `Write`.

> "Fixed `Edit()` deny rules and the write-path check not applying to the file a Bash `tee` command writes; a `Bash(tee:*)` allow rule no longer covers destinations outside the working directories", Claude Code CHANGELOG 2.1.269
