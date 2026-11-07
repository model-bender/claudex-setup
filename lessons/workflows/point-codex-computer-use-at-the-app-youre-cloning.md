---
id: point-codex-computer-use-at-the-app-youre-cloning
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/mark-kashef/cursor-accidentally-exposed-grok-bot-s-blueprint_mAWT1HCBgbQ_20260910.txt
---

# Point Codex's Computer Use at the App You Are Cloning, Not Just Its Docs

## TL;DR

When rebuilding something that already exists, have Codex drive the reference app through computer use and observe its real behaviour while it builds your version.

## Why it matters

Kashef calls this his expert tip on the rebuild: he used Codex to build the app and also to look at the original's performance and behaviour directly, so the clone matched how the thing actually acts rather than how a write-up describes it. A description (or a leaked repo) tells you the structure; watching the running app tells you the interaction details that never make it into prose, which is where a reimplementation usually feels wrong.

## How to apply

Install the Codex computer use plugin, open the reference app, and give Codex a specific observation brief (walk this flow, note what happens on each state change) rather than a vague 'look at it'. Keep the observed behaviour in notes it can consult while implementing, and supervise the session, computer use drives a real screen.

## Related

[[codex-computer-use-installs-as-a-plugin-and-refuses-os-privacy-settings]], [[point-computer-use-at-a-product-s-docs-to-self-configure-it]], [[clone-reference-codebase-to-tmp]]
