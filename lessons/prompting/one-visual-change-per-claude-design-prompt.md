---
id: one-visual-change-per-claude-design-prompt
created: 2026-07-17
status: active
supersedes: null
category: prompting
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-design-builds-beautiful-3d-websites-instantly-full-tutorial_TcFeSjwTo7g_20260624.txt
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
---

# Change One Visual Dimension per Claude Design Prompt

## TL;DR

Unlike Claude Code, where a mega-prompt spawns a to-do list and gets worked through, Claude Design silently drops most of a multi-change request. Ask for five changes and it does one or two well and disregards the rest.

## Why it matters

This is flagged explicitly as a Claude Code habit that does **not** transfer: "I know that some people might disagree with this because sometimes in Claude Code you want to send off one big prompt."

The failure is silent, no error, just a partial application, so you burn one round discovering which changes landed and another re-asking for the rest.

## How to apply

Send one main visual change per prompt and let it land before the next.

Batch the cheap stuff elsewhere: cosmetic variations go through the tweaks panel, text/size fixes go through direct canvas edits. Reserve prompts for the one substantive change you actually need the model for.

## Related

[[pin-claude-design-edits-to-one-element-with-an-exact-value]], [[ask-claude-design-to-generate-tweak-knobs-instead-of-prompting-variations]], [[declare-variation-axes-and-tweak-toggles-up-front]]
