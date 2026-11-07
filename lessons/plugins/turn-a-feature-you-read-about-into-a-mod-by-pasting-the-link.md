---
id: turn-a-feature-you-read-about-into-a-mod-by-pasting-the-link
created: 2026-10-19
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/ray-amjad/most-claude-code-mods-are-toys-these-are-for-agentic-engineers_Od9706XIXcc_20261013.txt
---

# When You See a Feature Write-Up Online, Ask Claude to Turn It Into a Mod

## TL;DR

Paste the article or post and say 'turn this into a mod', and keep the result as your own plugin instead of waiting for the feature to ship.

## Why it matters

Ray Amjad did this with Cognition's 'Dreaming' write-up and got a mod called Dream Pass with a /dream command that merges and rewrites memory and cites its sources, running every 20 turns, before compaction or on demand. He notes it differs from the built-in auto-dream.

## How to apply

1. Paste the link or text. 2. Ask Claude to turn it into a mod, with the plugin-authoring skill loaded. 3. Run /reload-plugins and try it. Checked: claude 2.1.303 binary has the plugin-authoring skill name and a reload-plugins command string; the Dream Pass result is the speaker's demo.

## Related

[[tell-claude-to-load-the-plugin-authoring-skill-before-building-a-mod]], [[ask-claude-to-save-a-mod-as-a-plugin-or-it-stays-temporary]], [[auto-dream-memory-consolidation]]
