---
id: taste-skill-ai-tells-forbidden-pattern-list
created: 2026-09-01
status: active
supersedes: null
category: prompting
tool: [claude-code, claude-design]
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Ban Specific AI-Slop Patterns (Inter, Roboto, Generic Gradients, Teal) When Building a Design System

## TL;DR

The taste skill's 'AI tells' section is a concrete forbidden-pattern list, no Inter, no Roboto, no generic gradients, no teal, that you paste into whatever is generating your design system to strip out the telltale AI aesthetic before it ever appears.

## Why it matters

Claude Design and Claude's front-end skill fall back to a documented default house style when a brief is loose, and that default is exactly what makes AI output recognizable as AI output. A named ban list is a much stronger lever than asking for 'not generic' because it removes the specific defaults instead of leaving the model to guess what you mean.

## How to apply

Open the taste skill (npx skills add) and copy its AI-tells section, the list of forbidden fonts, gradients, and colors. Paste that list into the prompt or notes field of whatever is producing your design system, ChatGPT image generation, Claude chat, or Claude Design's own brief, before generation, not after.

## Related

[[bracket-claude-design-with-claude-code-skills]]
