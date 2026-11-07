---
id: bash-deny-rules-miss-path-qualified-and-sh-c-forms
created: 2026-10-02
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/permissions
---

# Do not rely on a Bash deny rule as a boundary, it misses path-qualified and `sh -c` forms

## TL;DR

`Bash(rm *)` stops `rm -rf build/` but not `/bin/rm -rf build/` or `bash -c 'rm -rf build/'`; the docs table also lists `Bash(curl *)` vs `/usr/bin/curl` and `sh -c`.

## Why it matters

A deny rule written for safety gives false assurance. The docs say to use a hook or sandbox for a hard guarantee.

## How to apply

Pair `permissions.deny` Bash rules with a PreToolUse hook or the sandbox (`/sandbox`, network allowlist) wherever the restriction must hold.

Verified: Read live docs permissions.md ("What a Bash rule doesn't match" table) and debug-your-config.md (same row). Library grep for "sh -c", "security boundary", "/usr/bin/" with deny/permission found no lesson on this.

> "A Bash rule matches the command text Claude writes, after Claude Code splits compound commands and strips wrappers. It doesn't match the same program invoked in a different form, so a deny or ask rule covers the invocation Claude usually produces and isn't a security boundary around the program.", Claude Code docs (permissions)
