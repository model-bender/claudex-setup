---
id: add-a-contents-list-to-skill-reference-files-over-100-lines
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everything-you-know-about-skills-is-outdated_e7TY56-yIvM_20261002.txt
---

# Add a contents list at the top of any skill reference file over 100 lines

## TL;DR

Claude may preview a long reference file instead of reading it all, so rules past the preview can be missed. A contents list at the top shows the full scope even on a partial read.

## Why it matters

Simon Scrapes says Claude can open a reference file with a head -100 style command to decide whether it is useful, so rules sitting after line 100 may as far as Claude is concerned not exist. Anthropic's own example is an API reference with a contents list (authentication and setup, core methods, advanced features, error handling patterns, code examples) followed by the matching sections.

## How to apply

Ask Claude to go through every skill under .claude/skills, find each reference file longer than 100 lines, and add a contents list at the top that matches its headings.

Verified: Anthropic skill best practices page, fetched 2026-10-02: 'For reference files longer than 100 lines, include a table of contents at the top' and the head -100 partial-read warning. The exact preview command is the doc's wording, 'might use commands like head -100'.

## Related

[[skill-md-under-200-lines-progressive-disclosure]], [[separate-skill-md-from-references-to-localize-debugging]]
