---
id: codex-queue-resume-wakes-a-parked-session
created: 2026-11-06
status: active
supersedes: null
category: workflows
tool: codex
source_type: canonical
sources:
  - https://github.com/openai/codex/releases/tag/rust-v0.166.0
---

# Queue a Message Into Another Codex Session From a Script With codex queue --resume

## TL;DR

`codex queue --thread <id|name> --message <text> --resume` drops a message into an existing session and wakes it if it is not loaded.

## Why it matters

Without --resume a queued message sits until someone opens the thread; with it, a script or a second terminal can hand work to a parked session.

## How to apply

Name sessions, then call `codex queue --thread <name> --message "..." --resume` from a hook or cron; a failed resume only warns and the command still succeeds.

Checked: `codex queue --help` on 0.167.0 lists `--thread <THREAD>` (session UUID or exact name), `--message <TEXT>` and `--resume` ("After queueing, try to resume the thread on the local daemon or selected --remote server. A failed resume produces a warning and the command still succeeds").

> "Added `codex queue --resume` to resume unloaded threads after queueing a message.", openai/codex release notes 0.166.0
