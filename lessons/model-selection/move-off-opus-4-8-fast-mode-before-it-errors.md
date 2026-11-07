---
id: move-off-opus-4-8-fast-mode-before-it-errors
created: 2026-11-06
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Move Off Opus 4.8 Fast Mode Before 30 November 2026, Because the Request Errors Instead of Falling Back

## TL;DR

Any script, settings file or habit that pins Opus 4.8 with fast mode will start failing on 30 November rather than quietly running slower.

## Why it matters

A silent fallback would only cost speed; an error breaks unattended jobs. The deadline is three weeks out.

## How to apply

Search settings.json, scheduled tasks and wrapper scripts for Opus 4.8 pins combined with fast mode, and switch them to Opus 5.5 now.

> "2.1.316: Deprecated fast mode for Opus 4.8 as of October 30, 2026; it will be removed on November 30, 2026. After removal, fast mode requests on Opus 4.8 return an error and do not fall back to standard Opus 4.8. Migrate to Opus 5.5 to keep the speedup", Claude Code CHANGELOG

## Related

[[fast-mode-bills-api-credits-and-reprices-your-context-uncached]]
