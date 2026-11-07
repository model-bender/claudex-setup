---
id: remote-env-command-and-ampersand-suffix-routes-to-remote
created: 2026-09-01
status: active
supersedes: null
category: remote-access
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# Use /remote-env to Manage Remote Environments, and a Trailing & to Route a Prompt to the Default One

## TL;DR

/remote-env lists and lets you create the same remote environments visible in the Claude Code desktop app or cloud, including environment variables; marking one as default and suffixing a prompt with & sends that prompt to run in the remote environment instead of locally.

## Why it matters

Without a CLI path to remote environments, you'd have to leave the terminal to trigger cloud/remote runs; this keeps environment management and dispatch inside the same session.

## How to apply

Run /remote-env to view or create remote environments (with their env vars) and mark one default. Then append & to any prompt you type to have Claude Code run it in that default remote environment instead of the current session.
