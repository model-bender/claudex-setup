---
id: create-a-skill-only-for-a-correction-you-keep-having-to-make
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/matt-pocock-s-exact-system-to-10x-your-claude-skills_QsU0f-547rQ_20261002.txt
  - transcripts/austin-marchese/reverse-engineer-anything-does-way-more-than-you-think_lKz3cDrLgTk_20261120.txt
---

# Create a Skill Only for Something You Keep Sending Back, and Mine Your History to Find It

## TL;DR

Matt Pocock's definition: a skill is a correction you got tired of making. When you ask Claude to propose skills from your past conversations, key the prompt on what you had to send back, not on what you used AI for: if the model already gets a task right first time, a skill for it is just token cost.

## Why it matters

The rule: stop asking what you used AI for, ask what you had to send back and which step of the process it was. Every send-back is a step the model did not get right the first time, so it is worth encoding; skills for things the model already does right cost tokens for nothing. Two Austin Marchese videos make the same point, the first relaying Matt Pocock's system.

## How to apply

Have Claude scan your last 30 days of conversation history for places you sent a result back, framed as 'what did I have to send back, not what did I use AI for', and list them as skill candidates, each tied to one step. A task it got right the first time probably does not need a skill. Neither video gives the text of its prompt, so write your own.

## Related

[[skills-encode-lived-experience-not-obvious-behavior]], [[reverse-engineer-skills-from-successful-runs]]
