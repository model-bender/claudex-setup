---
id: ask-claude-to-interview-you-with-askuserquestion-before-a-large-build
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-5-changed-prompting-forever-fix-yours-now_dfi3BsEPxic_20260910.txt
  - transcripts/nate-herk-ai-automation/gpt-6-astra-finally-solves-ai-video-editing-full-guide_o3IEkKXXXvo_20260910.txt
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# For a Large Build, Start Minimal and Ask Claude to Interview You With AskUserQuestion

## TL;DR

When you cannot state what done looks like, do not write a better prompt: give a minimal one and ask Claude to interview you with the AskUserQuestion tool, and name the number of questions you want, because left to its own judgment it stops after about four.

## Why it matters

Definition-of-done guidance breaks on work whose shape you do not know yet, and Anthropic's own Claude Code best-practices answer is to have Claude interview you for larger features rather than guess. The interview surfaces the fifty small decisions a prompt silently omits (edge cases, trade-offs, who it is for), and because it runs through AskUserQuestion you get selectable options plus a free-text box instead of a wall of prose questions.

Naming a number is the part people leave out. Left to its own judgment Claude asks clarifying questions but caps out around four, which is not enough coverage for a large feature, so the interview ends before it reaches the decisions you most needed surfaced.

## How to apply

Open with the minimal statement of what you want to build, then: 'Interview me in detail using the AskUserQuestion tool. Ask me 20 clarifying questions about the goal, who it is for, what done looks like, edge cases and trade-offs, and dig into the parts I have not considered.' Answer the rounds, then have it write the brief and start the build from that.

The tool renders at most four questions per round, so a 20-question interview arrives as several rounds. If you would rather take the whole list in one pass, ask for the questions without the tool (see another lesson).

## Related

[[write-a-definition-of-done-with-a-length-cap-for-narrow-tasks]], [[write-askuserquestion-into-skill-question-steps]], [[brand-voice-quiz-for-fast-voice-profile]]
