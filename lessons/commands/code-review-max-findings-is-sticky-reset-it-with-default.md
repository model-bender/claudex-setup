---
id: code-review-max-findings-is-sticky-reset-it-with-default
created: 2026-10-11
status: active
supersedes: null
category: commands
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Pass /code-review --max-findings all for a Full Sweep, Then Reset It With --max-findings default

## TL;DR

`/code-review --max-findings <n>|all` raises or lowers the findings cap, and the choice carries over to every later review until you pass `--max-findings default`.

## Why it matters

The default cap hides lower-ranked findings on a large diff. But the override is sticky like the effort level, so a one-off `all` silently makes every later review long and noisy.

## How to apply

Run `/code-review --max-findings all` when you want everything, then `/code-review --max-findings default` to restore the cap. Checked: `--max-findings` has 10 hits in the 2.1.296 binary.

> "Added `--max-findings <n>|all` to /code-review to report more or fewer findings than the usual limit; the choice is reused until you pass `--max-findings default`", Claude Code CHANGELOG 2.1.288

## Related

[[code-review-reuses-your-last-effort-level]]
