---
id: switch-to-the-built-in-concise-output-style-instead-of
created: 2026-08-22
status: active
supersedes: null
category: configuration
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/output-styles
---

# Switch to the Built-in Concise Output Style Instead of Fighting Preamble in Every Prompt

## TL;DR

There is now a first-party Concise output style that strips preamble and narration without reducing engineering thoroughness or truncating error/security output.

## Why it matters

The most-reacted open Claude Code issue in this window (#77136, "increasingly default to repetitive rhetorical tics") is verbosity, and people have been patching it with hand-rolled styles that silently drop the coding system prompt. Concise is a built-in, so it keeps the Default style's engineering instructions.

## How to apply

Run `/config` → Output style → Concise, or set `"outputStyle": "Concise"` in `.claude/settings.local.json`; requires v2.1.237+ and takes effect after `/clear`.

> "Concise: Claude leads with the result, skips preamble and narration, and keeps responses short by default, while doing the engineering work as thoroughly as in the Default style. When you ask for an explanation or more detail, Claude answers in full. Claude always keeps the complete content of error reports, security warnings, and confirmations for destructive actions. Requires Claude Code v2.1.237 or later.", canonical: Claude Code docs — Output styles (also CHANGELOG 2.1.237)
