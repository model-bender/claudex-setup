---
id: no-session-persistence-for-batch-headless-runs
created: 2026-08-16
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/best-practices
---

# Pass `--no-session-persistence` to Headless Runs You Don't Want Resumable on Disk

## TL;DR

Every `claude -p` invocation writes a resumable session by default, so a batch loop over 2,000 files leaves 2,000 session transcripts behind.

## Why it matters

Non-interactive runs *feel* ephemeral - you piped a prompt in, you got text out, nothing was opened. But each one persists, and the corpus already treats session history as an asset worth keeping (raising `cleanupPeriodDays` to retain it). That makes the flip side worse: high-volume fan-outs, CI jobs, and pre-commit hooks accumulate transcripts containing whatever code, diffs, and secrets passed through them, sitting on the same disk under the same long retention.

## How to apply

Add `--no-session-persistence` to `claude -p` calls inside batch loops, CI jobs, and hooks. Keep persistence on for interactive and long-running work you actually want to resume or mine later.

> "The run still creates a resumable session unless you pass `--no-session-persistence`.", Claude Code docs, Best practices

## Related

[[headless-mode-for-batch-automation]], [[mine-jsonl-transcripts-for-model-behavior-playbook]]
