---
id: build-a-mod-that-offers-to-save-each-correction-as-a-permanent-rule
created: 2026-11-22
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/austin-marchese/7-new-claude-features-to-get-you-ahead-of-99-of-people-using-ai_BgbJFggbTVE_20261106.txt
---

# Use a mod that offers to save each correction as a permanent rule

## TL;DR

A mod can watch for the moments you tell Claude no or correct it and pop up a band offering to save that correction as a permanent rule.

## Why it matters

It reminds you to stop repeating the same correction and improves the setup continuously, at the moment the correction happens.

## How to apply

Ask Claude Code to build a mod that detects a correction in your prompt and draws a band offering to write it into your rules. The speaker recommends one called 'reflect' but does not say who wrote it or where to get it.

Checked: Live docs fetched with curl on 2026-11-22 (docs index, mods overview, interface and events pages; Claude Code 2.1.330 installed): a mod can 'Draw panes, a band above the prompt, buttons, and text fields', and a `prompt.submit` hook 'sees each prompt before the turn starts', so the described behaviour is within what mods can do. The specific 'reflect' mod was not found: it is not among Anthropic's sample mods in the claude-code-playground repo (blast-radius, replay-theater, token-weather).

## Related

[[route-claude-md-fixes-to-the-narrowest-scoped-file]]
