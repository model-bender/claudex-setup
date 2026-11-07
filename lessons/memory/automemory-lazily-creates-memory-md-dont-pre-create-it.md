---
id: automemory-lazily-creates-memory-md-dont-pre-create-it
created: 2026-09-01
status: active
supersedes: null
category: memory
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-memory-system-compared-so-you-don-t-have-to_20260424.txt
---

# Don't Pre-Create memory.md, Automemory Creates It Only When It Has Something to Note

## TL;DR

A brand-new project folder has no memory.md or CLAUDE.md until Claude actually records feedback; automemory builds the index quietly on demand rather than requiring setup.

## Why it matters

Seeing no memory file in an empty project can look like automemory is broken or needs manual bootstrapping, when it is simply waiting for something worth remembering.

## How to apply

Don't manually create memory/memory.md in a fresh project. Just work normally; once Claude has feedback or notes worth keeping, it creates the file and folder structure itself, visible via /memory.
