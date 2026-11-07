---
id: broad-bash-allow-rules-now-prompt-for-credential-file-writes
created: 2026-10-02
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21287
---

# A broad `Bash` allow rule no longer silently covers writes to credential stores Claude's file tools refuse

## TL;DR

Even `Bash` with no pattern in allow, or a hook that approves, now stops and asks before a shell command writes to the profile store or credentials file.

## Why it matters

It closes a path where an allow-all Bash rule bypassed the file-tool protection, so unattended runs may now stall on those writes. Same release: "Fixed a dangerous `rm` (such as one on `/` or the home directory) losing its always-ask safeguard when the same command also redirected output to a `~` or wildcard path".

## How to apply

Expect a prompt on those writes; do not rely on a broad allow rule or approval hook as the guardrail, keep deny rules for credential paths.

Verified: Read the entry in the local 2.1.287 block. Library grep: permissions/tee-no-longer-bypasses-edit-deny-rules is the closest sibling (a different bypass).

> "Changed whole-tool `Bash` allow rules and allowing hooks to prompt for, not run, shell writes to files Claude Code's file tools refuse outright (the Anthropic profile store, the host credentials file)", Claude Code CHANGELOG 2.1.287
