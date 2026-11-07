---
id: pin-the-client-side-auto-mode-classifier-model-with-claude-code-auto-mode-model
created: 2026-10-19
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21302
---

# Choose the Client-Side Auto Mode Classifier's Model With CLAUDE_CODE_AUTO_MODE_MODEL

## TL;DR

You can set which model judges auto mode tool calls, but only when the classifier runs client-side; it has no effect on server-side auto mode.

## Why it matters

The classifier model drives both cost and how often calls are blocked. The same releases add `classifier_verdict`, `classifier_category` and `permission_mode` to OpenTelemetry `tool_decision` events, so the effect can be measured.

## How to apply

Set `CLAUDE_CODE_AUTO_MODE_MODEL=<model>` in the environment or settings `env`, then compare block rates in `tool_decision` telemetry. Check first whether your sessions use the server-side classifier, where the variable does nothing. Checked: 9 hits in the 2.1.303 binary.

> "Added `CLAUDE_CODE_AUTO_MODE_MODEL` to choose the model the client-side auto mode classifier uses; it does not change the model for server-side auto mode", Claude Code CHANGELOG 2.1.302
