---
id: route-architecture-planning-to-gpt-for-big-new-projects
created: 2026-09-01
status: active
supersedes: null
category: model-selection
tool: [claude-code, codex]
sources:
  - transcripts/ray-amjad/my-claude-code-workflow-for-2026_20260307.txt
---

# Route Architecture Decisions on Big New Projects to GPT via Codex

## TL;DR

For a project expected to grow large, route the up-front architecture and structuring decisions to GPT-5.2 via Codex even when Opus is doing the actual implementation.

## Why it matters

The reported failure mode is that an architecture chosen early by Opus on a big build later turns out to be a poor fit once the project has grown, so getting a planning-strong model to weigh in early avoids costly rework.

## How to apply

Before starting a project you expect to become large, pass the spec through GPT-5.2/Codex specifically to get structural recommendations, then feed the resulting plan back to Opus/Claude Code for implementation.

## Related

[[bookend-each-work-item-with-the-strongest-model]]
