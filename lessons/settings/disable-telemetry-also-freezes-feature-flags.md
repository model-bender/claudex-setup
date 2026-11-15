---
id: disable-telemetry-also-freezes-feature-flags
created: 2026-11-15
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/108726
---

# DISABLE_TELEMETRY=1 also freezes feature flags, so Fable 5.2 and other flagged features vanish; pin the model in modelPicker or use /model

## TL;DR

With telemetry off, the /model picker keeps the stale Fable 5.1 row. `claude --model claude-fable-5-2` and `/model claude-fable-5-2` still work, and a user-settings `modelPicker` block adds the row.

## Why it matters

A telemetry opt-out silently changes which models and features you get. The VS Code extension sets DISABLE_TELEMETRY=1 itself when VS Code or VSCodium telemetry is off, and an `env` block cannot override it. The debug log line is `[servedCatalog] off (flag)`.

## How to apply

If you run telemetry off, pass `--model claude-fable-5-2` or `/model claude-fable-5-2`, or add a `modelPicker.options` entry in ~/.claude/settings.json. The picker also needs a restart to pick up a refreshed served list. Run `claude --debug-file` and look for `[servedCatalog]` to confirm.

Checked: on Claude Code 2.1.325, `DISABLE_TELEMETRY` has 17 hits, `modelPicker` 21 and `servedCatalog` 21; 2.1.319 also added `CLAUDE_CODE_DISABLE_FEATURE_FLAGS` (11 hits), which stops flag fetching without turning telemetry off.

> "`DISABLE_TELEMETRY=1` does more than disable telemetry. It stops Claude Code from downloading feature flags and makes it ignore the flags cached on disk, so every flag falls back to its compiled default. Features that depend on a flag break silently.", anthropics/claude-code issue #108726

## Related

[[monitor-tool-now-works-with-telemetry-disabled-from-2-1-310]], [[unset-telemetry-opt-out-vars-because-0-still-counts-as-set]]
