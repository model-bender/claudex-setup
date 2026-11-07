---
id: spin-up-parallel-threads-at-different-effort-levels-from-one-prompt
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: [codex, claude-code]
sources:
  - transcripts/mark-kashef/i-tested-every-gpt-6-astra-effort-level-here-s-what-i-d-use_OQipTxv9Qv0_20260910.txt
---

# A/B an Effort Level by Asking the Agent to Spin Up Renamed Parallel Threads Itself

## TL;DR

Instead of opening several chats by hand, tell Codex (or Claude) to create N threads running the identical prompt, each at a different effort level, renamed in the sidebar and started at the same time.

## Why it matters

Comparing effort levels or model settings is only meaningful if the context, tools, scope and timing are identical, and doing it by hand guarantees drift plus a sidebar of unlabelled chats you cannot tell apart later. Kashef ran seven threads this way over one research-and-build prompt and could attribute the differences to the effort level alone, including time and token counts per thread. The agent creating its own threads is what makes the controlled comparison cheap enough to actually run.

## How to apply

In one message, tell the agent to take the exact prompt, create the threads (one per level), rename each one after its level so the sidebar is readable, pin them in a folder, start them all at the same time, and monitor progress. Check the recents list to confirm each thread opened with the identical task. Kashef notes this works in both Claude and Codex.

## Related

[[name-your-sessions-so-they-can-message-each-other]]
