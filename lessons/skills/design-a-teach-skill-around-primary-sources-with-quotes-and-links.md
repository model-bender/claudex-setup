---
id: design-a-teach-skill-around-primary-sources-with-quotes-and-links
created: 2026-11-22
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/matt-pocock-the-most-valuable-skill-to-learn-in-the-age-of-ai_Z8lf5oWKfj0_20261017.txt
---

# Build a learning skill that fetches primary sources and explains them with quotes and links

## TL;DR

When you have the agent teach you a topic, make the skill go out and fetch high-trust primary sources, then break them down with direct quotes, attribution and the exact link each claim comes from.

## Why it matters

Pocock says you should not simply trust what an agent teaches you. Hallucination is less frequent than it was but still happens, so the teach skill is built so every explanation can be traced to a primary source the learner can read. Pocock mostly uses teach sessions to get introduced to a topic, then reads the primary source.

## How to apply

In the skill's instructions, require: fetch high quality primary sources first, quote them, attribute each point, and give the link it came from. Pocock's published version (`skills/productivity/teach` in mattpocock/skills, run as `/teach`) tells the model 'Never trust your parametric knowledge', keeps the sources it finds in a `RESOURCES.md`, says lessons 'should be littered with citations', and has each lesson recommend one primary source.

Checked: No built-in mechanism named. mattpocock/skills read through the GitHub API on 2026-11-22: `skills/productivity/teach/SKILL.md` exists with `disable-model-invocation: true` and contains the quoted lines.

## Related

[[require-an-exact-quote-and-source-for-every-rule-extracted-into-an-agent]]
