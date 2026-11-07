---
id: gate-a-fork-behind-a-small-model-classifier-after-every-turn
created: 2026-10-19
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/ray-amjad/most-claude-code-mods-are-toys-these-are-for-agentic-engineers_Od9706XIXcc_20261013.txt
---

# Build Mods on a Classifier-Gated Fork: A Small Model Decides, a Prompt-Cache-Sharing Fork Does the Side Work

## TL;DR

The common pattern behind the useful Claude Code mods is: after each turn a small model (Haiku) answers a quick yes or no, and only on yes does a fork of the conversation run on the same prompt cache while the main session keeps working.

## Why it matters

Ray Amjad says most good mods work this way: cheap early exit like middleware, then a fork that handles background jobs (updating memory, drawing a diagram) without the main agent splitting its attention. Probabilities are available if you use a classifier rather than a yes or no.

## How to apply

1. Describe the behaviour you want to Claude and ask it to build it as a mod (load the plugin-authoring skill first; the /plugin step in the transcript is garbled). 2. Structure it as: call a small model each turn; if the answer is not yes, exit early; otherwise fork the conversation with an extra instruction; pass anything found back into the main session. 3. Run /reload-plugins to load it. Checked: claude 2.1.303 binary: plugin API method names 'model.complete', 'model.classify', 'model.fork' (and 'ui.panes', 'tool.register') appear in a call list, and the 'plugin-authoring' skill name appears 12 times. Mod behaviour itself is the speaker's demo, not tested here.

## Related

[[build-claude-code-mods-as-plugins-installed-at-user-scope]], [[tell-claude-to-load-the-plugin-authoring-skill-before-building-a-mod]], [[forked-subagents-share-main-session-prompt-cache]]
