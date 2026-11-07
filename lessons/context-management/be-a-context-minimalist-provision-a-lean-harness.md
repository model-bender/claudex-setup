---
id: be-a-context-minimalist-provision-a-lean-harness
created: 2026-07-17
status: active
supersedes: null
category: context-management
source_type: post
sources:
  - https://www.theneuron.ai/explainer-articles/claude-code-creators-boris-cherny-and-cat-wu-explain-how-to-use-agent-loops/
---

# Be a Context Minimalist: Provision a Lean Harness and Let Claude Pull the Rest

## TL;DR

Deliberately start with a minimal system prompt / CLAUDE.md and a minimal tool set, then give Claude a way to fetch context on demand, rather than front-loading everything "just in case."

## Why it matters

Over-stuffing the harness micromanages the model and crowds out the user's actual prompt; the Claude Code team's own default is a lean system prompt plus just-in-time retrieval. Starting minimal is a proactive design choice, not the reactive bloat-trimming that `/context` and `/checkup` do after the window is already full.

## How to apply

Strip CLAUDE.md and the tool list to essentials, tell the model only what the current task needs, and rely on exploration/retrieval for the rest instead of pre-loading files. Treat every added instruction and tool as a cost to justify, not a default.

> "Cat calls herself 'a context minimalist': tell the model only what it needs, then let it choose the route.", Cat Wu (via The Neuron)

## Related

[[write-human-docs-as-mental-models-let-agents-fetch-details]], [[run-checkup-doctor-to-audit-setup-health-and-context-bloat]], [[skill-md-under-200-lines-progressive-disclosure]]
