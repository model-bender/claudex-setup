---
id: skip-goal-command-and-ralph-loops-by-default
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/ray-amjad/openai-and-anthropic-agree-on-what-comes-after-loops_yrRpnx_iugY_20261106.txt
---

# Stop wrapping every task in /goal or a Ralph loop

## TL;DR

With current models, state a clear goal and give the right tools, and the agent keeps going on its own. Reach for /goal or a Ralph loop only when that fails, not by default.

## Why it matters

The speaker relays OpenAI's point that earlier models did not know when they were done and had to be pushed from outside, and that this behaviour has since been trained into the models. The speaker says /goal is now rarely needed, and that current models also judge better when a goal is impossible.

## How to apply

Drop the outer loop from routine tasks. Instead, write a clear goal into the prompt and give the agent access to the tools it needs to reach it.

Checked: Claude Code 2.1.330 binary (command grep -a on the installed binary): `/goal` still exists ('Set a goal Claude checks before stopping'); code.claude.com/docs/en/goal.md documents it. Codex live docs (learn.chatgpt.com/docs/codex-manual.md, fetched 2026-11-22; codex-cli 0.171.0 installed): `/goal` documented for the desktop app, CLI and IDE extension. The 'rarely needed' claim is the speaker's experience, not a deprecation.

