---
id: route-claude-md-fixes-to-the-narrowest-scoped-file
created: 2026-09-01
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# When Claude Code Makes a Mistake, Tell It to Fix the Narrowest Relevant CLAUDE.md, Not the Root One

## TL;DR

After Claude Code errs, direct it to find and edit the most specific applicable CLAUDE.md file for that rule rather than defaulting to adding it at the root.

## Why it matters

Adding every correction to the root CLAUDE.md defeats progressive disclosure: rules that only matter for one subsystem end up loaded into every task's context.

## How to apply

When you spot a mistake, tell Claude Code explicitly: 'find the relevant CLAUDE.md file for this and make the change there,' instead of letting it default to the root file.

