---
id: setting-sources-now-reaches-spawned-sessions
created: 2026-09-24
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Spawned Sessions (Teammates, /bg, claude agents, --worktree --tmux) Now Actually Inherit --setting-sources

## TL;DR

If you launch a parent session with a restricted --setting-sources (e.g. to exclude managed/user settings you don't trust for that run), any teammate, /bg session, claude agents session, or --worktree --tmux session it spawns previously did NOT inherit that restriction and could load settings the parent deliberately excluded; as of 2.1.281 they do inherit it.

## Why it matters

This closes a trust-boundary gap silently: a restricted parent session was previously not a restricted tree, since anything it spawned fell back to the full default settings resolution. Anyone using --setting-sources as an isolation mechanism (not just a convenience) should know the boundary only became real in 2.1.281.

## How to apply

If your workflow relies on --setting-sources / SDK settingSources to keep a session (and everything it spawns) off certain settings sources, confirm you're on 2.1.281+; before that version, spawned teammates/background sessions/worktree sessions escaped the restriction. Checked: `setting-sources`/`settingSources` strings present in the installed 2.1.281 binary (command grep -c -a: 26 and 13 hits respectively).

> "Fixed `--setting-sources` (and SDK `settingSources`) not being forwarded to spawned sessions: teammates, `/bg`, `claude agents` sessions and `--worktree --tmux` now start with the parent's restriction", Claude Code CHANGELOG 2.1.281
