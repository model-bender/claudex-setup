---
id: default-to-code-review-low-it-spawns-no-agents
created: 2026-08-16
status: active
supersedes: null
category: commands
tool: claude-code
source_type: post
sources:
  - https://x.com/bcherny/status/2087292941111095345
  - https://x.com/bcherny/status/2087384107307422176
---

# Default to `/code-review low` - It Spawns Zero Agents and Costs Under a Cent

## TL;DR

`/code-review low` runs with no subagents at all and costs under $0.01 per run, which Anthropic's own evals put ahead of other models' reviews - so make it the per-PR default and save the higher levels for risky diffs.

## Why it matters

The existing lesson on effort levels covers only that a bare `/code-review` silently reuses your last level. Nobody documents what the levels actually *do*, and the mechanic is the entire cost story: low spawns zero agents, higher levels spawn up to ten. That is a 10x fan-out difference hidden behind a single word, and it is why an unthinking `ultra` on every PR is expensive in a way the command gives no hint about.

## How to apply

Type `/code-review low` explicitly on routine PRs - bare invocation reuses whatever level you typed last, so this also pins it. Reserve medium and above for changes whose blast radius justifies up to ten review agents.

> "Have you tried /code-review low? From our evals, this produces a better result than other models at a fraction of the cost (<$0.01)", Boris Cherny

> "On low effort it uses no agents, at higher effort levels it uses up to 10", Boris Cherny

## Related

[[code-review-reuses-your-last-effort-level]], [[max-effort-is-a-trap-quality-plateaus-at-high]]
