---
id: bracket-claude-design-with-claude-code-skills
created: 2026-07-17
status: active
supersedes: null
category: skills
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Bracket Claude Design With Claude Code Skills: It Cannot Load Your Own

## TL;DR

Claude Design is a separate app that supports no custom skills; it always runs Anthropic's built-in front-end design skill. Put your skills on either side of it: author the design system with a skill before, polish the export with a taste/redesign skill after.

## Why it matters

The single biggest documented limitation is that Claude Design "does not allow you to import your own custom skills", so your front-end/UI skills are inert inside it.

That matters because the built-in skill's own defaults have become the generic AI aesthetic. Its description promises interfaces that "avoid generic AI aesthetics", but at Claude Design's volume the escape hatch became the cliche, serif font, coloured accent bars, blinking green dot, and the widespread sense that "everyone thinks Claude design has one look". Anthropic's prompting docs confirm this is baked in rather than accidental: Opus 4.7 "has a consistent default house style with warm cream and off-white backgrounds."

With no skill hook to steer it, your only levers are the artifacts you feed it and an explicit ban list.

## How to apply

**Before:** extract or author the design system in Claude Code with a skill, and paste a forbidden-patterns list into whatever produces it, the "AI tells" section of a taste skill works well (no Inter, no Roboto, no generic gradients, no teal).

**After:** export from Claude Design via Share → standalone HTML (or the whole project as a zip if you need the design files), then `npx skills add` the taste skill and point it at the file: "use the redesign skill on this landingpage.html".

Treat the polish pass as a variant generator, not a strict upgrade. Claude Design's own output beat `redesign`'s in one head-to-head (which swapped in stock images and changed the logo), while the sibling `brutalist` skill produced the best-looking result of that build.

## Related

[[precompute-the-design-system-outside-claude-design]], [[skip-the-frontend-design-skill-for-whole-sites]], [[hand-off-claude-design-exports-to-claude-code]]
