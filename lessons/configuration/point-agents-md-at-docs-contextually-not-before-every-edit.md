---
id: point-agents-md-at-docs-contextually-not-before-every-edit
created: 2026-09-13
status: active
supersedes: null
category: configuration
source_type: post
tool: [codex, claude-code]
sources:
  - https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
---

# Replace a Read-These-Docs-Before-Every-Edit Rule With Per-Topic Pointers

## TL;DR

A blanket instruction to read a doc stack before every edit burns context on every trivial change; scope each pointer to the topic that should trigger it.

## Why it matters

A capable model already works out what it needs to read, so the blanket rule buys no accuracy and costs context on every turn, including a typo fix. This is the counterweight to the advice about moving repeated constraints into an instruction file: that says when to add a rule, this says when a rule has grown too broad to keep.

## How to apply

Rewrite "before every edit, read architecture.md, database.md and deployment.md" as "use architecture.md for service boundaries, database.md for schema changes, deployment.md when preparing a deployment", so each doc is consulted only when its topic is in play.

> "Prompting the model to read files before every edit is a great way to burn context and slow work down. Pointing to some docs can still be helpful, however, so long as it is contextual.", OpenAI developers blog
