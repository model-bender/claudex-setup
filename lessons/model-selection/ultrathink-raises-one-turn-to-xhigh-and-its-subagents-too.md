---
id: ultrathink-raises-one-turn-to-xhigh-and-its-subagents-too
created: 2026-11-06
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: canonical
sources:
  - https://x.com/dmwlff/status/2115625812640854153
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  - https://x.com/dmwlff/status/2115627642959565243
---

# ultrathink Raises One Turn to xhigh, Subagents Spawned in It Included, Without Breaking the Prompt Cache

## TL;DR

Since 2.1.311, typing ultrathink in the terminal runs that turn at xhigh effort on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1, and any subagents spawned in the turn run at xhigh too; the session then returns to its set effort.

## Why it matters

It lets you run medium by default and pay for xhigh only on the turns that need it. Adam Wolff (Claude Code) says newer models switch effort without breaking the prompt cache. This replaces the older lesson that ultrathink raises effort to high and is a no-op on high.

## How to apply

Stay on medium and put ultrathink in the one prompt that needs depth, such as the first research turn on a bug. Expect that turn's subagents to run at xhigh too. It does nothing if the session is already on xhigh.

Checked: claude 2.1.318 binary: ultrathink 39 hits, xhigh 40; the 2.1.311 CHANGELOG line reads "Changed ultrathink in the interactive terminal to run its turn at xhigh effort on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 through Anthropic's API". Subagent inheritance rests on Wolff's post, not tested here.

> "it's just an effort change to xhigh for one turn. any subagents spawned in that turn will also run at xhigh.", Adam Wolff (@dmwlff), Claude Code engineer

## Related

[[extended-thinking-on-by-default-with-budget-cap]]
