---
id: link-every-skill-reference-file-directly-from-skill-md
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everything-you-know-about-skills-is-outdated_e7TY56-yIvM_20261002.txt
---

# Keep skill reference files one level deep, linked straight from SKILL.md

## TL;DR

If SKILL.md points to a file that points to a second file, Claude may only preview the second one. Link every reference file directly from SKILL.md.

## Why it matters

Simon Scrapes gives the chain skill.md to advance.md to details.md: the file at the bottom of the chain is more likely to be read only partially, so its content is effectively lost. Anthropic's fix is one level of nesting.

## How to apply

Open each SKILL.md and list every file it points to. Look for any file reachable only through another file and add a direct link from SKILL.md. Claude can do this audit for you.

Verified: Anthropic skill best practices page, fetched 2026-10-02: 'Keep references one level deep from SKILL.md' and the nested-reference head -100 warning. The existing put-every-skill-one-level-under-skills lesson is about where skill folders sit, a different claim.

## Related

[[skill-md-under-200-lines-progressive-disclosure]], [[put-every-skill-one-level-under-skills]]
