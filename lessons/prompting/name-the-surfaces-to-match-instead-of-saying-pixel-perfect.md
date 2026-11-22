---
id: name-the-surfaces-to-match-instead-of-saying-pixel-perfect
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/i-tested-14-uncensored-ais-this-one-let-me-do-anything_uox59Sj4z4k_20261112.txt
---

# Replace 'make it pixel perfect' with a named list of surfaces and flows to match

## TL;DR

When asking an agent to reproduce a reference UI, list the specific surfaces and interactions to match instead of asking for 'pixel perfect'.

## Why it matters

The transcript calls 'make it pixel perfect' leaving it to chance, and gives the alternative of naming the chat layout, the sidebar, the new-item flow and the interactions. The source demonstrates this while cloning a third-party desktop app with a refusal-stripped model; the technique is stated here for matching a reference UI you are entitled to copy.

## How to apply

In the prompt, enumerate each screen region and flow that must match (the transcript's list: chat layout, sidebar, new bot flow, interactions).

Checked: No mechanism named.

## Related

[[point-codex-computer-use-at-the-app-youre-cloning]]
