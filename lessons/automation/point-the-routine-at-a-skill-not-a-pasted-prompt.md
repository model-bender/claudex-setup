---
id: point-the-routine-at-a-skill-not-a-pasted-prompt
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/austin-marchese/6-easy-steps-to-automate-99-of-your-life-with-claude_ktY1b2-OKRA_20260910.txt
---

# Point Every Routine at a Skill, Never at a Pasted Prompt

## TL;DR

A scheduled routine should invoke a skill by name. Then improving the automation means editing one skill file locally, and the routine picks the change up with no edit of its own.

## Why it matters

Austin Marchese ranks the three options and rejects two: pasting the original build prompt makes the routine rediscover the work every run, which is 'slower, costing more tokens, and just being more inconsistent'; pasting a cleaned-up reusable prompt is better but leaves you copying prompts back and forth between your machine and the routine to test anything. Referencing a skill is the one that closes the loop: 'if we update that skill, the routine automatically updates, too.' He calls maintenance effort the deciding variable for whether an automation portfolio survives at all, and a prompt trapped inside a scheduler is the thing you stop maintaining.

## How to apply

Build and refine the workflow as a skill in a normal session first. Create the routine with nothing but the skill invocation, for example '/daily-brief'. To change behaviour later, run the skill interactively, iterate on the output until it is right, then tell Claude to update the skill to match. Leave the routine untouched.

## Related

[[routines-with-claude-generated-prompts]], [[make-the-status-report-its-own-skill-and-attach-it-to-every-routine]], [[prove-a-process-as-a-manual-skill-before-automating-it]]
