---
id: split-skill-reference-files-by-area-so-unrelated-ones-never-load
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everything-you-know-about-skills-is-outdated_e7TY56-yIvM_20261002.txt
---

# Split a multi-area skill's reference files by area so a question loads only one

## TL;DR

Give each domain its own reference file, linked from SKILL.md, so a revenue question never loads the marketing file.

## Why it matters

Simon Scrapes cites Anthropic's example of a data skill with separate files for finance, sales, product and marketing. For a client reporting skill they suggest one file per client. Files not opened cost no context.

## How to apply

List the areas your skill covers. Make one reference file per area (for example reference/finance.md) and have SKILL.md name each one with a one-line description of when to open it.

Verified: Anthropic skill best practices page, fetched 2026-10-02: BigQuery example with reference/finance.md, sales.md, product.md, marketing.md linked from SKILL.md; unopened files 'consuming zero context tokens'.

## Related

[[skill-md-under-200-lines-progressive-disclosure]], [[separate-skill-md-from-references-to-localize-debugging]]
