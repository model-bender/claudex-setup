---
id: set-claude-code-disable-structured-outputs-behind-gateways-that-reject-them
created: 2026-10-11
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Set CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS When Titles, Memory Recall or Prompt Hooks Fail Behind a Gateway

## TL;DR

Gateways that reject structured outputs used to break session titles, memory recall and prompt hooks; since 2.1.288 `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS` turns structured outputs off.

## Why it matters

These failures are quiet: titles go missing and recall never fires, which looks like the feature is broken rather than the gateway.

## How to apply

If you route Claude Code through a gateway or alternate provider and see these symptoms, set `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS=1` in the settings `env` block. Checked: the variable has 7 hits in the 2.1.296 binary.

> "Fixed session titles, memory recall and prompt hooks failing on Mantle or behind gateways that reject structured outputs; added `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS` to turn structured outputs off", Claude Code CHANGELOG 2.1.288
