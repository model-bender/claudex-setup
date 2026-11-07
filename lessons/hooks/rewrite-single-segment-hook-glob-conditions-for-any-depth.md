---
id: rewrite-single-segment-hook-glob-conditions-for-any-depth
created: 2026-07-25
status: active
supersedes: null
category: hooks
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Rewrite Single-Segment `dir/**` Hook Conditions as `**/dir/**`: They No Longer Match at Any Depth

## TL;DR

A hook `if:` condition like `src/**` now matches only `<cwd>/src`, so hooks scoped to a directory name stop firing on nested copies of that directory, while `deny`/`ask` permission rules keep the old any-depth behaviour.

## Why it matters

This is a silent-failure change: the hook still loads, still validates, and simply stops running on paths it used to cover. Nothing tells you. The asymmetry makes it worse, permission rules kept any-depth matching, so it's natural to assume both surfaces share glob semantics and to leave the hook alone.

## How to apply

Audit every hook `if:` condition of the form `dir/**` and rewrite it to `**/dir/**` wherever you meant any-depth matching. Leave `deny`/`ask` permission rules alone, they still match at any depth, and "fixing" them to `**/dir/**` is unnecessary.

> "Changed single-segment `dir/**` hook `if:` conditions to match only `<cwd>/dir`; write `**/dir/**` for any-depth matching. `deny`/`ask` permission rules keep their any-depth match.", Claude Code CHANGELOG 2.1.214

## Related

[[add-fork-to-sessionstart-hook-matchers]]
