---
id: park-human-only-notes-in-claude-md-html-comments
created: 2026-09-12
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/simon-scrapes/37-cheat-codes-to-level-up-in-claude-code-in-19-minutes_RDeofKimDxo_20260910.txt
---

# Park Notes-to-Self in CLAUDE.md HTML Comments, Not in Headed Sections

## TL;DR

Anything in CLAUDE.md that exists for you rather than for Claude belongs in an HTML comment block, which can span multiple lines. Only write a heading and a section when the content is meant to change Claude's behaviour.

## Why it matters

Every heading in CLAUDE.md reads as an instruction and spends part of a limited instruction budget, so notes you wrote for your own orientation compete with the rules you actually want followed. The video's rule is blunt: only write subsection headers if they benefit Claude, and put anything that is only for your benefit in comment notation. It goes further and claims Claude spends no tokens on those comments, which is the part to treat as unverified; the durable half is that a heading looks like a directive and a comment does not.

## How to apply

Move orientation notes, reminders and personal context in CLAUDE.md into HTML comment blocks and keep the headed sections for rules you want applied. Audit existing sections with the same test: if deleting it would not change Claude's behaviour, it is a note.

