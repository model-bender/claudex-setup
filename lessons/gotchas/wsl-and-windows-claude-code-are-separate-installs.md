---
id: wsl-and-windows-claude-code-are-separate-installs
created: 2026-08-31
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Upgrade WSL and Windows Claude Code Separately: They Are Two Installs on Two Update Tracks

## TL;DR

If you mirror a Claude Code setup across WSL and native Windows, the two are separate installs that update independently; check the Windows one explicitly with `claude --version` instead of assuming the WSL upgrade covered it.

## Why it matters

Version-dependent fixes only protect the install that actually has them: the parent case is three Windows permission bypasses closed in 2.1.232/2.1.233, which a WSL-side upgrade does nothing about. A stale native Windows install can sit with unenforced permission rules while its WSL twin reads as fully current.

## How to apply

Treat each environment as its own install. After upgrading, run `claude --version` in native Windows and in WSL separately, and fold both checks into whatever upgrade habit or script you use.

## Related

[[three-windows-permission-bypasses-fixed-in-2-1-232-and-2-1-233]]
