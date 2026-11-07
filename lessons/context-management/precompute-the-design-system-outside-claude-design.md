---
id: precompute-the-design-system-outside-claude-design
created: 2026-07-17
status: active
supersedes: null
category: context-management
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Pre-compute the Design System Outside Claude Design, Then Import It Finished

## TL;DR

Claude Design's weekly quota is a separate, small pool, and design-system setup burns more of it than anything else you'll do. Do the exploration elsewhere and spend Design's tokens on execution, not on guessing your brand.

## Why it matters

> **REVISIT (2026-07-17), the "separate pool" framing below is June-era.** [[claude-design-now-bills-your-normal-plan-usage-not-a-separate-quota]] reports that Design's July 2026 upgrade moved it onto normal plan usage (single-source, uncorroborated). The lesson stands regardless: the reason to pre-compute is **specialization**, Design's job is generation, and exploration done elsewhere is cheaper and better wherever the meter sits. Only the "protect a distinct design pool" motive is in doubt.

Every bit of thinking you leave to Claude Design is billed against a pool separate from Claude Code and the chat app, and one or two design systems can reportedly wipe out a Pro plan.

The counter-demo is the evidence: two full design systems for 25% of a Max 20x weekly limit, specifically because "all of the work was done outside of Claude design", and an entire build (2 systems, landing page, mobile wireframes with variations, a video, a slide deck) finishing at 70%, against users burning 100% in an hour.

The review UI reinforces it. Ticking "looks good" on a generated token card costs nothing; only "needs work" pays for a round trip. Import something you already like and you mostly tick.

## How to apply

Pick one of two extraction routes:

1. **skill-ui**, `npm install -g skill-ui` plus Playwright/Chromium, then `skill-ui --url <site> --mode ultra`. Pure static analysis, zero API keys, no token cost. Ultra mode drives Playwright to capture scroll screenshots, hover/focus states and animations, emitting a folder with `skill.md`, a long `design.md`, `colors.json`, `spacing.json`, fonts, and component/animation references.
2. **An image model**, paste 3-5 reference screenshots (landbook.com and Dribbble are good sources) and ask for a one-page design system of tokens, buttons, colors, typography, then ask for it again as a `design.md`.

Either way: go to claude.ai/design → design systems → create, link the local folder, attach fonts/logos/assets, paste `design.md`, and generate (~5 min).

Do the whole setup in ONE focused session, and only if you're committed to the tool.

## Related

[[seed-design-system-with-a-real-brand-kit]], [[attach-only-the-files-claude-design-needs]], [[bracket-claude-design-with-claude-code-skills]], [[extract-a-design-system-from-any-site-with-skill-ui]]
