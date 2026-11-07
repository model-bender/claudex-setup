---
id: avoid-write-glob-permission-rules-use-edit-read
created: 2026-07-17
status: active
supersedes: null
category: permissions
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Don't Scope Permissions With Write(path)/Glob(path)/NotebookEdit(path): Use Edit(path) or Read(path)

## TL;DR

Path-scoped permission rules written as `Write(path)`, `NotebookEdit(path)`, or `Glob(path)` don't scope the way you expect and now trigger a startup warning; path scoping works via `Edit(path)` (writes) and `Read(path)` (reads).

## Why it matters

People intuitively write `Write(src/**)` to gate where the agent can write, or `Glob(**/*.env)` to restrict searches, but those forms are unsupported, so a rule you believe is scoping access may be doing nothing at all. Claude Code added a startup warning precisely because these silent no-op rules give a false sense of containment.

## How to apply

Replace any `Write(path)` / `NotebookEdit(path)` / `Glob(path)` rules in your settings with `Edit(path)` for write scoping and `Read(path)` for read scoping. Heed the startup warning rather than dismissing it, it's flagging a permission rule that isn't enforcing what you intended.

> "Added a startup warning for `Write(path)`, `NotebookEdit(path)`, and `Glob(path)` permission rules — use `Edit(path)` or `Read(path)` instead", Claude Code CHANGELOG 2.1.210

## Related

[[match-tool-parameters-in-permission-rules]]
