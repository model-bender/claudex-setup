---
id: ascii-wireframe-plan-in-terminal-before-coding
created: 2026-07-10
status: active
supersedes: null
category: workflows
sources:
  - transcripts/mark-kashef/plan-like-a-pro-in-claude-code_3qUg57KGSVY_20260703.txt
---

# Wireframe UIs, Decks, and Schemas as ASCII Art in the Terminal Before Writing Any Code

## TL;DR

Before Claude writes code, have it render the landing page / dashboard / slide deck / DB schema as an ASCII-art diagram in the terminal, iterate on that text blueprint over multiple turns, then build only once you and it agree - instead of generating real code you overwrite.

## Why it matters

The default loop is prompt -> generate real code -> dislike it -> regenerate, which burns tokens (slide decks especially are token-hungry) and leaves cross-wired dead code from mismatched versions; a text blueprint aligns you and the model on layout, structure, and relationships for near-zero cost first. It is also the great equalizer for non-technical users - an ASCII table diagram makes a schema's tables and PK/FK relationships legible before any SQL exists.

## How to apply

Prompt 'before writing any code, create an ASCII wireframe of X' (sidebar, stat cards, two charts, data table); iterate with targeted edits ('make the line chart wider than the pie chart, redraw the full wireframe'); for decks add 'no PowerPoint yet, just labeled boxes' so it does not prematurely fire the PowerPoint skill; for a schema ask for tables with PK/FK relationships and have it re-explain 'as if I am in seventh grade' if unclear; then say 'build this, use the wireframe as the exact specification' and spin it up on localhost.
