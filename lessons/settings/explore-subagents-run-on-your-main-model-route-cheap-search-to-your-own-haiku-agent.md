---
id: explore-subagents-run-on-your-main-model-route-cheap-search-to-your-own-haiku-agent
created: 2026-10-19
status: active
supersedes: null
category: settings
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1x0kzbh/haiku_55_is_40x_cheaper_than_opus_55_your_explore/
  - https://www.reddit.com/r/ClaudeCode/comments/1x0kzbh/haiku_55_is_40x_cheaper_than_opus_55_your_explore/pelvavy/
---

# Explore Subagents Run on Your Main Model: Route Cheap Search to Your Own Haiku Agent

## TL;DR

The built-in Explore agent no longer runs on Haiku: it inherits your main session's model (capped at Opus), so on an Opus session every Explore fan-out bills at Opus rates, and `CLAUDE_CODE_SUBAGENT_MODEL` alone does not move it.

## Why it matters

Advice written before 2.1.198 assumes Explore is the cheap Haiku searcher, including tips to remap Haiku to Sonnet so Explore plans better; that remap now changes nothing for Explore. The only switch that does move Explore, `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`, is all or nothing: it also overrides every agent file's `model:` line and every per-spawn model, so implementer agents you pinned to Sonnet or Opus get pulled down too.

## How to apply

For cheap code search, define your own read-only agent with `model: haiku` (one reply in the thread calls it "scout") and tell your user CLAUDE.md to use it for searching, rather than relying on Explore. Use `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` only when you really want every subagent on one model. Checked against Claude Code 2.1.303: the changelog says "The built-in Explore agent now inherits the main session's model (capped at opus) instead of running on haiku" (2.1.198) and that `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` ignores "per-spawn and agent-definition model overrides" (2.1.257); the binary's built-in Explore definition carries `model:"inherit"` with an `"opus"` cap, and an agent definition's model beats `CLAUDE_CODE_SUBAGENT_MODEL` since 2.1.251, which is why the plain variable does not reach it.

> "Worth knowing: Claude Code's built-in Explore subagent no longer runs on Haiku. It uses your main model, so on Opus 5.5 every Explore run goes through Opus.", u/emarkosov on r/ClaudeCode

> "Just create subagents files. Create one named "scout", set it to haiku, and in your user Claude.md tell it to use that agent for searching", u/muikrad on r/ClaudeCode

## Related

[[claude-code-subagent-model-is-now-a-default-not-an-override]], [[give-code-search-subagents-to-haiku-but-keep-fact-checking-on-opus]], [[restate-critical-rules-in-subagent-prompts-explore-and-plan-skip-claude-md]]
