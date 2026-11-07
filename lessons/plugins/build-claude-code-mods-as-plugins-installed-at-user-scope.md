---
id: build-claude-code-mods-as-plugins-installed-at-user-scope
created: 2026-10-11
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/mark-kashef/claude-code-now-has-mods-here-are-10-worth-stealing_uvIopT_2sY0_20261009.txt
---

# Install Claude Code mods as plugins, and choose user or project scope

## TL;DR

Mods (panes, footer bars, slash commands that add behavior) ship inside plugins. Install with claude plugin install and pick the scope: user for every chat, project for one repo.

## Why it matters

Mark Kashef describes a mod as lines of code injected to add behavior while you work, a cousin of hooks that needs no model call. He says the plugin is the 'Trojan horse' for the mod, and that scope user applies it to every chat while project scope limits it to one repo (or a shared project level with Claude Code for teams).

## How to apply

1. Run claude plugin install <plugin> --scope user (or project, or local) in the terminal; the desktop app's embedded terminal works too. 2. Start a fresh session to see the mod. 3. To remove experiments in bulk, ask Claude for a bash command that removes them at the same scope (the lesson's inference: it will use `claude plugin uninstall`, so the scope must match the install scope). 4. To build your own, feed Claude Code the mods article and describe the behavior in plain language.

Checked: command grep -c -a -- '--scope' on claude 2.1.296 = 49; 'claude plugin install --help' lists '-s, --scope <scope> Installation scope: user, project, or local'; 'claude plugin uninstall' present (9 hits).
