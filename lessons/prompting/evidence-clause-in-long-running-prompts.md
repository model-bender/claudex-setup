---
id: evidence-clause-in-long-running-prompts
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-anthropic-actually-prompts-fable-5-1_FBVNS1l5Vb8_20260910.txt
---

# Put an Evidence Clause in Long-Running Prompts: Audit Each Claim Against a Tool Result

## TL;DR

Anthropic's Fable prompting docs give the wording: before reporting progress, audit each claim against a tool result from the session, report only work you can point to evidence for, and say explicitly when something is not yet verified.

## Why it matters

A long autonomous run reports success far more often than it achieves it, and you find out later from a claim you believed. Making self-verification explicit in the prompt ('verify your work with subagents against the specification') means the thing handed to you is a version five that has already been reviewed and corrected several times, rather than a first draft you have to audit yourself.

## How to apply

Add two clauses to any long-running prompt: 'verify your work with subagents against the specification', and 'before reporting progress, audit each claim against a tool result from this session; only report work you can point to evidence for, and say so explicitly when something is not verified'. For outputs without an objective check, write down what good looks like and how to test it, so the verifying agent has a rubric rather than an opinion.

## Related

[[audit-agent-transcripts-dont-trust-the-success-claim]], [[design-agent-output-for-verifiability-before-building-evals]], [[verify-touched-symbols-after-agent-says-done]], [[shift-verification-to-the-cheapest-rung]]
