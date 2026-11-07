---
id: outsource-writing-only-when-boring-predictable-and-accurate
created: 2026-08-07
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/2026/jul/5/sqlite-utils-fable/
---

# Use "Boring, Predictable, Accurate" as the Test for What an Agent Can Own End to End

## TL;DR

Before delegating a writing task fully (not draft-then-review), ask whether the genre rewards being boring, predictable, and accurate. Release notes, changelogs, and migration guides qualify. Anything carrying voice or judgment does not.

## Why it matters

The useful part is that it is a property of the *genre*, not of the model's ability. Willison let an agent draft the sqlite-utils 4.0 release notes unsupervised precisely because that form's requirements (dry, formulaic, factual) are what agents reliably hit, while still hand-reviewing everything else in the release. That gives a reusable line between full delegation and draft-then-review, rather than deciding case by case.

## How to apply

Score the target genre on the three properties before choosing a delegation mode. All three present means the agent can own it end to end. Any one missing means keep it as a draft you review, since the value is in exactly the part the agent will average away.

> "Release notes are a great example of writing that I'm OK to outsource to agents because they need to be boring, predictable and accurate.", Simon Willison

## Related

[[tell-claude-to-re-ground-its-final-message-after-unattended-runs]], [[doc-sync-pass-reconcile-docs-against-diffs]]
