---
id: ship-agents-md-with-architecture-and-hard-rules-for-agent-led-setup
created: 2026-11-22
status: active
supersedes: null
category: configuration
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/how-to-use-any-ai-model-in-grokbot_Jq3WcqtakNQ_20260910.txt
---

# Ship an AGENTS.md with the architecture and non-negotiable rules so a user's agent can install your tool

## TL;DR

For a fragile or experimental tool, write the repo so a coding agent can set it up: an AGENTS.md that explains the architecture and lists non-negotiable rules such as the host app version it requires, next to the README.

## Why it matters

The speaker built his router on a Mac, so it works most smoothly on macOS, and expects it to need upkeep as the host app keeps updating. He gives the repo enough instructions (an AGENTS.md and the README) that a user can "theoretically" feed it to Codex, Claude or another agent and ask it to set the tool up on their machine. His AGENTS.md walks through the architecture and then a list of non-negotiable rules, one of which pins the host app version. He does not report anyone completing such an agent-led install, so treat that half as a proposed, untested pattern.

## How to apply

In AGENTS.md describe the components and how they connect, then list the hard rules (required versions, things that must not be changed). Tell users to open the repo in their agent and ask it to set the tool up for their OS. This lesson's inference: try that yourself on a second machine before you rely on it.

Checked: Codex docs (learn.chatgpt.com/codex/agent-configuration/agents-md, fetched 2026-11-22): Codex reads `AGENTS.md` files before doing any work. Claude Code docs (memory.md, fetched 2026-11-22): Claude Code 2.1.277 and later reads a repo's `AGENTS.md` when there is no `CLAUDE.md` (installed version 2.1.330). The speaker's repo was not inspected.

## Related

[[feed-unfamiliar-repo-link-for-fan-out-install-plan]]
