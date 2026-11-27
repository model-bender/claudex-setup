---
id: approve-the-custom-api-key-prompt-on-first-launch
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/austin-marchese/you-re-overpaying-for-claude-code-use-this-open-source-strategy-instead_WyFrrdof5oU_20260910.txt
---

# Choose Yes at Claude Code's custom API key prompt the first time a key-based launcher starts

## TL;DR

The first time an interactive Claude Code session starts with a new key in `ANTHROPIC_API_KEY`, it asks whether to use that key. You have to choose Yes, and the preselected option is No.

## Why it matters

The speaker hits this prompt on the first run of his new OpenRouter launcher and tells viewers to select yes. The docs say the choice is remembered, so a declined key stays unused in later sessions too until you change it.

## How to apply

Open a new terminal, start the key-based launcher, and at the 'Do you want to use this API key?' dialog pick Yes rather than the preselected 'No (recommended)'. If you already declined, turn on "Use custom API key" in `/config`; the toggle only appears while `ANTHROPIC_API_KEY` is set.

Checked: Claude Code 2.1.330 (installed binary): the dialog titled 'Detected a custom API key in your environment' shows `ANTHROPIC_API_KEY`, asks 'Do you want to use this API key?', focuses the cancel option 'No (recommended)', and stores the answer as approved or rejected; it is triggered only by `ANTHROPIC_API_KEY`, not by other auth variables. Live docs (authentication.md, fetched 2026-11-22): in interactive mode you are prompted once to approve or decline the key and the choice is remembered; change it later with the "Use custom API key" toggle in `/config`; in `-p` mode the key is always used when present.

## Related

[[use-openrouters-free-models-router-as-a-rate-limit-fallback]]
