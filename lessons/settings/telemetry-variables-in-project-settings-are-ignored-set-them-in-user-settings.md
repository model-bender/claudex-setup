---
id: telemetry-variables-in-project-settings-are-ignored-set-them-in-user-settings
created: 2026-10-02
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21282
---

# Put telemetry and OTEL variables in user or managed settings, project settings are now ignored for them

## TL;DR

A repo's `.claude/settings.json` can no longer switch on telemetry export or content capture, so a team dashboard setup committed to the repo stops working.

## Why it matters

Protects you from a cloned repo turning on content capture, but breaks setups that put OTEL env in project settings.

## How to apply

Move `CLAUDE_CODE_ENABLE_TELEMETRY` and `OTEL_*` into `~/.claude/settings.json` or managed settings; `/status` and `claude doctor` now list ignored variables.

Verified: Changelog 2.1.282 entries read from the saved raw CHANGELOG; the monitoring-usage docs page (read 2026-10-02) says Claude Code 'ignores the OpenTelemetry exporter variables in a repository's `.claude/settings.json` and `.claude/settings.local.json`'. CLAUDE_CODE_ENABLE_TELEMETRY is present in the 2.1.287 binary.

> "Changed project and local settings to ignore OpenTelemetry variables that turn on export, set its endpoint, or capture content, like `CLAUDE_CODE_ENABLE_TELEMETRY` and `OTEL_LOG_*`", Claude Code CHANGELOG 2.1.282

