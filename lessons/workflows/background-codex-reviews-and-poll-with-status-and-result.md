---
id: background-codex-reviews-and-poll-with-status-and-result
created: 2026-07-17
status: active
supersedes: null
category: workflows
tool: claude-code
about: codex
sources:
  - transcripts/mark-kashef/you-can-run-claude-and-codex-together-here-s-how_Fu5KIG2Jm1g_20260704.txt
  - transcripts/nate-herk-ai-automation/codex-just-10x-d-claude-code-projects_B2Kh_ZoLVTM_20260623.txt
---

# Background Long Codex Reviews With --background and Collect Them With /codex status and /codex result

## TL;DR

Codex plugin reviews take 4-25 minutes on a real codebase. Append `--background` to get a job ID and keep working in Claude Code, then poll with `/codex status` and collect with `/codex result`. Use `--wait` only when you genuinely can't proceed without the answer.

## Why it matters

Run in the foreground, a rescue-scale audit blocks your Claude Code session for the length of a coffee break, long enough that people skip the review entirely. Backgrounding it turns the second opinion into something you fire at a feature the moment you finish it and read later, which keeps you in flow instead of rabbit-holing on one bug.

Which command you background matters too:

- **review**: a standard, unsteerable pass over your current work
- **adversarial**: steerable, so you can aim it at one plan, feature, or trade-off
- **rescue**: the whole-codebase sweep, and unlike the two read-only reviews it will hand off to a Codex subagent that actually changes code

## How to apply

`/codex:adversarial --background <scope>` for a targeted pressure-test, `/codex:rescue --background --model <model> <what to solve>` for a holistic audit. Both return a job ID.

Poll `/codex status` for elapsed time, then `/codex result` for the findings (priority-scored, with recommendations and next steps). Reserve `--wait` for when the next step depends on the verdict.

The review commands anchor on a diff, with nothing staged or committed, Codex creates a review branch to diff against.

> **Note on scope:** another lesson says these commands "can't see logic that hasn't been written yet, so use the consult skill or MCP for a plan." That reads as over-stated: `/codex adversarial` aimed at a plan before any code exists is a heavily-used pattern, and the review-branch fallback is what makes it work. Verify against your own setup.

## Related

[[pair-a-max-claude-plan-with-the-cheap-chatgpt-tier-for-audit-only-codex]], [[route-work-between-claude-code-and-codex-by-task-type]]
