---
id: text-brand-kit-overrides-screenshots-in-claude-design
created: 2026-08-31
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/jono-catliff/claude-code-web-design-10-years-covered-in-66-minutes_2Gda_ZvV1V4_20260701.txt
  - transcripts/jono-catliff/how-i-built-insane-claude-design-websites-in-10-minutes_xYv4_cTOSNM_20260701.txt
  - transcripts/tristen-o-brien/claude-design-basics-master-95-in-10-minutes_20260610.txt
---

# In a Claude Design System, the Pasted Text Kit Overrides Your Screenshots

## TL;DR

When the reference screenshots and the pasted text brand kit disagree, Claude Design follows the text: Stripe buttons came out rounded per the design.md spec even though the screenshots showed square ones. Treat the text as the authority and screenshots as supporting evidence.

## Why it matters

If you assume the screenshots are canonical, you will keep re-uploading better images to fix a detail the text kit is silently dictating. The precedence is invisible until a generated component contradicts the reference site, so knowing the rule up front saves an expensive regeneration loop.

## How to apply

Before generating, proofread the pasted text kit against your screenshots and fix the text side wherever they disagree. When output contradicts a screenshot detail, correct the text kit rather than swapping in different images.

## Related

[[seed-design-system-with-a-real-brand-kit]]
