---
id: set-claude-code-thrifty-sonic-0-to-disable-bash-first-editing
created: 2026-08-31
status: active
supersedes: null
category: settings
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/issues/88565
  - https://github.com/anthropics/claude-code/issues/87575
---

# Set CLAUDE_CODE_THRIFTY_SONIC=0 to Turn Off Auto Mode's Bash-First Editing Directive

## TL;DR

Auto mode injects a harness directive steering Claude to read with cat/sed and edit with sed and heredocs; setting CLAUDE_CODE_THRIFTY_SONIC=0 in a settings.json env block turns that directive off so Claude goes back to the native Read, Edit, and Write tools.

## Why it matters

Bash-first editing is the root cause of several documented failures: path-scoped .claude/rules and nested CLAUDE.md files are never injected for files touched through Bash, and /rewind cannot restore Bash-written edits because the checkpoint system never sees them. One env var removes the directive behind all of them, which is simpler and more reliable than writing counter-instructions into CLAUDE.md.

## How to apply

Add CLAUDE_CODE_THRIFTY_SONIC=0 to the env block of settings.json; it works there, not just as a shell export. With the directive off, edits flow through the native Read, Edit, and Write tools, which are checkpoint-tracked and trigger path-scoped rule injection.

## Related

[[rewind-leaves-bash-written-edits-on-disk-in-auto-mode]]
