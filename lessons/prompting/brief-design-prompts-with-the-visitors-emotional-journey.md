---
id: brief-design-prompts-with-the-visitors-emotional-journey
created: 2026-08-29
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-built-the-ultimate-claude-website-design-skill-steal-this_QUI6Ug4cHnE_20260824.txt
---

# Brief website design by the visitor's emotional journey, not a feature list

## TL;DR

Direct design generation with emotional and narrative constraints: what the visitor hits first and in what order, the one sentence they must believe by the end, where the page should feel calm versus intense, and one signature move no other site does. Then have Claude reason as if it were the user scrolling.

## Why it matters

The creator's observation is that current models take emotional direction far better than they used to: "I'm telling this thing what I want it to feel like... I really have it thinking about if it was the user and clicking through and scrolling through, what would it feel." His design skill's intake bakes these in as questions: "What must the visitor believe by the end? One sentence, not a feature list", "What real assets do you have?" (deciding generated vs owned), "Where should this page feel calm and where should it feel intense?", and "One thing this site should do that no sites you've seen does, this becomes a signature move." The results diverged run to run instead of collapsing into one template, which is exactly the failure mode of adjective-only briefs.

## How to apply

In any Claude Code design prompt (or design-skill intake), replace feature lists with: (1) the scroll journey, what the visitor encounters first and the order after; (2) a single belief statement the page must produce; (3) an inventory of real assets versus what may be generated; (4) an emotional map of calm and intense zones; (5) one signature move. Then instruct Claude to evaluate its draft from the visitor's seat (scrolling, feeling, deciding) before presenting it. Give feedback in the same register ("the hero is bland, it should hook; slow the globe animation so users register what's happening").

## Related

[[reference-real-products-and-state-negatives-instead-of-adjectives]], [[design-philosophy-first-strip-prd-then-pick-one-ux-direction]], [[write-askuserquestion-into-skill-question-steps]]
