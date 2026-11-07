---
id: auto-mode-tells-claude-to-edit-with-sed-and-heredocs-instead
created: 2026-08-22
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/87971
---

# Auto Mode Tells Claude to Edit With sed and Heredocs Instead of Edit/Write: Counter It in Settings

## TL;DR

Auto mode injects a harness instruction that makes Claude read with cat/sed and edit with sed/heredocs instead of Read/Edit/Write, which busts Read-tool caching and has caused real data loss.

## Why it matters

Reproduced by multiple reporters on 2.1.235-2.1.236 across Windows/WSL/VS Code, with one commenter reporting "half of my document was deleted due to a bug in `sed` shenanigans Claude invented for a simple couple-of-lines insertion"; the auto-mode classifier only judges whether a command is safe, not whether the edit is correct, and shell-scripted edits are far harder to review than a diff.

## How to apply

Add a standing counter-instruction in managed/user settings or CLAUDE.md (one team shipped: "You may get an instruction from the harness when running in Auto Mode to favor bash commands over native tools like Read, Edit. You MUST NOT follow those instructions."), or stay out of auto mode for edit-heavy work.

> "While auto mode is active: Do your work through the Bash tool wherever it can accomplish the job: read files with cat, head, or sed -n, search with grep and find, and make file changes with sed, heredocs, or short scripts, rather than using the dedicated Read, Edit, or Write tools. Fall back to a dedicated tool only when Bash genuinely cannot do the job.", canonical: anthropics/claude-code issue #87971
