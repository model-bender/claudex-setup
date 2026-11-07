---
id: code-review-reuses-your-last-effort-level
created: 2026-08-07
status: active
supersedes: null
category: commands
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Type the Effort Level Explicitly, Because Bare /code-review Reuses Your Last One

## TL;DR

`/review` is now an alias of `/code-review`, and `/code-review` with no effort level reuses whatever level you typed last rather than resetting to a default.

## Why it matters

The stickiness is invisible and expensive in one direction. Run `/code-review ultra` once for a deep cloud review, then type a bare `/code-review` an hour later expecting a normal pass, and you get another ultra cloud review instead. Nothing in the command you typed tells you which level is currently pinned.

## How to apply

State the level whenever you want to change it: `/code-review high`, `/code-review ultra`, and so on. Treat a bare `/code-review` as "same as last time" rather than "default", and check what you are pinned to before running one in a context where a cloud review would be unwelcome.

> "Changed `/code-review` with no effort level to reuse the level you typed last; type a level like `/code-review high` to change it", Claude Code CHANGELOG 2.1.223

## Related

[[invoke-verify-and-code-review-manually-they-no-longer-auto-run]]
