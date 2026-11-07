---
id: upgrade-past-2-1-280-for-the-symlink-write-fix
created: 2026-09-24
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# A Second Symlink-Write Permission Bypass Was Fixed in 2.1.280, Separate From the 2.1.251 Round

## TL;DR

This library already has a lesson about symlink permission bypasses fixed in 2.1.251; 2.1.280 fixed a distinct one: a write through a symlinked path was being permission-checked against how the path is spelled inside the tree, not where the symlink actually resolves to, so acceptEdits/allow-rules/auto-mode could approve a write that actually landed outside the approved directory.

## Why it matters

Symlink-based permission bypasses have now recurred at least twice across this window (2.1.251, 2.1.280) as distinct bugs in different code paths, which suggests "symlinks in the working tree" is a recurring soft spot worth treating with extra caution rather than a one-time fixed issue, don't assume the class is closed just because one instance was patched.

## How to apply

Stay upgraded past 2.1.280 before trusting acceptEdits, allow rules, or auto mode to correctly scope writes in a repo containing symlinks; the fix means the permission prompt now names the real landing location, so a write that looks like it targets an approved path but actually resolves elsewhere should now surface that in the prompt text.

> "Fixed writes through a symlinked path being judged by their in-tree spelling: the prompt names where the write lands, and `acceptEdits`, allow rules and auto mode no longer approve one landing outside", Claude Code CHANGELOG 2.1.280

## Related

[[upgrade-past-2-1-251-symlink-and-arithmetic-permission-bypasses]]
