---
id: hook-based-memory-injection-beats-mcp-tool-call-for-reliability
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-memory-system-compared-so-you-don-t-have-to_20260424.txt
---

# Prefer a Hook-Based Memory Auto-Inject Over an MCP Memory Tool the Model Must Choose to Call

## TL;DR

mem-search auto-injects your top semantic memory matches into every prompt via a hook, while MCP-based memory tools like claude-mem require the model to actively decide to call a search tool, so a memory that matters can simply not get retrieved.

## Why it matters

Retrieval you depend on for continuity should not be conditional on the model choosing to invoke a tool; a hook that runs unconditionally on every prompt makes recall reliable at the cost of always paying for the lookup.

## How to apply

If reliable recall of past decisions matters more than dashboards or MCP tooling, choose a memory setup that injects context via a hook (e.g. on every user prompt) rather than one that exposes memory only as an MCP tool the model must decide to invoke.

## Related

[[semantic-hybrid-memory-search-with-reranking]]
