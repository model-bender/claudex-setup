---
id: compare-redesign-skill-output-before-trusting-it
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
about: claude-design
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Compare a Redesign/Polish Skill's Output Against the Original Before Accepting It

## TL;DR

Running a 'redesign' or 'de-AI-slop' skill against a Claude Design export is not guaranteed to be an upgrade, in one head-to-head the original Claude Design output was preferred over the redesign skill's version (which swapped in stock images and changed the logo), while a different sub-skill (brutalist) won.

## Why it matters

It's easy to assume a dedicated polish/critique skill always improves on the base output because that's its stated purpose. Here the redesign pass introduced its own regressions (wrong stock images, an altered logo) even while fixing some AI-tell patterns, so blindly accepting its output would have shipped a worse page.

## How to apply

After running a redesign/polish skill, open the before and after side by side rather than assuming the after is better. Check that assets (logo, images) weren't silently swapped, and if the result is worse, try a sibling skill or keep the original.

## Related

[[bracket-claude-design-with-claude-code-skills]], [[taste-skill-named-subskills-redesign-brutalist-minimalist]]
