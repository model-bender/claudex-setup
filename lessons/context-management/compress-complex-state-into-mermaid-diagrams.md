---
id: compress-complex-state-into-mermaid-diagrams
created: 2026-08-31
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-concept-explained-for-normal-people_20260307.txt
  - transcripts/simon-scrapes/the-easiest-way-to-get-ahead-with-claude-code_20260424.txt
  - transcripts/simon-scrapes/200-hours-of-claude-code-lessons-in-14-minutes-for-business-owners_20260424.txt
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
  - transcripts/andrew-codesmith/master-95-of-claude-code-in-15-mins-as-a-beginner_20260424.txt
---

# Describe Complex State With a Mermaid Diagram Instead of Thousands of Tokens of Prose

## TL;DR

A Mermaid diagram conveys what thousands of tokens of text would, so express complex state descriptions as diagrams to spend far fewer tokens on the same information.

## Why it matters

Long prose descriptions of complex state are one of the quiet ways a context window fills up, and the tokens they burn crowd out the work itself. A Mermaid diagram carries the same structural information in a fraction of the tokens, so the model gets an equally clear picture of the state at much lower context cost.

## How to apply

When you need to convey complex state to Claude, write it (or ask Claude to write it) as a Mermaid diagram rather than a long textual description. Reach for this wherever a state description would otherwise run to thousands of tokens.

## Related

[[context-rot-prevention-compact-proactively]]
