---
id: taskoutput-tool-removed-read-the-output-file-instead
created: 2026-09-24
status: active
supersedes: null
category: agents
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Stop Reaching for TaskOutput, It Was Removed; Read the Task's Output File Instead

## TL;DR

The TaskOutput tool for reading a background task's/agent's output no longer exists as of 2.1.277; the only way to read a background task's output now is Read on its output file, and taskOutputMaxChars/TASK_MAX_OUTPUT_LENGTH are dead settings.

## Why it matters

Any prompt, skill, or habit that still calls TaskOutput on a background agent (rather than Read-ing its output file) is calling a tool that no longer exists; a stale reference to it will error instead of degrade gracefully, and a settings file still tuning taskOutputMaxChars is a no-op.

## How to apply

Use Read on the background task's output file path instead of a TaskOutput call; drop taskOutputMaxChars/TASK_MAX_OUTPUT_LENGTH from settings/env, they do nothing now. Checked: Installed 2.1.281 binary's Agent tool description literally reads "Deprecated: no longer has any effect (the TaskOutput tool was removed). Read a background task's output file wit[h Read instead]" (command grep -a -o context around "TaskOutput" in the binary).

> "Removed the deprecated TaskOutput tool; Claude reads a background task's output file with Read instead, and the `taskOutputMaxChars` setting and `TASK_MAX_OUTPUT_LENGTH` no longer have any effect", Claude Code CHANGELOG 2.1.277
