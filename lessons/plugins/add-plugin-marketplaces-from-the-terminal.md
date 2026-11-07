---
id: add-plugin-marketplaces-from-the-terminal
created: 2026-07-17
status: active
supersedes: null
category: plugins
sources:
  - transcripts/nate-herk-ai-automation/claude-code-clay-makes-lead-generation-actually-fun_zyvdl__Ywfk_20260712.txt
---

# Add a Plugin Marketplace From the Terminal CLI: the Desktop App and VS Code Extension Can't

## TL;DR

Adding a plugin marketplace (`/plugin` → add marketplace) only works from the Claude Code terminal CLI; the desktop app and VS Code extension can't add one, though once a plugin is installed via the terminal it's usable from every surface.

## Why it matters

Beginners try to add a marketplace from the desktop app or the VS Code extension, hit a wall, and conclude the plugin doesn't work there. It's only a one-time setup constraint: marketplace management is terminal-only, but installed plugins run everywhere. Not knowing this sends people down a dead end before they ever reach the plugin they wanted.

## How to apply

Open Claude in a terminal (e.g. VS Code's integrated terminal running `claude`), run `/plugin`, choose add-marketplace, paste the marketplace URL, install the plugin, and reload. Afterward invoke it from the desktop app or IDE extension as normal. If the plugin bundles an MCP server, ask Claude to help authenticate it, it loads the plugin's setup skill and hands you an OAuth link.

## Related

[[plugin-system-install-from-marketplace]]
