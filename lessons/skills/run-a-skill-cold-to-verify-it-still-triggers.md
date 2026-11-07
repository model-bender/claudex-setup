---
id: run-a-skill-cold-to-verify-it-still-triggers
created: 2026-07-10
status: active
supersedes: null
category: skills
sources:
  - transcripts/mark-kashef/why-90-of-your-claude-skills-are-dead-weight_cgWZcFKx2lQ_20260704.txt
---

# Run a Skill 'Cold' With a Vague Prompt to Confirm It Still Triggers and Does Not Collide

## TL;DR

Test each skill by firing a deliberately vague prompt that does NOT name the skill, and check whether Claude still auto-invokes the intended one - if a sibling skill fires or none does, its name/description is not unique or trigger-heavy enough.

## Why it matters

Skills only help if they actually activate; with several similarly-named skills (daily-planner / daily-standup / morning-routine / today's-tasks) whichever fires depends on your prompt wording that day, and vague descriptions routinely fail to trigger at all. Running cold surfaces both the collision and the weak-trigger problem empirically, instead of eyeballing frontmatter.

## How to apply

In a fresh session, prompt the underlying task in the vaguest realistic way without calling the skill by name and confirm the intended skill fires. If the wrong one wins, make the name distinctive and rewrite the description to be trigger-heavy (list the exact phrases/situations that should invoke it); re-run cold until it fires reliably. Complements keeping no two skills semantically close.
