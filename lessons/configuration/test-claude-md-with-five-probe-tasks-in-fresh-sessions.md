---
id: test-claude-md-with-five-probe-tasks-in-fresh-sessions
created: 2026-11-06
status: active
supersedes: null
category: configuration
tool: [claude-code, codex]
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xf2pkt/stop_paying_to_polish_agentsmd_claudemd_keep_it/
---

# Test CLAUDE.md With Five Probe Tasks in Fresh Sessions Instead of Rewriting It Again

## TL;DR

Instead of growing the instruction file after each miss, keep a fixed set of five probe prompts, run each in a fresh session, kill it as soon as you see the first moves, and change one line only when a probe fails.

## Why it matters

Adding a paragraph per ignored rule is what makes the file too long for any rule to land, and without probes you have no signal on whether an edit helped; the probes also show which failures belong in a hook or permission rather than in prose.

## How to apply

Write five prompts that each exercise one rule (test command, migrations, no new package, read the ADR first, stop before pushing), run them cold, and when one fails ask whether a tool can enforce it before touching the wording, then re-run all five.

Checked: the post's companion claims are real in 2.1.318: `prompt-audit` (14 hits, the /doctor subcommand it names) and the AGENTS.md and CLAUDE.local.md loading surfaces (19 and 30 hits).

> "Five probe tasks, each in a fresh session, stopped as soon as you see the first moves:", u/SirRobinBlibs on r/ClaudeCode

