---
id: document-your-folder-layout-in-claude-md-so-claude-files-outputs-correctly
created: 2026-10-02
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/jono-catliff/full-claude-code-masterclass-beginner-to-expert-in-2-hours-2026_R3mx8XHX8ns_20261002.txt
---

# Document the folder layout in CLAUDE.md so Claude files each output in the right place

## TL;DR

A short folder map in CLAUDE.md let Claude reorganize a messy project in one shot, putting generated proposals, sites and decks under output/.

## Why it matters

Jono Catliff's layout is context/, skills/, references/, design/ and output/ with a one-line purpose each. After they asked Claude to clean up the project it put every asset in the right folder in one pass, which they credit to the file structure in CLAUDE.md, since Claude reads that file almost every time it acts.

## How to apply

Add to CLAUDE.md the folders and what belongs in each (context, skills, references, design, output). Then ask Claude to organize the project against it.

Verified: No mechanism claims. Their claim that Claude reads CLAUDE.md on every action matches how the file is loaded each session; their layout is their own choice, not a requirement.

## Related

[[fork-init-into-project-archetype-scaffolding-skills]], [[claude-md-hierarchy-keep-it-under-200-lines]]
