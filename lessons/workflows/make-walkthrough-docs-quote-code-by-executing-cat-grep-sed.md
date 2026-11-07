---
id: make-walkthrough-docs-quote-code-by-executing-cat-grep-sed
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/
---

# Make walkthrough docs quote code by executing cat/grep/sed, never by retyping snippets

## TL;DR

When asking an agent to write a walkthrough, explainer, or review doc that contains code, instruct it to insert the snippets by running shell commands whose output is captured, so the quoted code is mechanically guaranteed to match the file.

## Why it matters

A doc whose whole purpose is to teach you an unfamiliar codebase is the worst possible place for a hallucinated snippet, and it is the hardest place to catch one because you do not yet know the code well enough to spot the drift. Routing snippets through executed commands makes fabrication structurally impossible rather than merely unlikely.

## How to apply

Add the clause "use sed or grep or cat or whatever you need to include snippets of code you are talking about" to the doc-generation prompt. Willison pairs it with his `showboat` CLI (`uvx showboat --help`; `showboat note` appends Markdown, `showboat exec` runs a command and appends both command and output), but the clause works with any capture mechanism, including a plain `cmd >> doc.md` loop.

## Staleness

The *pattern* is tool-independent and current. REVISIT the tool name: `showboat` is Willison's own utility, written 2026-02; confirm `uvx showboat --help` still works before putting the tool name (rather than the technique) in a project prompt. Nothing in the archive covers this, closest neighbours another lesson and another lesson make different claims.

> "By telling it to use \"sed or grep or cat or whatever you need to include snippets of code you are talking about\" I ensured that Claude Code would not manually copy snippets of code into the document, since that could introduce a risk of hallucinations or mistakes.", Simon Willison
