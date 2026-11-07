---
id: root-claude-md-as-pure-router-nested-for-specifics
created: 2026-09-01
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/5-hacks-to-instantly-level-up-your-ai-os_Ek1NBfnnTH0_20260724.txt
---

# Keep the Root CLAUDE.md a Pure Routing Table, Push Project-Specific Instructions Into Nested CLAUDE.md Files

## TL;DR

In a large multi-folder AI-operating-system repo, treat the top-level CLAUDE.md purely as a table of contents (here's where wikis live, here's where skills live, here's where projects live) rather than a system prompt, and rely on nested CLAUDE.md files inside subfolders for project-specific behavior.

## Why it matters

A router-only root file stays short and cheap to load on every session, while each subfolder's own CLAUDE.md only loads when you're actually working in that folder.

## How to apply

Write the root CLAUDE.md as short if-you-need-X-look-in-Y lines per data type (wiki, memory, tools, API keys, skills, templates, projects). CD into a subfolder and give it its own CLAUDE.md for that project's specific rules.

