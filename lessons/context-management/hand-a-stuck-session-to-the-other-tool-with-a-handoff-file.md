---
id: hand-a-stuck-session-to-the-other-tool-with-a-handoff-file
created: 2026-07-17
status: active
supersedes: null
category: context-management
tool:
  - claude-code
  - codex
sources:
  - transcripts/nate-herk-ai-automation/how-to-use-your-claude-code-projects-in-codex-in-5-mins_kB9iMD0EjT8_20260627.txt
---

# When One Tool Is Stuck, Hand the Session to the Other One: Not Just to a Fresh Context

## TL;DR

Keep a session-handoff skill that dumps what you discussed, the active files, the decisions made, and the next steps into a file you can paste straight into the other tool. A wall in Claude Code becomes a Codex prompt (or vice versa) instead of another round of arguing.

## Why it matters

Some walls are context problems, but some are **model** problems, the same prompt that loops in one harness gets solved in seconds by a differently-trained model that reads the code from a different starting point.

Without a handoff artifact you either re-explain the whole project by hand or give up and keep grinding in the tool that's already failing.

Because both tools work out of the same folder, the handoff costs nothing but the summary itself: no duplicated project, no lost work.

## How to apply

Write a `session-handoff` skill that outputs four sections, what we've been working on, active files, decisions already made, next steps, then open the other tool in the same directory, paste it, and continue.

Reach for it when the current tool is repeating itself or plainly missing something, not merely when context is full.

This differs from another lesson, which resets context within one tool; here the point is changing the model.

## Related

[[route-work-between-claude-code-and-codex-by-task-type]], [[port-a-project-between-claude-code-and-codex-by-layer]]
