---
id: ask-claude-to-save-a-mod-as-a-plugin-or-it-stays-temporary
created: 2026-10-11
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-code-just-dropped-mods-master-it-in-10-minutes_LDn7rQKIFro_20261009.txt
---

# Copy a Mod Out of Its Session Folder or It Is Temporary

## TL;DR

Tristen says mods Claude builds are temporary by default, and the docs agree: a mod Claude writes loads only in the session that made it. To keep one, copy its directory out of `~/.claude/dev-mods/<session id>/` and load it with `claude --plugin-dir <folder>`, or add it to a marketplace. Shared mods install like any plugin through /plugin.

## Why it matters

Without copying it out, the mod will not be there each time you open Claude, and Claude Code deletes the session's mods folder once it is older than `cleanupPeriodDays`. Corrected in place on 2026-11-22: the earlier remedy, asking Claude to save the mod as a plugin and install it, is not the documented way to keep one (the id keeps its old name so existing links still resolve).

## How to apply

Once you like a mod, copy its directory to a folder of your own, such as `~/mods/git-branch`, then start sessions with `claude --plugin-dir ~/mods/git-branch`, or add it to a marketplace so others can install it.

Checked: Live docs https://code.claude.com/docs/en/plugins/mods/create.md fetched 2026-11-22 with curl, Claude Code 2.1.330 installed (`dev-mods` and `plugin-dir` both present in the binary): 'A mod Claude wrote loads only in the session that made it, and Claude Code deletes that session's mods folder once it's older than `cleanupPeriodDays`. To keep the mod, copy its directory out of the mods folder to a place of your own'. /plugin appears in the 2.1.296 binary (count 353).
