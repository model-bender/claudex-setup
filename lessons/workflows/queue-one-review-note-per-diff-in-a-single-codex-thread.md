---
id: queue-one-review-note-per-diff-in-a-single-codex-thread
created: 2026-10-19
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/john-kim/stop-using-codex-in-terminal-it-s-holding-you-back_yK9GnaE9rlY_20261017.txt
---

# While Reading a Stack of Diffs, Queue One Note Per Diff in the Same Codex Thread

## TL;DR

Read a diff, write a short note, queue it, move to the next diff, and let the agent work through maybe 20 notes in one thread so all related context stays together.

## Why it matters

John Kim does this for stacks of PRs: the changes are related, so one thread keeps the context. In the app queued prompts can also be reordered by dragging, edited, removed or steered directly, and a queued prompt waits until the running goal finishes (so it can run while you sleep).

## How to apply

1. Start the goal or task. 2. As you review each diff, queue a note. 3. Reorder or edit the queue in the app, or click steer on one to inject it now. Checked: app UI behaviour is the speaker's, not verifiable from codex-cli 0.163.0; related Codex queue behaviour is already in the library.

## Related

[[queue-follow-up-prompts-while-claude-works]]
