---
id: add-a-setup-wizard-to-shared-skills
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-their-internal-skills-strategy_20260424.txt
---

# Add a Config-File Setup Wizard to Skills You Share With Others

## TL;DR

A shared skill can ask the user for its own per-user configuration (like a channel handle) the first time it's used, resolve it via an API, then write it to a config.json it reads on every future run.

## Why it matters

A skill built around one person's data (e.g. a specific YouTube channel) breaks or needs manual editing when a teammate or friend reuses it on their own account; a one-time setup step that persists the answer removes that friction for anyone the skill is shared with.

## How to apply

Give the skill a config.json in its folder; in skill.md, add a bash step at the top that loads the config and reports "not configured" if empty; instruct Claude to ask the user for the missing value on first run, resolve it (e.g. via an API call), and write it back to config.json for subsequent runs.

## Related

[[shared-brand-context-folder-for-all-skills]]
