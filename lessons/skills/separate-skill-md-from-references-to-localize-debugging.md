---
id: separate-skill-md-from-references-to-localize-debugging
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/how-to-use-claude-code-skills-like-the-1-it-s-easy-actually_20260307.txt
---

# Keep SKILL.md and Reference Files Separate So You Can Localize Quality Issues

## TL;DR

Splitting the process (SKILL.md) from the knowledge (reference files) lets you tell whether a bad output is a process bug or a knowledge gap; a single monolithic SKILL.md with everything inlined makes that undiagnosable.

## Why it matters

Many downloaded or LLM-authored skills dump process and all domain knowledge into one SKILL.md file; when output quality is off there's no way to tell if the steps are wrong or the underlying knowledge is wrong.

## How to apply

When building or fixing a skill, ask 'is this a process problem or a knowledge problem?' first. Put step-by-step instructions in SKILL.md only, and move all example/domain-knowledge detail into reference files SKILL.md points to.

## Related

[[skill-md-under-200-lines-progressive-disclosure]], [[skill-gotchas-section-most-valuable-part]]
