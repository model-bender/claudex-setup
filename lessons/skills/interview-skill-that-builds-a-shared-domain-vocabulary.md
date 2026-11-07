---
id: interview-skill-that-builds-a-shared-domain-vocabulary
created: 2026-10-19
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/matt-pocock-the-most-valuable-skill-to-learn-in-the-age-of-ai_Z8lf5oWKfj0_20261017.txt
---

# Have Your Interview Skill Build a Shared Domain Vocabulary So Code, Database, UI and Client Use the Same Terms

## TL;DR

Matt Pocock uses a variant of his Grill Me skill, Grill with Docs, that builds a ubiquitous language (a domain-driven design idea) while it interviews you. The same word then means the same thing in the code, the database, the UI and your conversations with the client.

## Why it matters

Pocock says the communication gap between you and the agent is permanent, and precise shared terms are how you close it. His example is 'order': it should mean one thing in the code, the database, the UI and in talks with the client. He calls the technique extraordinary for building with agents even though most coders have not heard of DDD. Clear language from the person doing the thinking ends up in the product.

## How to apply

1. Run your interview or grill-me skill with an added instruction to define each domain term as it appears (what an 'order' is, what states it has) and to record the agreed definitions in a glossary document in the repo.
2. Tell the agent to use only those terms in code names, schema, UI copy and replies, and to flag any place where two words mean the same thing or one word means two.
3. Re-read the glossary with the client or user, since the terms should match how they talk.
The glossary file is the lesson's inference from the skill name 'Grill with Docs'; the transcript says only that it helps you build the domain language as you go.
Checked: no CLI flag, setting or command is named. The skill is described only, and its contents were not inspected.

## Related

[[self-interview-skill-to-extract-tacit-knowledge]], [[fix-one-noun-per-entity-in-a-skill-before-writing-it]]
