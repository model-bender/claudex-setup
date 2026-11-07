---
id: give-an-ordered-skill-a-checklist-with-a-go-back-step
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everything-you-know-about-skills-is-outdated_e7TY56-yIvM_20261002.txt
---

# Give an order-dependent skill a copyable checklist with a go-back step

## TL;DR

For multistep skills where order matters, have Claude copy a short checklist into its reply and tick it off. Add a line that sends it back to an earlier step when a check fails.

## Why it matters

Simon Scrapes says steps are for when order matters (check the data before building the report on it) and should be left out when order does not. Anthropic's research synthesis example is five short lines, each with a short paragraph beneath. Step five, verify citations, says to return to step three if citations are incomplete, which stops Claude ticking a failed step and moving on.

## How to apply

In the skill, write the steps as a checklist Claude copies into its reply and checks off. Keep each step short and goal-shaped. Put an explicit 'if X fails, return to step N' in the verification step.

Verified: Anthropic skill best practices page, fetched 2026-10-02: 'provide a checklist that Claude can copy into its response and check off as it progresses', with the research synthesis example.

## Related

[[skill-goal-oriented-not-railroaded]]
