---
id: ask-the-wrong-primitive-question-before-building-a-skill
created: 2026-07-10
status: active
supersedes: null
category: skills
sources:
  - transcripts/mark-kashef/why-90-of-your-claude-skills-are-dead-weight_cgWZcFKx2lQ_20260704.txt
  - transcripts/mark-kashef/you-ve-been-using-claude-code-at-10-here-s-the-rest_oYIXe6aqh_U_20260704.txt
---

# Ask the 'Wrong Primitive' Question - a Skill Is a Suggestion, a Hook/Function Is a Rule

## TL;DR

Before packaging something as a skill, decide whether it should instead be a rule, a CLAUDE.md line, a CLI command, a slash command, or a hook - gate on determinism: predictable same-every-time steps belong in a hook or Python function (a deterministic rule), not a skill (a probabilistic suggestion the model may or may not follow).

## Why it matters

People default to skills for everything, so deterministic work ends up as a skill that fires unreliably while genuinely suggestion-shaped guidance gets buried. Matching each job to the right primitive makes behavior reliable and keeps the skill set lean. Where the inner-loop test decides whether a skill should exist at all, this decides which primitive the job actually needs.

## How to apply

For each candidate ask: is it deterministic (fixed A-to-Z every time)? -> hook or CLI/Python function. A short always-true rule? -> a CLAUDE.md line or .claude/rules file. Something you only ever trigger yourself? -> a slash command (optionally disable-model-invocation). A fuzzy, context-dependent process that benefits from preloaded examples? -> a skill. You can have the Claude Code Guide agent run this 'wrong primitive' check when auditing an underperforming skill against Anthropic's current guidance.
