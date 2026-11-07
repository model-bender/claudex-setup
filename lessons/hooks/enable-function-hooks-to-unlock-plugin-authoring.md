---
id: enable-function-hooks-to-unlock-plugin-authoring
created: 2026-09-12
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Start Claude Code With CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 to Get the plugin-authoring Skill

## TL;DR

Function hooks sit behind an environment flag. Launch with CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude and a built-in plugin-authoring skill appears, which writes and debugs plugins made of function hooks from a plain-English description.

## Why it matters

Function hooks are middleware around every tool call rather than the allow-or-block shell hooks, so they can rewrite input, cache results, add UI, ask questions, register tools and keep state. Hand-writing that wiring is where people give up; the authoring skill produced a working 300-line hook plus plugins.json and hooks.json from one sentence in the demo.

## How to apply

Run CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude, then /plugin-authoring and describe the behaviour you want. Add 'feel free to interview me and give me a few prototypes to play with before you code this up' for anything with a UI or a judgment call. Run /reload plugins afterwards to activate what it wrote.

## Related

[[reload-plugins-after-a-repo-local-plugin-install]]
