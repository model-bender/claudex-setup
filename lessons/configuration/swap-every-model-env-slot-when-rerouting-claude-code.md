---
id: swap-every-model-env-slot-when-rerouting-claude-code
created: 2026-08-29
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/this-stealth-model-makes-claude-code-free-here-s-how__kK_4cOYF4o_20260824.txt
---

# When rerouting Claude Code to another provider, replace the model in every env slot or subagents will spawn on a different model

## TL;DR

The BYO-model env block has multiple model slots, not one; if you only change the main model, a session that spawns a "Sonnet" subagent (or any implicit small-model call) will route that spawn to whatever is left in the other slots. Paste the substitute model id into every slot.

## Why it matters

Subagent spawns and small-fast-model calls resolve their model from separate settings, so a partial edit produces a mixed fleet: your main loop on the free/cheap model, subagents on something else, with cost, capability, and data-destination implications you didn't choose. The creator is explicit: "if your session invokes different sub-agents, and it wants to make like a Sonnet sub-agent... that's why you want to switch out all of those when you want all of them to actually be the same model."

## How to apply

In .claude/settings.json's env block, after setting ANTHROPIC_AUTH_TOKEN to your OpenRouter key, copy the target model slug (e.g. stealth/ox-alpha or z-ai/glm-5.2:free from the OpenRouter model page) into every model variable in the block, the main model and each subagent/small-model slot, then save and open a fresh session. To change models later, find-and-replace every instance of the old slug, not just the first. Verify with a task that spawns a subagent and check which model it ran on.

## Related

[[claude-code-subagent-model-is-now-a-default-not-an-override]], [[route-claude-code-to-cheaper-or-local-models]], [[set-anthropic-default-model-not-anthropic-model-when-you-want]]
