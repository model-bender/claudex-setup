---
id: write-a-definition-of-done-with-a-length-cap-for-narrow-tasks
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-5-changed-prompting-forever-fix-yours-now_dfi3BsEPxic_20260910.txt
---

# Give Narrow Tasks an Explicit Definition of Done, Including Output Length

## TL;DR

Claude 5 models expand scope by default, so for a narrow task state what done looks like and how long the output should be, in the prompt itself.

## Why it matters

The Opus 5 guide says the model can expand the scope of a task, adding steps that were not requested or applying its own judgment, and tells you to constrain scope explicitly for narrow tasks. In practice you ask a question and get a reworked output plus a dashboard, a chart and a research pass you never asked for. Older guidance pushed the opposite way because earlier models did too little; that advice is now the problem.

## How to apply

Close a narrow prompt with the finish line and the shape of the deliverable, for example: a client email drafted in my mailbox, under 300 words, leading with total leads for the week and the change in share of AI answers, plus the top three reasons for the shift in a table. Name the artifact, the length, the lead, and the structure. Keep this for defined tasks; for larger builds you cannot define up front, have Claude interview you first.

## Related

[[state-change-breadth-explicitly-maximal-or-minimal]], [[validation-loop-in-claude-md-is-critical]], [[done-when-prompt-scaffold-for-codex]], [[ask-claude-to-interview-you-with-askuserquestion-before-a-large-build]]
