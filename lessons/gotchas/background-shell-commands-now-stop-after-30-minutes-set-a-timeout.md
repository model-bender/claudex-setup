---
id: background-shell-commands-now-stop-after-30-minutes-set-a-timeout
created: 2026-10-02
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21285
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21288
---

# Set an explicit timeout on background shell commands in unattended sessions, they stop after 30 minutes by default

## TL;DR

In `-p`, Agent SDK, CI and cloud sessions, a long build, server or watch started with `run_in_background` is killed at 30 minutes unless the call sets a longer `timeout`, capped at 2 hours. Interactive sessions have no limit since 2.1.288.

## Why it matters

Long jobs in a headless or scheduled run that used to run until finished now die silently from the user's point of view. Anything beyond 2 hours cannot live in a background Bash call there at all.

## How to apply

In a prompt or command that may run headless, ask Claude to set a longer `timeout` on the background call for jobs over 30 minutes, and move anything over 2 hours to tmux, a scheduled job or a routine.

Verified: Read the entry in the local 2.1.285 block; behaviour is a runtime change, not a flag, so no binary string to count. Library grep: only monitor-watches-expire-at-30-minutes-and-can-drop-events covers Monitor, not background Bash.

Corrected 2026-10-02: 2.1.288 narrowed the limit to unattended sessions. Terminal, desktop app and VS Code sessions no longer stop background commands at all.

> "Changed background Bash and PowerShell commands to stop after a time limit (their `timeout` with `run_in_background`, default 30 min, max 2 h); Claude is notified when one is stopped", Claude Code CHANGELOG 2.1.285

> "Changed the background command time limit to apply only in unattended sessions (`-p`, Agent SDK, CI, cloud); terminal, desktop app and VS Code sessions have no limit", Claude Code CHANGELOG 2.1.288
