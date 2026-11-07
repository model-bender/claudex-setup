---
id: give-a-skill-a-check-fix-repeat-loop-with-a-style-guide-as-the-checker
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everything-you-know-about-skills-is-outdated_e7TY56-yIvM_20261002.txt
---

# Give a skill a check, fix, repeat loop, and use a style guide as the checker when there is no code

## TL;DR

Have the skill draft, review against a reference document, note each issue with the section it breaks, revise, and only finalize when everything passes.

## Why it matters

Simon Scrapes, citing Anthropic, says run a check, fix the errors and repeat until it passes greatly improves output quality, and the check need not be code. Anthropic's no-code example uses a style guide. For a business user the style guide can be a brand voice document.

## How to apply

In the skill, add steps: draft following the reference doc, review against it, list each issue with the section it breaks, revise, review again, finalize only when all requirements are met. For skills with code, replace the review with a validator script.

Verified: Anthropic skill best practices page, fetched 2026-10-02: section 'Implement feedback loops' with the STYLE_GUIDE.md example and the validator example.

## Related

[[skill-self-improvement-loop-binary-assertions]], [[give-an-editing-skill-a-rubric-and-a-revise-threshold]]
