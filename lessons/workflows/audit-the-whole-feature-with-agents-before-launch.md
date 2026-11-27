---
id: audit-the-whole-feature-with-agents-before-launch
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/john-kim/how-i-review-ai-code-meta-senior-staff-engineer_b2QkhmQ0sT0_20260923.txt
---

# Treat merge-ready as not launch-ready: audit the whole feature with agents first

## TL;DR

After the gated pieces have landed, run a set of agents over all the code written for the feature before you launch it, looking at performance, bugs, security and whether it works to spec.

## Why it matters

Reviewing leaf code by skimming gets the feature landed fast but, by the speaker's estimate, only about 80% done. He says the remaining 20% (audit, refactor, cleanup, detail work) takes as long as the first 80%, is the most important part, and is where his own effort and taste go.

## How to apply

Before flipping the gate: have several agents audit the full set of changes for the feature at a high level (performance, bugs, security, conformance to the spec), then refactor and clean up from their findings and polish the details yourself. Budget as much time for this as for the build.

Checked: No mechanism named.

## Related

[[ask-the-agent-for-non-functional-requirements-then-test-cases-for-your-app]]
