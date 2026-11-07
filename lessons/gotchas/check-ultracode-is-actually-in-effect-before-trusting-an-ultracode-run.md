---
id: check-ultracode-is-actually-in-effect-before-trusting-an-ultracode-run
created: 2026-10-02
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-had-opus-5-5-build-me-the-same-app-at-every-effort-level_QCkHIyEPIYo_20261002.txt
---

# If an Ultracode Run Looks Like Plain Extra Effort, Check That Dynamic Workflows Are Actually Available

## TL;DR

Ultracode only does anything when dynamic workflows are enabled and the model supports it. A run that never spawns a workflow may simply not have had ultracode in effect.

## Why it matters

The creator ran six effort levels including ultracode on one big build and found that ultracode never spun up a dynamic workflow in the session logs, across several tries. They could not tell whether this was a harness bug or a model limitation. The Claude Code binary describes ultracode as standing dynamic-workflow orchestration that requires workflows to be enabled and a model that supports it, and it tracks 'requested' separately from 'available' and 'in effect'. That makes 'requested but not in effect' a likely explanation (the lesson's inference, not something the creator confirmed).

## How to apply

When you choose ultracode (the `ultracode` settings key or `/effort ultracode`), confirm it took effect by checking the session log or transcript for workflow or subagent activity rather than assuming from the label. If none appears, check that workflows are enabled and that the model you are on supports ultracode. If you cannot get it working, plain `xhigh` is the fallback the creator effectively ran.

Verified: Claude Code 2.1.287 binary: `ultracode` settings key and `/effort ultracode` text, description 'Requires workflows to be enabled and a model that supports ultracode', and separate ultracodeRequested/ultracodeAvailable/in-effect fields. `claude --help` lists effort levels low, medium, high, xhigh, max. That the creator's extra level equals xhigh is the lesson's assumption.

Corrected 2026-10-02: since 2.1.284 Ultracode is its own toggle in `/effort` and no longer forces xhigh, so an Ultracode run is not "extra effort" and turning it off (`/effort ultracode off`) leaves your effort level as set. The xhigh fallback above describes the older behaviour.

> "Changed Ultracode into its own toggle in `/effort` (Tab, or `/effort ultracode [on|off]`): it no longer forces xhigh effort and stays on at any effort level", Claude Code CHANGELOG 2.1.284

## Related

[[use-dynamic-workflows-for-high-value-complex-work]], [[max-effort-is-a-trap-quality-plateaus-at-high]]
