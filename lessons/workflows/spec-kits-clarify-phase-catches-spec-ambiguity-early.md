---
id: spec-kits-clarify-phase-catches-spec-ambiguity-early
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/sean-kochel/why-your-agentic-workflows-don-t-work_ILKrUq_8aC4_20260820.txt
---

# Run a Dedicated Clarify Pass on a Spec Before Planning

## TL;DR

GitHub Spec Kit inserts a distinct 'clarify' step between writing the spec and planning the build, specifically to surface anything ambiguous that would otherwise let the model make an unstated decision on its own.

## Why it matters

Sean Kochel frames this as a named failure mode ('there's not something that you didn't actually think about that the model could go off and make any random decision... that is a huge failure mode'), addressed by giving ambiguity-hunting its own explicit pipeline stage rather than folding it into planning.

## How to apply

After writing a feature spec and before planning the build, run a clarify-style pass (Spec Kit's `clarify` command, or your own prompt asking 'what is ambiguous or unstated here that you'd otherwise have to guess?') and resolve every flagged item before proceeding to plan.

## Related

[[gate-every-feature-on-a-constitution-file]], [[openspec-living-spec-contract-breaks-surface-on-archive]]
