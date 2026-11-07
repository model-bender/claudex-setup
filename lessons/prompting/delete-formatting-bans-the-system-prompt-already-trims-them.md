---
id: delete-formatting-bans-the-system-prompt-already-trims-them
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-5-changed-prompting-forever-fix-yours-now_dfi3BsEPxic_20260910.txt
---

# Delete 'No Bullets, No Tables' Style Bans: Fable 5.1's System Prompt Already Trims Them

## TL;DR

Anthropic put instructions to use fewer bullets, less bold and fewer tables into Fable 5.1's own system prompt, so your negative formatting rules are surplus tokens that can fight the system prompt instead of helping.

## Why it matters

Negative constraints were how you got earlier models to stop bulleting everything. On Claude 5 models the behaviour is already trained and instructed, so repeating it spends tokens on every turn and adds a constraint the model has to reconcile with its own. The general rule Simon draws from the Anthropic guidance is to state the behaviour you want plus the reason, not the behaviour you do not want.

## How to apply

Remove 'never use bullets', 'do not use tables', 'avoid bold' and similar from CLAUDE.md, skills and project instructions, and check whether the output actually regresses before adding anything back. If you need a specific shape, state it positively once in the place it applies ('answer in plain paragraphs because this goes straight into an email').

## Related

[[directive-not-aggressive-prompting]], [[keep-the-context-half-of-a-skill-delete-the-procedure-half]], [[add-remove-all-mannered-prose-to-your-global-instructions]]
