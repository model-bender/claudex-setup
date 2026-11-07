---
id: ban-react-in-artifacts-so-the-code-copies-straight-out-to
created: 2026-08-22
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/guides/agentic-engineering-patterns/prompts/
---

# Ban React in artifacts so the code copies straight out to static hosting

## TL;DR

Put a standing "no React, plain HTML/vanilla JS/CSS with minimal dependencies" instruction in the project you use for building artifacts, so every prototype is a file you can paste onto static hosting unchanged.

## Why it matters

Models default to React for artifacts, and React introduces a build step, which is precisely what stops you copying the artifact out and hosting it anywhere. The constraint converts every throwaway prototype into a permanently reusable asset, which is what makes the "hoard things you know how to do" pattern in the same guide compound.

## How to apply

Set it as custom instructions on the Claude project you use for artifacts. Willison's block also pins house style so output is drop-in: two-space indents, CSS starting with a `* { box-sizing: border-box; }` reset, inputs and textareas at 16px, Helvetica-first font stack, `<script type="module">`, Sentence case headings.

## Staleness

Current, and if anything strengthened: the Artifact tool in this harness enforces self-contained pages via CSP (external hosts, including CDN scripts, are blocked, Google Fonts is the only exception), so a CDN React build would not load at all. Scope note for whoever writes this up: the source is about claude.ai chat Artifacts / project custom instructions, so state the target explicitly rather than implying it is a Claude Code setting. Not covered by [[html-as-default-artifact-not-markdown]], which argues HTML over Markdown for plans, not vanilla JS over React.

> "Never use React in artifacts - always plain HTML and vanilla JavaScript and CSS with minimal dependencies.", Simon Willison
