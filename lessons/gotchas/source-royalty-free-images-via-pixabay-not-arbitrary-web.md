---
id: source-royalty-free-images-via-pixabay-not-arbitrary-web
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/jono-catliff/claude-code-web-design-10-years-covered-in-66-minutes_2Gda_ZvV1V4_20260701.txt
---

# Ask Claude to Pull Stock Images From a Royalty-Free Library Like Pixabay

## TL;DR

When Claude fills placeholder images on a generated site, direct it to pull from a named royalty-free source such as Pixabay rather than arbitrary web images, to avoid copyright cease-and-desist risk.

## Why it matters

Reused copyrighted images (e.g. stock photos already used on thousands of other sites, or images without a royalty-free license) can trigger legal cease-and-desist demands years after a site ships.

## How to apply

In the image-fill prompt to Claude Code/Design, name a royalty-free source explicitly (e.g. 'pull stock images from Pixabay') instead of leaving the image source unconstrained.
