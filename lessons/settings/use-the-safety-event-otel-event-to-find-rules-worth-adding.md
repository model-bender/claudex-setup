---
id: use-the-safety-event-otel-event-to-find-rules-worth-adding
created: 2026-10-25
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21307
---

# Use the claude_code.safety_event OpenTelemetry Event to See What Stopped or Prompted Each Tool Call

## TL;DR

Since 2.1.307 Claude Code emits one OpenTelemetry event for each tool call that a permission rule, auto mode, a safety check, a hook or the sandbox stopped, prompted or sent back.

## Why it matters

Deciding which allow rules to add, or why an unattended run keeps stalling, used to mean reading transcripts; one event per stopped call gives a list you can count.

## How to apply

With OpenTelemetry export already on, filter on `claude_code.safety_event` and group the results to find the commands that are prompted most often or the mechanism that blocks an unattended run. Checked: 1 match in the installed 2.1.310 binary; the event's attribute names were not checked.

> "Added the `claude_code.safety_event` OpenTelemetry event for each tool call a permission rule, auto mode, a safety check, a hook or the sandbox stopped, prompted or sent back", Claude Code CHANGELOG 2.1.307

