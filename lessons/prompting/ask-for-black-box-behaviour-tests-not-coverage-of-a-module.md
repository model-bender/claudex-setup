---
id: ask-for-black-box-behaviour-tests-not-coverage-of-a-module
created: 2026-11-15
status: active
supersedes: null
category: prompting
tool: [claude-code, codex]
source_type: post
sources:
  - https://martinfowler.com/articles/tests-as-data.html
---

# Ask the agent for black-box behaviour tests, not "cover module X with unit tests", which locks in current bugs

## TL;DR

"Cover module X with unit tests" yields mock-heavy tests that prove "A calls B". Ask for black-box tests written in the user's terms (input, expected output or side effect) that carry no implementation detail.

## Why it matters

Mock-heavy tests give false positives on harmless refactors and do not prove correctness. The same article reports that agents do better when told what they want and how to validate it than when told how to do it.

## How to apply

Prompt "write tests from the outside, in customer language, no mocks of our own code, one input and expected output per case". State how to validate the result rather than the steps to get there.

> "when we ask AI to cover something with tests, we'd like the tests to specify the correct behaviour, but most often, the AI will write tests that confirm the current implementation, including any bugs it may contain.", Matteo Vaccari (Thoughtworks), martinfowler.com

## Related

[[keep-acceptance-tests-as-protected-data-files]]
