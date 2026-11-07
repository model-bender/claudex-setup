---
id: give-a-reusable-sub-skill-a-mode-argument
created: 2026-09-12
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/this-fixes-claude-s-biggest-problem-karpathy-s-method_4hIvG849w4Y_20260910.txt
---

# Give a Shared Sub-Skill a Mode Argument Instead of Cloning It Per Caller

## TL;DR

When a skill will be reused by several orchestrators, pass the purpose in as an argument rather than hard-coding it. One analysis skill with modes beats three near-identical skills.

## Why it matters

Austin Marchese designed his session-analysis skill this way on purpose: the analysis is the same, only the lens changes, so '/session-analysis dream' formats its findings for memory consolidation while '/session-analysis time-analysis' would look at the same history for where his time goes. His reasoning is the software one: 'you design systems based on functions or self-contained logic that you can reuse across your entire system.' Cloning instead means the expensive part, the analysis logic, drifts between copies and every fix becomes three fixes.

## How to apply

Identify the part of the skill that is genuinely shared (the gathering and analysis) and the part that varies (the output shape and what to select for). Take the varying part as an argument with argument-hint documenting the accepted modes, and have the orchestrating skill pass it explicitly. Add a mode only when a second caller actually needs it, not speculatively.

## Related

[[skill-systems-over-monolithic-skills]], [[give-a-critique-skill-a-blunt-mode-and-a-professional-mode]]
