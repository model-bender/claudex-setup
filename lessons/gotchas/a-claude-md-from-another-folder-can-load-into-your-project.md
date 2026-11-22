---
id: a-claude-md-from-another-folder-can-load-into-your-project
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/anthropic-engineers-just-10x-d-everyone-s-claude-code_oz2CwrPV2Rg_20261009.txt
---

# Check for CLAUDE.md files outside the project that load into it

## TL;DR

Cleaning the CLAUDE.md inside a project is not enough: instructions can be coming from somewhere else. /doctor found a CLAUDE.md from a separate project in the speaker's desktop folder loading into the speaker's project at roughly 2,000 tokens.

## Why it matters

You pay for those tokens on every request and the foreign instructions can steer the model, without you knowing they are loaded.

## How to apply

Run `/context all` and read the list under Memory files to see every CLAUDE.md that loads (in fullscreen mode plain `/context` collapses that list). The speaker found the stray file with `/doctor`, whose setup checkup covers CLAUDE.md files. Move or delete a stray file, or exclude it with the `claudeMdExcludes` setting, whose glob patterns match absolute file paths.

Checked: Code.claude.com/docs/en/memory.md (fetched 2026-11-22): 'Claude Code loads CLAUDE.md and CLAUDE.local.md from your current working directory and every directory above it'; `/context all` lists loaded files under Memory files; `claudeMdExcludes` skips files by path or glob (6 matching lines in the 2.1.330 binary). The skills.md `/doctor` section lists CLAUDE.md files among the checkup's areas. That the stray file sat in an ancestor directory is this lesson's inference; the transcript only says it was in the speaker's desktop folder. `claudeMdExcludes` and `/context all` are from the docs, not the transcript.

