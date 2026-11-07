---
id: turn-a-computer-use-workflow-into-a-cli-then-run-it-on-a-cheaper-model
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/mark-kashef/gpt-6-astra-s-computer-use-is-ridiculously-good_tU-fO6cADvQ_20260910.txt
---

# Have Computer Use Build You a CLI the First Time, Then Run the CLI on a Cheaper Model

## TL;DR

For a site with no API or MCP, let a strong model drive it once with computer use and reverse-engineer a reusable command line interface. Every run after that is the CLI, which any agent or cheaper model can call.

## Why it matters

Mark Kashef measured both paths on the same flight searches: Toronto to Lisbon went from 77 seconds with vanilla computer use to 23 with the generated CLI, and Toronto to Seoul from 50 seconds to 25. His framing of why it is worth the first expensive run: 'you can have Astra do the hard work the first time, and then you can execute this workflow with a lower level model.' A computer-use run is slow, non-deterministic and needs the strongest model; a CLI is fast, scriptable, schedulable and runs anywhere, so paying once to cross that boundary pays back on every subsequent run.

## How to apply

Prompt for the artefact, not the answer: 'build a reusable command line interface for <task on this site> for these parameters, I want to reuse it as a scheduled task.' Then push it past your first case, ask whether it generalises to any combination of inputs and have it test the awkward variants. Finally benchmark honestly: run the same fresh request twice in separate sessions, once through the CLI and once through plain computer use, and keep the CLI only if it actually wins.

## Related

[[cli-anything-wraps-any-repo-as-an-agent-drivable-cli]], [[cli-tools-over-mcp-for-tokens]]
