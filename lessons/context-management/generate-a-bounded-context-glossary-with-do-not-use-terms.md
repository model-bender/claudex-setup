---
id: generate-a-bounded-context-glossary-with-do-not-use-terms
created: 2026-11-15
status: active
supersedes: null
category: context-management
tool: [claude-code, codex]
source_type: post
sources:
  - https://martinfowler.com/bliki/GeneratedGlossary.html
---

# Have an LLM generate a bounded-context glossary, with "do not use" terms, and load only terms plus links up front

## TL;DR

Mine your docs, chat and code for jargon the model has not seen, and generate a glossary for domain-expert review. Keep it in version control with a periodic refresh. Split glossaries per bounded context, list deprecated terms with replacements, and put only terms and links in initial context.

## Why it matters

A model that does not know a repo or organisation's specialised vocabulary performs worse there. A single standard glossary tends to hide that the same word means different things in different contexts.

## How to apply

Run a one-off agent pass over your sources to produce GLOSSARY.md, with context-specific definitions and a "use X instead of Y" section. In CLAUDE.md, reference it so that large glossaries load as a term-and-link index.

> "It's often useful for glossaries to include terms that should not be used, in which case it includes advice on what other term to use instead.", Martin Fowler

## Related

[[interview-skill-that-builds-a-shared-domain-vocabulary]]
