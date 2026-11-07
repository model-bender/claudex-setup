---
id: the-memory-md-compaction-nudge-uses-hardcoded-caps
created: 2026-09-13
status: active
supersedes: null
category: memory
source_type: canonical
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/issues/91188
---

# Measure MEMORY.md Yourself Rather Than Trusting the Compaction Nudge's Reported Size

## TL;DR

The auto-memory compaction reminder fires at 80% of a hardcoded 200-line / 25,000-unit cap and targets 70%, and its reported KB figure can understate real bytes for non-ASCII content.

## Why it matters

Neither cap is configurable for the personal index, so the arithmetic is fixed and the nudge is the only signal you get. If your index carries non-ASCII content, acting on the reported figure can leave it further over budget than it claims, or trigger a more aggressive trim than needed.

## How to apply

Keep MEMORY.md near 160 lines and well under the unit cap by measuring directly, for example `node -e "console.log(require('fs').readFileSync('MEMORY.md','utf8').length)"` for the UTF-16 unit count the reminder actually uses, rather than judging by bytes on disk. The 0.8 fire threshold and 0.7 target multiplier were re-derived against the installed 2.1.270 binary; the exact 200 / 25,000 values rest on the thread's own analysis.

> "`kM` and `MU` are 200 and 25,000, hardcoded, with no configured cap anywhere in that function.", anthropics/claude-code issue #91188
