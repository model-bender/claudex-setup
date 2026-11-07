---
id: codex-has-no-custom-slash-commands-port-them-as-skills
created: 2026-07-17
status: active
supersedes: null
category: commands
tool: codex
sources:
  - transcripts/john-kim/complete-beginner-s-guide-to-openai-s-codex-app_20260424.txt
  - transcripts/mark-kashef/how-to-instantly-run-any-skill-in-claude-codex_tjjX43FoAUg_20260704.txt
  - transcripts/nate-herk-ai-automation/master-97-of-codex-in-1-hour-full-course_3TdD8Qv5Tk8_20260626.txt
---

# You Can't Author a Codex Slash Command: Port Claude Code Commands as Skills

## TL;DR

Codex's slash commands are built-in primitives only (model, plan mode, reasoning, review, personality, side). The user extension point is skills, invoked with `$` in the CLI and surfaced alongside the primitives under `/` in the app.

## Why it matters

Anyone porting a Claude Code setup goes looking for the commands directory and finds nothing, custom slash commands are a core Claude Code primitive with no Codex counterpart. The sigil difference between the CLI and the app makes it look like the skill didn't install when it did.

Knowing the mapping up front turns "this doesn't exist in Codex" into a one-line conversion.

## How to apply

Convert each custom slash command into a skill: the markdown body ports as-is, only the invocation changes. Use `$skill-name` in the Codex CLI, or `/skill-name` in the Codex app.

Skills install globally (`~/.codex`, usable from any project) or project-local; ask Codex to move one between the two rather than doing it by hand.

The markdown body ports, but **adapt it** rather than copying verbatim: drop `allowed-tools`/`argument-hint`, add a short description, and state the `$name` invocation contract in the body. There is **no sidecar file** to write, see [[codex-skills-need-sidecar-and-cap-descriptions-put-triggers-first]] (verified 2026-07-17 against a live 71-skill install).

## Related

[[port-a-project-between-claude-code-and-codex-by-layer]], [[codex-skills-need-sidecar-and-cap-descriptions-put-triggers-first]]
