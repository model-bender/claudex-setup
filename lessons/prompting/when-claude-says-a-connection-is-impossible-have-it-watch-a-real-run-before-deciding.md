---
id: when-claude-says-a-connection-is-impossible-have-it-watch-a-real-run-before-deciding
created: 2026-10-11
status: active
supersedes: null
category: prompting
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/these-mods-take-claude-code-to-another-level_UcvD53jqHRU_20261009.txt
---

# When Claude says a hacky integration is impossible, have it watch a working run of the target tool first

## TL;DR

Mark's pattern: open the other app, run the feature while Claude listens to the tools being called, and only then let it decide if the connection is possible; he also says to make it distinguish a missing tool in this chat from a capability that can be implemented.

## Why it matters

Mark says Claude often claims such connections are impossible from the start, and when you make it observe a real run it usually realizes it was wrong. He used it to build a mod that lets Claude Code drive Codex's computer use through an MCP bridge, and a threads mod that spins up helper sessions on chosen models.

## How to apply

Prompt along the lines of: I am about to open the Codex app and run computer use; listen in for all the tools being run behind the scenes. In the build prompt say: before deciding a feature is impossible, inspect the installed mod authoring API and the current CLI help, and distinguish a missing tool in this chat from a capability that can be implemented. Point it at claude --help so it can find the flags it needs (Mark mentions this for choosing models). If it keeps refusing, throw a /goal at it that says to battle test it step by step (one thread, then two).

Checked: grep -c -a '/goal' on the 2.1.296 binary: 25; claude --help is a real CLI command

## Related

[[spike-the-whole-automation-chain-before-polishing-any-step]]
