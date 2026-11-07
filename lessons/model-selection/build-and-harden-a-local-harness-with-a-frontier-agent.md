---
id: build-and-harden-a-local-harness-with-a-frontier-agent
created: 2026-08-16
status: active
supersedes: null
category: model-selection
tool:
  - claude-code
  - codex
about: local models
sources:
  - transcripts/mark-kashef/3d-websites-just-became-free-one-prompt_FSnubu4Lpz8_20260812.txt
---

# Have a Frontier Agent Build and Keep Improving the Harness Your Local Model Runs In

## TL;DR

Point Codex or Claude Code at your local agent harness and its skills and have it hack them until the local model completes the target process end to end. The frontier model authors the substrate once; the local model then spends free tokens executing on it.

## Why it matters

A local model in the 27B-40B range is not the bottleneck for this class of work - the harness around it is: task management, a self-checking loop, a skill router, and the domain skills. Those are exactly the artifacts a frontier model writes well, and once written they cost nothing to run.

The creator had Codex read his harness and build the skills it needed rather than writing them himself, and had Fable teach it browser use so it could open a browser and check its own output. On the live build, that loop recovered a completely blank first render with no intervention.

This is the same move as using a premium model to refactor load-bearing code for a cheaper default, applied to the agent harness instead of the codebase - and it is what makes routing to cheap or local models actually pay off.

## How to apply

Give the frontier agent read access to the harness and name the process you want to work ("make this good enough to build a scroll-scrubbed 3D site"), and have it write the skills rather than authoring them yourself.

Transplant capabilities the same way: ask the strong model to teach the harness to launch a browser and verify its own rendered output. Treat it as a standing job rather than a one-off, having the frontier model periodically re-read and improve the harness as the local model changes. When the local stack is not installed yet, hand the frontier agent the download links and let it do the installation and troubleshooting.

## Related

[[over-explain-the-procedure-when-the-harness-runs-a-local-model]], [[refactor-load-bearing-code-with-premium-model-for-cheaper-default]], [[route-claude-code-to-cheaper-or-local-models]]
