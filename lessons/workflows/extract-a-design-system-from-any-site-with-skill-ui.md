---
id: extract-a-design-system-from-any-site-with-skill-ui
created: 2026-08-31
status: active
supersedes: null
category: workflows
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Extract a Design System From Any Site With skill-ui at Zero Token Cost

## TL;DR

`npm install -g skill-ui` plus Playwright/Chromium, then `skill-ui --url <site> --mode ultra` statically extracts a full design system (skill.md, design.md, colors.json, spacing.json, fonts, component and animation references) with no API keys and no token spend.

## Why it matters

Design-system exploration is among the most token-hungry work you can hand a model, and skill-ui does it by pure static analysis on your own machine, so the extraction costs nothing against any quota. Ultra mode drives Playwright to capture scroll screenshots, hover and focus states, and animations, so the output covers interaction detail a single screenshot misses. The emitted folder is ready to feed into Claude Design or Claude Code as finished reference material.

## How to apply

Install with `npm install -g skill-ui` along with Playwright/Chromium, then run `skill-ui --url <site> --mode ultra` against the site whose design you want. It emits a folder containing `skill.md`, a long `design.md`, `colors.json`, `spacing.json`, fonts, and component/animation references. Link or paste those artifacts into your design tool (for Claude Design: design systems, create, link the local folder and paste `design.md`) so the model executes from a finished system instead of guessing your brand.

## Related

[[precompute-the-design-system-outside-claude-design]]
