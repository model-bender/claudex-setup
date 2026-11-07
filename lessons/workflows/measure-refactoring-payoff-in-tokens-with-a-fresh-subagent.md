---
id: measure-refactoring-payoff-in-tokens-with-a-fresh-subagent
created: 2026-08-07
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html
---

# Justify Refactoring by Measuring the Token Cost of the Same Prompt Before and After

## TL;DR

Because agents do not learn between runs, refactoring's payoff is directly measurable: run one identical change prompt in a fresh subagent before and after each refactoring stage and compare token counts. On a 17,155-line Rust data-access layer this showed an 83% drop.

## Why it matters

Refactoring is usually argued for on readability, which is subjective and loses to delivery pressure. This reframes it as a recurring cost on every future agent-run change, with a reproducible experiment behind the number: decompose a large file so the agent can find and read only the relevant section instead of the whole thing, and every subsequent change touching that file gets cheaper. It is a different lever from adding retrieval, because it changes the shape of the code rather than the search over it.

## How to apply

Before refactoring a large agent-touched file, write one representative single-prompt change and run it in a fresh subagent instructed to report its own token consumption, giving you a baseline. After each refactoring stage, re-run the identical prompt in a *fresh* subagent and compare. The freshness matters: a reused session carries the file in context and hides the effect.

> "Input tokens for the same task reduced from 159,564 to 27,360. A saving of 132,204 tokens, or 83%.", Giles Edwards-Alexander, Thoughtworks "Exploring Gen AI"

## Related

[[give-agents-index-backed-code-search-in-large-codebases]]
