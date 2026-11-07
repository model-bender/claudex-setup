---
id: scope-a-skill-to-answer-only-from-your-knowledge-base
created: 2026-08-07
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/paste-this-into-claude-never-get-stupid-ai-responses-again_Dza_WDoTzRQ_20260807.txt
---

# Create a KB-Only Skill That Refuses to Answer From General Training Knowledge

## TL;DR

Claude blends your ingested docs with its general training data by default, which dilutes company-specific answers with generic best practice. A dedicated skill whose instructions restrict it to a named knowledge-base directory, and explicitly forbid supplementing from outside knowledge, fixes it.

## Why it matters

Demonstrated on an internal "how do we write our newsletter" question. Unscoped, Claude answered from generic content-marketing knowledge. Scoped to the ingested internal docs, the answer became a specific step-by-step process naming actual team members. The problem was never missing information: the docs were already ingested. Nothing stopped Claude from *also* pulling everything else it knew, so the specific answer got averaged down toward the generic one.

## How to apply

Write a skill whose entire job is retrieval-scoping:

- Instruct it to read only from a named directory (for example a `knowledge/` or `wiki/` folder you have already populated with curated docs).
- Instruct it to decline to supplement with general or training knowledge. If the KB does not contain the answer, it must say so rather than filling the gap.
- Reach for it specifically on company-process and domain-specific questions, where a merely plausible generic answer is worse than an honest "not in the knowledge base".

## Related

[[audit-knowledge-base-claims-against-disk-read-only]], [[skill-description-is-routing-logic-not-marketing]]
