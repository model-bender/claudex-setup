---
id: taste-skill-named-subskills-redesign-brutalist-minimalist
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
about: claude-design
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# The Taste Skill Ships Named Sub-Skills (redesign, brutalist, minimalist): Invoke Them by Name to Get Different Aesthetics

## TL;DR

The taste skill is a collection, not one skill; asking Claude Code to 'use the redesign skill', 'reformat using the brutalist skill', or the minimalist skill on the same exported HTML produces genuinely different visual outcomes from the identical input file.

## Why it matters

Without knowing the collection has multiple named entry points, you'd only ever try the default redesign pass and miss that a sibling skill (brutalist, in this case) can produce a noticeably better or more on-brand result for the same input.

## How to apply

After exporting an HTML page from Claude Design (or any page you want re-skinned), install with `npx skills add` the taste skill, then in Claude Code say 'use the [redesign|brutalist|minimalist] skill on this landingpage.html file'. Run more than one against the same source file and compare, they diverge enough in style that picking the wrong one costs you nothing but a rerun.

## Related

[[bracket-claude-design-with-claude-code-skills]]
