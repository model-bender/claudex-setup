---
id: permissionrequest-hooks-must-be-command-or-http
created: 2026-09-24
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# PermissionRequest Hooks Can No Longer Be "agent" Type: Use command or http

## TL;DR

An agent-type hook (one that dispatches to a subagent) attached to the PermissionRequest event will no longer run at all as of 2.1.280; it now errors immediately instead of silently doing nothing useful, because an agent hand-back can't return the allow/deny decision that event needs.

## Why it matters

If you'd wired a PermissionRequest hook as an agent-type hook (plausible, since agent-type hooks work for other events), it was already useless there (its answer could never be read as allow/deny) but previously failed silently or ran pointlessly; now it surfaces as a clear, actionable error instead.

## How to apply

For any hook on the PermissionRequest event, use a command (shell) or http hook, not an agent-type hook; the exact runtime error is "agent-type hooks are not supported for PermissionRequest events (an agent hook answers ok or not ok, and cannot return the allow / deny decision a permission request needs). Use a command- or http-type hook instead." Checked: The exact error string quoted above is present verbatim in the installed 2.1.281 binary (command grep -a -o around "PermissionRequest").

> "Changed `PermissionRequest` hooks: an agent-type hook no longer runs there, since its answer could never allow or deny the request; it now shows an error pointing to command or http hooks", Claude Code CHANGELOG 2.1.280
