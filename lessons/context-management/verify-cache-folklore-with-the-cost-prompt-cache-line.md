---
id: verify-cache-folklore-with-the-cost-prompt-cache-line
created: 2026-08-29
status: active
supersedes: null
category: context-management
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Stop Guessing About Cache Misses: /cost Now Reports Hit Ratio and Tokens Re-Cached

## TL;DR

Every cache rule you follow on faith ("don't edit CLAUDE.md mid-session", "don't switch models", "compact inside the window") is now measurable in-session: 2.1.251 adds a per-session prompt-cache line to `/cost`.

## Why it matters

Cache-invalidation advice has mostly been inferred from cost totals, and some real client-side causes of misses have since been fixed (2.1.248 fixed an hourly miss caused by OAuth token refresh), so an old habit may be guarding against something that no longer happens. Measure before you keep paying the workflow tax.

## How to apply

Run `/cost` and read the prompt-cache line (hit ratio, misses, tokens re-cached, warm/cold). To watch continuously, consume the matching `prompt_cache` object in a status line script.

> "Added a per-session prompt-cache line to `/cost` (hit ratio, misses, tokens re-cached, warm/cold) and a matching `prompt_cache` object for status line scripts", Claude Code CHANGELOG 2.1.251

## Related

[[prompt-cache-what-breaks-it]], [[compact-inside-the-cache-window-not-after-it-expires]], [[never-zero-the-workflow-prefix-stagger]]
