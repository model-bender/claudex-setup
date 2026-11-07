---
id: colleague-with-zero-context-test-for-prompts
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-5-changed-prompting-forever-fix-yours-now_dfi3BsEPxic_20260910.txt
---

# Check a Prompt by Asking Whether a Colleague With Zero Context Could Run It

## TL;DR

Anthropic's check from its best-practices guide: show the prompt to a colleague who knows nothing about the task, and if they would be confused, Claude will be too.

## Why it matters

It catches the specific failure that the Claude 5 prompting advice creates. Once you strip the step lists, what remains has to carry intent (who this is for, what they are judged on, what the output enables) or the model is left guessing on the fifty small decisions you did not specify. The colleague test is the fastest way to notice missing context, because a human reader stumbles on exactly the gaps a model silently fills with its own assumptions.

## How to apply

Before running a prompt you will reuse, read it as if you had no context, or paste it to someone who does not work on it. If they cannot say what good looks like or why the task exists, add the reason and the definition of done, not more steps.

## Related

[[directive-not-aggressive-prompting]], [[write-a-definition-of-done-with-a-length-cap-for-narrow-tasks]]
