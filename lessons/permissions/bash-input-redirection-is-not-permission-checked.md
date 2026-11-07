---
id: bash-input-redirection-is-not-permission-checked
created: 2026-08-16
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Don't Assume `< file` Redirection Is Permission-Checked - It Shipped, Then Was Reverted

## TL;DR

2.1.232 made Bash input redirections (`< file`) permission-checked "like their argument spellings on all platforms"; 2.1.233 reverted it one release later, so on current builds a read via redirection is **not** gated the way `cat file` is.

## Why it matters

A deny rule scoped to a read command does not cover the redirection spelling of the same read. `deny: Bash(cat:*)` does nothing about `while read line; do ...; done < secrets.env`.

The flip-flop is the second trap: anyone who tested this during the 2.1.232 window drew the correct conclusion for exactly one release and the wrong one afterwards. The changelog promises "a narrower version will return in a later release", so the current behaviour is explicitly temporary.

**REVISIT:** written against 2.1.233. Re-test whether `< file` is permission-checked before relying on either answer - a narrower version of the check is expected to return.

## How to apply

Do not rely on command-name-scoped Bash deny rules to protect file contents. Enforce reads at the file layer instead: `permissions.deny` on `Read(path)` and sandbox `denyRead` entries, both of which are independent of shell spelling.

> "Reverted the 2.1.232 Bash permission changes for Cygwin-style symlinks on Windows and for input redirections (`< file`); a narrower version will return in a later release", Claude Code CHANGELOG 2.1.233

## Related

[[keep-credentials-out-of-the-agent-sandbox]], [[sandbox-deny-entries-with-a-trailing-slash-were-bypassable]], [[three-windows-permission-bypasses-fixed-in-2-1-232-and-2-1-233]]
