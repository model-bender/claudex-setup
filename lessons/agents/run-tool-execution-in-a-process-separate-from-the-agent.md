---
id: run-tool-execution-in-a-process-separate-from-the-agent
created: 2026-09-12
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - https://hamel.dev/notes/llm/ai-product-engineering/systems-agent-sandboxes.html
---

# Run Tool Execution in Its Own Process So a Tool Crash Does Not Kill the Agent Run

## TL;DR

A tool that loads a large CSV and runs out of memory should take down the tool process, not the hours-long agent trajectory it was serving.

## Why it matters

The asymmetry is the whole argument: the trajectory is the expensive, unrepeatable part, and an in-process tool crash costs you all of it for a failure that had nothing to do with the agent's reasoning. Agents that work for hours or days also edit their own environment's dependencies mid-run, so the tool surface is exactly where unexpected crashes come from. The parent lesson's own body calls this 'the separate point', but its TL;DR is entirely about pre-baking images.

## How to apply

When you host your own agent loop, execute tools in a subprocess or separate sandbox rather than inside the agent process, and hand a tool crash back to the agent as a returned error it can react to. Cap the tool process's memory so a runaway tool fails fast instead of taking the host down with it.

## Related

[[pre-baked-machine-images-not-ci-for-agent-sandboxes]]
