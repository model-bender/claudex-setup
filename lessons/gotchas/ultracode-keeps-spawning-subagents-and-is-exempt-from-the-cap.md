---
id: ultracode-keeps-spawning-subagents-and-is-exempt-from-the-cap
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/how-the-top-1-use-claude-code-differently_J9NQTYUP6k0_20261013.txt
---

# Know that ultracode orchestrates repeated sets of subagents and ignores the subagent cap

## TL;DR

With ultracode on, Claude plans workflows for substantive tasks, sometimes several in a row for one request, and the session's concurrent subagent limit is not enforced. Do not expect that cap to contain it.

## Why it matters

The presenter describes ultracode as an effort level that can build out subagents indefinitely. Corrections from the docs: ultracode is a Claude Code setting, not a model effort level, and 'indefinitely' is too strong, because each workflow run keeps its own runtime caps (up to 16 concurrent agents by default, 1,000 agents total per run). With it on, every request uses more tokens, and the session limit on concurrent subagents (20 by default, set by `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`) is not enforced.

## How to apply

Leave ultracode off for routine work. Turn it on per session with /effort ultracode and off with /effort ultracode off (v2.1.284 or later), and expect higher usage while it is on.

Checked: Live docs model-config.md, workflows.md and sub-agents.md (fetched 2026-11-22): 'Ultracode is a Claude Code setting rather than a model effort level'; sessions with ultracode active are exempt from the concurrent subagent limit; workflows.md 'Behavior and limits' gives the 16 concurrent and 1,000 total agents per run. Installed binary Claude Code 2.1.330 contains 'ultracode' (72 matches).

## Related

[[use-dynamic-workflows-for-high-value-complex-work]]
