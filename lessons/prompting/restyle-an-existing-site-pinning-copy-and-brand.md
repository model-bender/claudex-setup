---
id: restyle-an-existing-site-pinning-copy-and-brand
created: 2026-08-29
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-built-the-ultimate-claude-website-design-skill-steal-this_QUI6Ug4cHnE_20260824.txt
---

# Restyle an existing site by pinning copy and brand and freeing only the presentation

## TL;DR

Instead of regenerating a website from scratch, point Claude at the live/current site plus a design skill and instruct it to keep all copy and branding identical while transforming only presentation and interactivity. You get a premium redesign with zero message drift.

## Why it matters

Full regenerations churn the copy and positioning you already validated; the failure mode of "redesign my site" prompts is a new site, not a better one. The creator's approach ("Hey, Claude, look at my website, use this skill and transform it") produced a redesign that "kept all the same copy... the same branding and the same feel, but turned it into something way more interactive". Pinning content while freeing form also makes review easy: anything that changed besides layout/motion is a bug.

## How to apply

Give Claude the existing site (URL, repo, or export) as the source of truth, state explicitly that copy, brand assets, and messaging must be preserved verbatim, and scope the transformation to structure, styling, and interaction (scroll behavior, animation, hierarchy). Run it through your design skill so taste rules apply, then diff-check the result for unintended copy changes before shipping.

## Related

[[generate-ui-structure-first-then-inject-copy]], [[split-brand-and-structure-sources-in-one-design-prompt]]
