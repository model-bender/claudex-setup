---
id: replace-the-at-file-picker-with-a-filesuggestion-command
created: 2026-08-29
status: active
supersedes: null
category: settings
source_type: post
tool: claude-code
sources:
  - https://sourcegraph.com/blog/claude-code-file-picker-symbol-ranking
---

# Replace Claude Code's @ Picker via the fileSuggestion Setting So It Ranks Symbols and Recency

## TL;DR

The top-level `fileSuggestion` key in `~/.claude/settings.json` swaps the built-in fuzzy-path @ picker for any command you write, so @ can resolve function names to their defining files and rank exact basenames and recently-touched files first.

## Why it matters

The default picker does subsequence path matching, so a query like `os.rs` returns a page of wrong files and a function name returns nothing at all. Most of the win (exact-basename-wins plus git-recency) needs only local `git ls-files` and `git log`, no external service.

## How to apply

Set `"fileSuggestion": {"type": "command", "command": "~/.claude/file-suggestion"}` pointing at a fast (under ~15ms) command that reads `{"query": ...}` on stdin and prints repo-relative paths on stdout. Sourcegraph's open-source implementation (sourcegraph-community/cookbook, symbol-ranked-file-picker) tiers exact basename > exact symbol > symbol prefix > substring, with recency bonuses. Deleting the key restores the built-in picker.

> "You point it at a command. When you type @ , Claude Code spawns that command once per keystroke, hands it {\"query\": \"...\"} on stdin, and shows whatever repo-relative paths it prints on stdout.", Justin Dorfman (Sourcegraph)
