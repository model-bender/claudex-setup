---
id: ask-what-claude-cannot-reach-when-you-keep-doing-a-step-by-hand
created: 2026-10-25
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/the-only-4-things-you-need-to-prompt-like-an-anthropic-engineer__NzakzRXzLI_20261022.txt
---

# When You Keep Doing a Step by Hand, Ask Yourself What Access Claude Is Missing

## TL;DR

When you keep doing a task by hand that Claude could do, treat it as a sign Claude lacks the right access: ask whether it has the same information you do, and if not, connect what is missing.

## Why it matters

Austin Marchese calls this a question he would almost guarantee viewers have never asked: does Claude have the same access to information that you do? On his own product he kept doing one manual task, realised there was no reason he should be doing it, gave Claude the access and says everything changed.

## How to apply

1. Each time you catch yourself doing a step for Claude (his example: approving the same thing again and again), ask yourself: what access would let it do this itself? 2. Add the missing connector (the creator mentions the plus button for connections in Claude). 3. Optionally prompt Claude to review what you have repeatedly approved and what past outputs required a manual next step, and propose connections that remove them. 4. For systems with no ready connector he mentions a build-connector skill in the Claude small business plugin (not verified here). Checked: Plugin and skill name 'build connector' in the Claude small business plugin not verified; the lesson keeps it as the creator's claim only.

## Related

[[verify-skill-ask-what-it-needs]], [[give-the-agent-the-emulator-so-it-self-tests]]
