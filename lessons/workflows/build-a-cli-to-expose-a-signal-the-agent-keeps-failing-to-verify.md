---
id: build-a-cli-to-expose-a-signal-the-agent-keeps-failing-to-verify
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/john-kim/how-to-build-an-app-with-claude-code-no-experience-required_20260603.txt
  - transcripts/john-kim/what-is-agentic-ai-engineering-meta-staff-engineer-explains_20260603.txt
---

# When the Agent Repeatedly Cannot Verify Something, Build It a CLI That Exposes the Signal

## TL;DR

A verification the agent keeps failing at is usually a missing surface, not a missing instruction: write a small tool that prints the state it needs, and the loop closes.

## Why it matters

The self-validation loop only works where the agent can observe the result, so a check it cannot perform does not fail loudly, it degrades into an assertion that the code looks right. Repeated failure on the same check is the signal that the gap is in the environment rather than the prompt, and rewriting the prompt again is the reflex that wastes the most time. Exposing the state as a tool also makes the check deterministic and reusable on every later change.

## How to apply

When an agent fails the same verification twice, stop rewording the instruction and ask what observation it is missing. Have it build a small CLI or script that prints exactly that (store contents, rendered layout metrics, a computed value), commit the tool, and reference it in the verification step so subsequent runs use it by default.

## Related

[[visual-self-validation-screenshot-grading]]
