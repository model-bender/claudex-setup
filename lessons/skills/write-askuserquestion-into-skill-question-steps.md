---
id: write-askuserquestion-into-skill-question-steps
created: 2026-07-25
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/17-tricks-to-build-10x-faster-with-claude_ZzHB2mPHb2g_20260724.txt
---

# Make Your Skills Ask Through AskUserQuestion Instead of One Prose Block

## TL;DR

A skill that gathers requirements will, by default, emit all its clarifying questions as a single wall of text you have to answer in one message. Explicitly instruct the skill to use AskUserQuestion and you get the structured, one-at-a-time picker instead.

## Why it matters

The transcript shows a side-by-side of the same skill run two ways: without the instruction it dumps a paragraph of questions that is "hard for me to answer each one", while the AskUserQuestion version steps through them individually in a formatted UI with real options to click. The tool is available either way, the skill just won't reach for it unless `SKILL.md` says so. That means every question-gathering skill you already own is silently degrading its own intake step, and the degradation is invisible because the prose version still "works".

## How to apply

In each question-asking skill, replace the vague "ask the user about X, Y, Z" step with an explicit instruction to use the AskUserQuestion tool, and enumerate both the questions and their candidate options so it can render real choices rather than free text. To find candidates across an existing library, prompt Claude to audit your skills and list which ones ask the user anything, plus the questions each should be asking. Note AskUserQuestion caps at 4 questions per round, so split a long intake into rounds rather than truncating it.

## Related

[[skill-description-is-routing-logic-not-marketing]]
