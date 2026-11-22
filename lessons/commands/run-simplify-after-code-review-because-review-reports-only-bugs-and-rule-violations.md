---
id: run-simplify-after-code-review-because-review-reports-only-bugs-and-rule-violations
created: 2026-11-22
status: active
supersedes: null
category: commands
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21328
---

# Run /simplify after /code-review: review now reports only bugs and CLAUDE.md violations

## TL;DR

`/code-review` no longer returns cleanup suggestions on most models, so a clean review does not mean the code is tidy.

## Why it matters

If you relied on /code-review to flag duplication or needless complexity, those findings silently stopped, and a green review gives false comfort about quality.

## How to apply

Treat /code-review as the bug and rule-violation gate and run `/simplify` as a separate pass for reuse and efficiency cleanups.

Checked: `/simplify` and `/code-review` both appear as skills in this 2.1.330 session's skill list; behaviour claim from the changelog only

> "Changed `/code-review` on most models to report only bugs and CLAUDE.md violations; run `/simplify` for reuse, simplification and efficiency cleanups", Claude Code CHANGELOG 2.1.328
