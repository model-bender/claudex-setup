---
id: simplify-a-skill-after-a-model-upgrade-instead-of-adding-detail
created: 2026-09-13
status: active
supersedes: null
category: skills
source_type: post
tool: claude-code
sources:
  - https://www.dbreunig.com/2026/09/07/what-we-can-learn-from-claude-s-fable-5-1-system-prompt.html
---

# When a Model Upgrade Breaks a Skill, Delete Instructions Rather Than Add Them

## TL;DR

Skills that regressed on Fable and Opus 5 usually improve by stripping detail out, not by patching in more explicit rules.

## Why it matters

The instinct when output gets worse is to constrain harder, and that is backwards for a stronger model: the examples and step lists that made a weaker model reliable are what now narrow its exploration space. Anthropic's own advice is to dramatically simplify skills or remove them entirely.

## How to apply

After a model version bump, if a previously working skill starts behaving oddly, first delete redundant and over-specified instructions (explicit numeric rules, repeated constraints, prescribed step orders) and re-test before adding anything.

> "One question I keep having, and am often asked, is why existing skills kind of broke with Fable and Opus 5. Anthropic talks about the problem plenty, advising people to dramatically simplify their skills, or remove them entirely.", Drew Breunig
