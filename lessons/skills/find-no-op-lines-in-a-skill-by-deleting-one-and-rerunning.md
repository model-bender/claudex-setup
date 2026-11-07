---
id: find-no-op-lines-in-a-skill-by-deleting-one-and-rerunning
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/matt-pocock-s-exact-system-to-10x-your-claude-skills_QsU0f-547rQ_20261002.txt
---

# Find No-Op Lines in a Skill by Deleting One and Checking Whether the Output Changes

## TL;DR

Lines such as 'be thorough' are no-ops: if removing one changes nothing, it was never doing anything and costs tokens.

## Why it matters

Matt Pocock's most engaged skills post, per the video, is about deleting. Agent-written skills are littered with no-ops. The video offers a precise way (remove a suspected line, rerun, compare) and an aggressive way (have Claude scan for no-op language and delete it, then see what happens).

## How to apply

Delete a whole sentence, not just some words. Rewrite what remains as what you want rather than what you do not want, since naming a banned thing puts it back in context (the video's elephant example). If a behaviour can be composed from existing skills, do not add a new skill.

Verified: Speaker's practice, not tested. Claude Code 2.1.287.

## Related

[[simplify-a-skill-after-a-model-upgrade-instead-of-adding-detail]], [[delete-examples-and-negative-constraints-from-claude-md]], [[explainability-test-to-prune-overlapping-skills]]
