---
id: request-platform-native-format-before-clipboard-paste
created: 2026-09-01
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/you-re-using-claude-code-wrong-these-10-tips-will-change-everything_20260307.txt
---

# Ask for the Destination App's Native Format Before Copying Output to Clipboard

## TL;DR

When you're going to paste Claude's output into an app that doesn't render markdown (e.g. LinkedIn), ask Claude to write in that platform's native format (no markdown headers, emoji bullets instead) before you copy it, rather than letting the markdown get mangled on paste.

## Why it matters

The speaker calls out the common pain of copying between Claude and LinkedIn: 'the bullets are lost, the emojis don't appear, the bold doesn't appear.' Asking Claude to 'write in LinkedIn native format with no markdown headers, just use emoji bullets' up front avoids the formatting loss instead of fixing it after the paste.

## How to apply

Before requesting the copy, add an explicit formatting instruction naming the destination, e.g. 'Write this as a LinkedIn post: no markdown headers, use emoji bullets instead of dashes.' Then have Claude copy it to your clipboard and paste directly; no manual reformatting needed.

## Related

[[copy-command-for-formatted-output]]
