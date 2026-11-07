---
id: attach-only-the-files-claude-design-needs
created: 2026-07-17
status: active
supersedes: null
category: context-management
tool: claude-design
sources:
  - transcripts/jono-catliff/how-i-hacked-claude-design-usage-bypass-limits_GPCF1XKYiD8_20260701.txt
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Attach Only the Files Claude Design Needs, Never the Whole Repo

## TL;DR

Claude Design reads every file you attach to a project and bills all of it against its own weekly pool. Hand it the two or three files or screens that matter, not your project folder.

## Why it matters

> **REVISIT (2026-07-17):** the "Design's own weekly pool" framing is June-era, see [[claude-design-now-bills-your-normal-plan-usage-not-a-separate-quota]] (single-source). The finding is unaffected: a whole-repo attach is enormously wasteful on **any** meter, and it's now spending the same pool Claude Code needs.

The attach-a-codebase control makes dumping a whole GitHub repo feel natural, and it's the fastest way to destroy the quota: one reported user burned 29% of their weekly limit on a single upload by attaching their entire project folder.

Nothing warns you, and Claude Design has no per-action audit log to diagnose it afterwards, so you cannot reconstruct where the quota went.

## How to apply

Before attaching, decide which files actually inform the design, usually a handful of components or screenshots, and attach only those. For an existing UI you're redesigning, screenshot the individual sections rather than linking the repo.

Watch claude.ai/settings/usage between steps to see the real cost of each action.

One prompting gotcha when you do attach reference screenshots of an existing page: say explicitly "create a structure based on the design system, not based on the screenshots, but include all of those elements", or it will faithfully rebuild the generic layout you were trying to escape.

## Related

[[precompute-the-design-system-outside-claude-design]], [[split-brand-and-structure-sources-in-one-design-prompt]], [[opus-to-generate-sonnet-to-edit-in-claude-design]]
