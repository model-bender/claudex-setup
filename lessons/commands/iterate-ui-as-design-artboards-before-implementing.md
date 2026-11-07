---
id: iterate-ui-as-design-artboards-before-implementing
created: 2026-08-29
status: active
supersedes: null
category: commands
source_type: post
tool: claude-code
sources:
  - https://x.com/ClaudeDevs/status/2089471692762673408
---

# Use /design to Iterate UI as Editable Artboards Before Asking Claude to Implement One

## TL;DR

The /design skill (research preview) brings the artboard workflow into Claude Code and Desktop, built on artifacts: generate variant artboards, pick and tweak one, then have Claude implement the chosen board.

## Why it matters

Choosing among editable artboards before any code exists avoids the expensive tweak-the-implementation loop, where each visual adjustment costs a code round-trip. Picking the direction first means the implementation pass starts from an approved design.

## How to apply

Run `/design` in Claude Code, select and adjust an artboard in the published artifact, then tell Claude to implement the chosen artboard. Verified via the r.jina.ai mirror of Boris Cherny's timeline (quote-tweeted by him on 2026-08-17).

> "Run /design to get editable artboards for your UI — pick one, tweak it, then have Claude implement it.", Claude Code team (@ClaudeDevs)

## Related

[[interactive-html-artifacts-for-design-decisions]], [[hand-off-claude-design-exports-to-claude-code]]
