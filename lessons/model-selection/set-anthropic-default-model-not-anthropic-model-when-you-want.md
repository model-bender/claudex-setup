---
id: set-anthropic-default-model-not-anthropic-model-when-you-want
created: 2026-08-22
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Set ANTHROPIC_DEFAULT_MODEL, Not ANTHROPIC_MODEL, When You Want a Starting Model You Can Still Override

## TL;DR

ANTHROPIC_DEFAULT_MODEL sets only the model new sessions open on and leaves /model picks sticky, whereas ANTHROPIC_MODEL pins the model and discards them.

## Why it matters

Anyone routing per task type (cheap default, escalate deliberately) who exported ANTHROPIC_MODEL has been silently losing their /model choice on every restart; the two variables look interchangeable and are not.

## How to apply

In `~/.claude/settings.json`'s `env` block (or the shell), replace `ANTHROPIC_MODEL` with `ANTHROPIC_DEFAULT_MODEL` unless you genuinely want a hard pin that a `/model` pick cannot outlive.

> "Added `ANTHROPIC_DEFAULT_MODEL` environment variable: sets the model new sessions start on, while a `/model` pick still overrides it and persists across restarts (unlike `ANTHROPIC_MODEL`)", canonical: Claude Code CHANGELOG 2.1.236
