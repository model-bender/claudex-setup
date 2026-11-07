---
id: run-ultracode-at-low-effort-for-wide-read-heavy-work
created: 2026-11-06
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1xks0kb/psa_ultracode_isnt_locked_to_max_effort_anymore/
---

# Ultracode Is a Separate Toggle From Effort: Run the Orchestration at Low Effort for Big Audits

## TL;DR

Ultracode no longer forces the top effort level: pick the effort you want in /effort and toggle Ultracode on top of it, which keeps the multi-agent workflow at a fraction of the usage.

## Why it matters

People skip Ultracode on cost grounds when what they want from it is the fan-out and verify passes, not maximum reasoning per turn, and audits or research sweeps are exactly that case.

## How to apply

Run /effort, select Low or Medium, toggle Ultracode on in the same slider, and use it for wide read-heavy work; raise the effort only when the thinking itself is the bottleneck.

Checked: claude 2.1.318 binary: effortSlider:toggleUltracode 3 hits, a keybinding on the effort slider separate from increaseEffort and decreaseEffort.

> "you still get the full workflow orchestration (multiple agents, verify passes, the whole thing), but the thinking runs at low effort, so it burns way less of your usage.", u/CoderLuii on r/ClaudeAI

## Related

[[check-ultracode-is-actually-in-effect-before-trusting-an-ultracode-run]]
