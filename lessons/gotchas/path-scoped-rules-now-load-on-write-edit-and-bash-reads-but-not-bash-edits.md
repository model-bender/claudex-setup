---
id: path-scoped-rules-now-load-on-write-edit-and-bash-reads-but-not-bash-edits
created: 2026-10-11
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Path-Scoped Rules Now Load on Write, Edit and Single-File Bash Reads, but Still Not on Bash Edits

## TL;DR

Path-scoped `.claude/rules` and nested CLAUDE.md files used to load only when the Read tool touched a file; 2.1.288 added Write and Edit, and 2.1.293 added single-file `cat`, `head`, `tail`, `sed -n` and `grep` reads in Bash. Edits made through Bash are not covered by either fix.

## Why it matters

The read side of the older Bash gap is closed, so the old advice overstates the problem. The edit side still stands: a file changed with `sed -i`, a heredoc or a script can still miss the rule that governs it.

## How to apply

Keep the hook or `CLAUDE_CODE_THRIFTY_SONIC=0` mitigation for files whose rules must hold on every edit. Drop any workaround you added only for Bash reads.

> "Fixed path-scoped `.claude/rules` and nested CLAUDE.md files not loading when Write or Edit creates or changes a file in their scope (previously only Read loaded them)", Claude Code CHANGELOG 2.1.288

> "Fixed path-scoped rules and nested CLAUDE.md files not loading when Claude views a file with a single-file cat, head, tail, sed -n or grep command in the Bash tool instead of the Read tool", Claude Code CHANGELOG 2.1.293

## Related

[[auto-mode-tells-claude-to-edit-with-sed-and-heredocs-instead]], [[set-claude-code-thrifty-sonic-0-to-disable-bash-first-editing]]
