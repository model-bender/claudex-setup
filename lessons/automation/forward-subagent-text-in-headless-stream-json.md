---
id: forward-subagent-text-in-headless-stream-json
created: 2026-07-17
status: active
supersedes: null
category: automation
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Forward Subagent Text and Thinking Into Headless stream-json With --forward-subagent-text

## TL;DR

In headless/SDK runs, subagents' intermediate text and thinking are omitted from stream-json output by default, pass `--forward-subagent-text` (or set `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT`) to surface them.

## Why it matters

An automated `claude -p --output-format stream-json` pipeline only sees each subagent's final result, so a fan-out that misbehaves mid-run is invisible until it returns (or doesn't). Forwarding the subagents' text and thinking restores real-time observability into what your workers are actually doing.

## How to apply

Add the `--forward-subagent-text` flag (or export `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT`) on any headless/SDK session whose stream-json you monitor or log, so subagent narration and thinking appear in the stream alongside the final results.

> "Added `--forward-subagent-text` flag and `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` environment variable to include subagent text and thinking in stream-json output", Claude Code CHANGELOG 2.1.211

## Related

[[headless-mode-for-batch-automation]]
