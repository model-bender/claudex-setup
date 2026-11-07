---
id: explainability-test-to-prune-overlapping-skills
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/the-claude-code-skills-trap-most-people-fall-for-this_20260307.txt
---

# Delete a Skill If You Can't State When Claude Should Pick It Over a Similar One

## TL;DR

When auditing an installed skill library, apply a one-sentence test to every pair of similar skills: if you cannot explain when Claude should use one versus the other, delete one of them.

## Why it matters

The speaker's diagnosis of the 'hoarding trap': people installing 50-200+ skills end up with overlapping ones (three SEO skills, four copywriting skills), which causes ambiguity, for example running the same SEO audit two days running and getting a different skill set used each time. His fix is explicit: 'if you can't explain when Claude should use one skill versus another, then delete one of them.'

## How to apply

For every pair of skills whose descriptions look similar, ask yourself (not Claude) whether you can state in one sentence when each should fire. If you can't, delete one rather than keeping both 'just in case.' Repeat until your active library is small; the speaker targets a curated 20-30 skills built specifically for your own workflows rather than a large generic collection.

## Related

[[skills-complementary-not-overlapping]], [[curate-a-bulk-skill-pack-before-installing-not-after]]
