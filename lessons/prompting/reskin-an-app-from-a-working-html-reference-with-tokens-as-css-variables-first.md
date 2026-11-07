---
id: reskin-an-app-from-a-working-html-reference-with-tokens-as-css-variables-first
created: 2026-10-19
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1x22sap/i_built_20_free_opensource_html_pages_you_can_use/
  - https://www.reddit.com/r/ClaudeAI/comments/1x22sap/i_built_20_free_opensource_html_pages_you_can_use/peyxc8m/
---

# Reskin an Existing App From a Working HTML Reference, With the Extracted Tokens Written as CSS Variables First

## TL;DR

To change how a working app looks, give Claude Code a single-file HTML page as the visual source of truth, have it write the extracted design tokens out as CSS variables for you to review, and only then apply them across the project while explicitly keeping content, routes and logic.

## Why it matters

Adjectives like "premium" or "modern" leave every design decision to Claude's defaults, while working code carries the exact type scale, spacing, colours and radii. Saying what must stay unchanged helps keep a reskin from turning into a rebuild, and reviewing the tokens first catches a wrong extraction before it is applied everywhere. The poster is clear it does not guarantee the result.

## How to apply

Attach the HTML reference and ask Claude to extract its design system into CSS variables first; check them. Then ask it to apply them, with a line such as the poster's: preserve all existing content, functionality, routes and business logic, and treat the HTML as the visual source of truth, not as a replacement for the app's architecture. Afterwards, review responsive layouts, component consistency and anything else the agent may have changed by accident.

> "Preserve all existing content, functionality, routes, and business logic. Treat the HTML as the visual source of truth, not as a replacement for my application's architecture.", u/Azra_Nysus on r/ClaudeAI

> "the extra step that helps most is asking it to first write out the extracted tokens (colors, type scale, spacing, radii) as CSS variables before touching your project, so you can sanity-check the design system before it gets applied everywhere.", u/DishSuch2406 on r/ClaudeAI

## Related

[[seed-a-new-claude-design-project-with-your-exported-html-as-the-brand]]
