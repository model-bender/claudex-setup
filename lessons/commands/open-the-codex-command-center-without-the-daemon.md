---
id: open-the-codex-command-center-without-the-daemon
created: 2026-11-06
status: active
supersedes: null
category: commands
tool: codex
source_type: canonical
sources:
  - https://github.com/openai/codex/releases/tag/rust-v0.167.0
---

# Open the Codex Agent Command Center Without the Daemon via codex agents --no-daemon

## TL;DR

`codex agents` is a session overview for browsing and switching sessions; `--no-daemon` runs it on an embedded app server, and unread results are now marked.

## Why it matters

With several parallel Codex sessions, one overview that flags which finished is faster than resuming each thread to check.

## How to apply

Run `codex agents --no-daemon` to scan parallel sessions for unread results and switch into the one that finished.

Checked: `codex agents --help` on 0.167.0: "Open the agent command center to browse and switch sessions"; `--no-daemon` "Run the agents overview with an embedded app server".

> "Open the agent command center with `codex agents --no-daemon`. The command center and session picker now mark unread results (#58238, #58239, #58263, #58264).", openai/codex release notes 0.167.0
