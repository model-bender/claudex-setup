---
id: tell-astra-to-make-reasonable-assumptions-claude-needs-the-opposite
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-5-changed-prompting-forever-fix-yours-now_dfi3BsEPxic_20260910.txt
  - transcripts/mark-kashef/i-tested-every-gpt-6-astra-effort-level-here-s-what-i-d-use_OQipTxv9Qv0_20260910.txt
---

# Tell Astra to Take a Bias Toward Action, Claude 5 Needs the Opposite Constraint

## TL;DR

GPT-6 Astra stops to ask rather than assuming, so state that you want a bias toward action and reasonable assumptions. Claude 5 models already act, so they need the boundary instead.

## Why it matters

OpenAI's own documentation says Astra is designed to be a more effective collaborator and thus more likely to ask questions of the user, and that this can cause it to stop when the user may expect it to make reasonable assumptions. Users report it stopping early and asking for permission every few minutes. The mirror image is Anthropic's Claude 5 guidance, which warns that the model takes unrequested actions and tells you to define explicit constraints. The same prompt therefore needs opposite clauses depending on which model runs it.

## How to apply

In the prompt file for whichever OpenAI-model agent you run (Codex reads AGENTS.md), say you want a bias toward action, that reasonable assumptions should be made and recorded rather than asked about, and name the small set of decisions worth stopping for. In CLAUDE.md keep the reverse: when I am asking a question or thinking out loud, report your assessment and stop. Do not copy prompts between the two without flipping this clause.

## Related

[[shape-the-prompt-to-the-harness-goal-for-claude-code-steps-for-codex]], [[assessment-only-mode-for-diagnostic-tasks]], [[move-repeated-prompt-constraints-into-agents-md]]
