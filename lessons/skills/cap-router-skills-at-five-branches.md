---
id: cap-router-skills-at-five-branches
created: 2026-08-29
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/you-re-prompting-claude-wrong-use-this-stanford-method-instead_5nB8Rs4l0_M_20260824.txt
---

# Cap a router skill at about five branches, then ask Claude whether to split it

## TL;DR

A skill that inspects conversation context and routes to different sub-workflows (skill routing) is powerful, but once it branches into more than ~5 distinct workflows it's over-engineered; at that point ask Claude "should I simplify this skill or break it up into multiple skills?"

## Why it matters

Once people discover branch-shaped skills they tend to pile everything into one mega-router. The transcript calls this "a crazy frenzy" where one skill tries to branch out and do everything, which is an anti-goal: routing accuracy and maintainability degrade as branches multiply. The creator's own daily-driver example, an "improve system" skill, stays useful precisely because it has a small number of branches (improve a skill from conversation history, audit the whole system, mine conversation history for skill-creation trends).

## How to apply

When building a context-routing skill, enumerate its branches explicitly and hold the line at roughly five. Above that, don't guess: paste the skill to Claude and ask whether to simplify it or split it into multiple skills, then extract the overflow branches into their own single-purpose skills. Treat the ~5 rule as a review trigger, not a hard limit.

## Related

[[skill-systems-over-monolithic-skills]], [[skills-complementary-not-overlapping]]
