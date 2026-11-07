---
id: encode-the-whole-task-lifecycle-in-claude-md-with-every-stage-in-a-subagent
created: 2026-07-25
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Write the Numbered Task Lifecycle Into CLAUDE.md and Put Every Stage in a Subagent

## TL;DR

Rather than prompting build, review, fix, and verify separately each time, write the whole lifecycle as numbered steps in CLAUDE.md with each step delegated to a subagent. The main session then coordinates and never does the work itself, so it never needs a context reset mid-task.

## Why it matters

The creator's framing is that running several parallel sessions is still level one if *you* are the one sequencing the stages; what moves you up a level is the main thread becoming a coordinator. Delegating each stage also isolates its context, which is what makes the review honest, the reviewing agent has not written the code it is reviewing, and the verification agent has no stake in the change passing. And because everything runs in subagents, the orchestrator's own window stays small enough to carry a two-hour task end to end without compaction.

## How to apply

Put a numbered lifecycle in CLAUDE.md, roughly:

1. Implement the request in a subagent.
2. Run `/code-review` in a subagent, scaled by diff size, medium setting under ~100 lines, high above, plus `/security-review`.
3. Pass any medium/high findings to another builder subagent to fix.
4. Repeat step 3 up to three times.
5. Run `/verify` in a subagent, using the Playwright plugin or the Claude in Chrome extension for GUI changes, and produce a screen recording. If verification finds issues, hand them to another builder subagent and repeat step 5, capped at three rounds.

Add explicit handling for verdicts that fall below the auto-fix bar, for a "plausible" finding, notify you with an explanation once the PR is open rather than silently fixing or silently dropping it. Amend the lifecycle every time the agent does something off. Once it stabilises, move it out of CLAUDE.md into a task-lifecycle skill you invoke per session, so it stops costing context on every unrelated task.

## Related

[[supervisor-agent-unblocks-worker-agents-and-escalates-by-exception]]
