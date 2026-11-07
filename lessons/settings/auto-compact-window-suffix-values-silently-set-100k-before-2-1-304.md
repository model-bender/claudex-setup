---
id: auto-compact-window-suffix-values-silently-set-100k-before-2-1-304
created: 2026-10-25
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21304
---

# Give CLAUDE_CODE_AUTO_COMPACT_WINDOW a k or M Suffix Only on 2.1.304 or Later

## TL;DR

Before 2.1.304, `CLAUDE_CODE_AUTO_COMPACT_WINDOW=200k` silently gave a 100K window; from 2.1.304 the variable accepts `k` and `M` suffixes like `--autocompact` and warns when a value is out of range or ignored.

## Why it matters

A suffixed value on an older build compacted at half the intended size with no sign anything was wrong, which looks like the model forgetting context early.

## How to apply

On 2.1.304 or later, write the window as `200k` or a plain token count and read the startup warning if one appears. On an older build, use a plain number. Checked: `CLAUDE_CODE_AUTO_COMPACT_WINDOW` has 17 matches in the installed 2.1.310 binary.

> "Fixed `CLAUDE_CODE_AUTO_COMPACT_WINDOW=200k` silently setting a 100K window: the variable now accepts `k` and `M` suffixes like `--autocompact`, and warns when a value is out of range or ignored", Claude Code CHANGELOG 2.1.304

## Related

[[set-a-fixed-token-auto-compact-window]]
