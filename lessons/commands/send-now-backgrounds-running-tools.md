---
id: send-now-backgrounds-running-tools
created: 2026-09-24
status: active
supersedes: null
category: commands
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# ctrl+enter / ctrl+x ctrl+s Now Backgrounds Running Tools Instead of Cancelling the Turn

## TL;DR

The "send now" key combo (ctrl+enter, or ctrl+x ctrl+s), added in 2.1.275 to interrupt the current turn and send all queued messages at once, changed behavior in 2.1.281: it now backgrounds whatever tools are still running instead of killing the current turn outright.

## Why it matters

If you learned this shortcut expecting it to cancel/interrupt (its original 2.1.275 behavior), using it now leaves the in-flight tool call(s) still running in the background rather than stopped, which changes what state you're in afterward, especially for anything with side effects mid-flight.

## How to apply

Use ctrl+enter or ctrl+x ctrl+s when you want to queue-and-send new instructions while letting current tool calls keep running in the background (similar in spirit to Ctrl+B, which backgrounds everything at once); if you actually want to stop the running tools, that's a different action now.

> "Changed send now (ctrl+enter or ctrl+x ctrl+s) to move running tools to the background instead of cancelling the turn", Claude Code CHANGELOG 2.1.281

## Related

[[ctrl-b-backgrounds-all-running-bash-and-subagents-at-once]], [[queue-follow-up-prompts-while-claude-works]]
