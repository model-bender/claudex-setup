---
id: reference-files-from-claude-md-by-path-with-a-when-to-open-line-not-at-import
created: 2026-10-19
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/simon-scrapes/how-the-top-1-use-claude-code-differently_J9NQTYUP6k0_20261013.txt
---

# Point CLAUDE.md at Other Files by Backticked Path With a When-to-Open Line, Not an @-Import

## TL;DR

Write 'read the client brief before any client work' with the path in backticks. An @-import pulls the whole file into every session.

## Why it matters

Simon Scrapes treats CLAUDE.md as a contents page: only tools Claude cannot guess, your deviations from the norm, repeat gotchas and boundaries stay in it. Everything else is a pointer that loads only when relevant.

## How to apply

Replace @imports of situational files with a path in backticks plus the trigger ('read X before any Y work'). Link every such file directly from CLAUDE.md, since the transcript says Anthropic's docs preview only the first 100 lines of a file reached only through another file. Add a contents list at the top of files over 100 lines (a rule the transcript says Anthropic set for skill files, which he applies to everything the index points at). Checked: @path/to/import syntax is documented and present in the 2.1.303 binary (4 hits). That imports are loaded in full at session start is the transcript's claim and standard import behaviour, not re-verified here. The 100-line preview claim is also unverified here.

## Related

[[add-a-contents-list-to-skill-reference-files-over-100-lines]], [[link-every-skill-reference-file-directly-from-skill-md]], [[root-claude-md-as-pure-router-nested-for-specifics]]
