---
id: build-an-auto-model-mod-that-picks-the-model-per-prompt-and-weigh-the-cache-cost
created: 2026-10-19
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/tristen-o-brien/5-more-claude-code-mods-you-need-get-ahead-of-95-in-9-minutes_aD-h7Bcn5OY_20261015.txt
---

# Describe an Auto-Model Mod to Route Simple Prompts to Haiku and Builds to Opus, Then Check What It Costs You in Cache

## TL;DR

Tristen O'Brien built a mod that reads each prompt and switches the model, shown in the status bar: 'how many unread emails' went to Haiku, 'build a weather dashboard' to Opus.

## Why it matters

Most prompts do not need the biggest model, and he does not want to remember which model does what. The mod makes the call without a slash command.

## How to apply

Ask Claude Code in plain language to build a mod that reads your prompt, picks a model and shows it in the status bar. The transcript gives the behaviour but not the mechanism. Lesson inference: switching models mid-session invalidates the prompt cache (see the related lessons), so check cost before trusting it. Checked: 'mods' exist as a feature (the plugin-authoring skill is listed in 2.1.303); I did not build or test this mod.

## Related

[[prompt-cache-what-breaks-it]], [[spawn-a-subagent-instead-of-switching-model-mid-session]], [[build-claude-code-mods-as-plugins-installed-at-user-scope]], [[ask-claude-to-save-a-mod-as-a-plugin-or-it-stays-temporary]]
