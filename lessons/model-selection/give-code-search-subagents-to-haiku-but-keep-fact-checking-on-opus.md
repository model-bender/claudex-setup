---
id: give-code-search-subagents-to-haiku-but-keep-fact-checking-on-opus
created: 2026-10-19
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1x1e7ts/i_tested_haiku_55_sonnet_55_and_opus_55_as/
  - https://www.reddit.com/r/ClaudeCode/comments/1x1e7ts/i_tested_haiku_55_sonnet_55_and_opus_55_as/petxmut/
---

# Give Code-Search Subagents to Haiku 5.5, but Keep Fact-Checking on Opus

## TL;DR

In one user's six-task test of Haiku 5.5, Sonnet 5.5 and Opus 5.5 as subagents, Haiku found 44 of the 48 files a feature changed (Opus 45) for $0.44 against Opus's $6.17, but as a fact-checker it flagged 30 correct sentences as errors where Opus flagged none, and rerunning it at xhigh effort still left it flagging 28 (Opus 3).

## Why it matters

The price gap tempts you to put every subagent on Haiku. The failure modes are not symmetric: a search agent that misses a file shows up later on its own, while a checker that wrongly says "this is wrong" gets acted on, and the author notes that following Haiku's verdicts would have meant deleting half of a correct post. Effort fixed one weakness but not the other: at xhigh, Haiku's web research made about as few mistakes as Opus (3 against 3) at half Opus's price but twice the time, while its fact-checking stayed bad.

## How to apply

Pin `model: haiku` on search and locate agents, and keep fact-checking and verification agents on Opus. Research can go to Haiku at xhigh when time matters less than cost. Treat the numbers as one person's six-task test, not a benchmark: rerun a few of your own checker tasks on Haiku before moving any verification agent down a tier.

> "- Correct sentences wrongly marked as errors: Opus 0, Sonnet 6, Haiku 30", u/emarkosov on r/ClaudeCode

> "So Haiku at xhigh is half the price of Opus but twice as slow, and not reliable for fact-checking.", u/emarkosov on r/ClaudeCode

## Related

[[explore-subagents-run-on-your-main-model-route-cheap-search-to-your-own-haiku-agent]], [[dont-run-haiku-5-5-at-low-effort-on-agent-tasks]], [[model-selection-opus-sonnet-haiku-use-cases]], [[upgrade-a-struggling-haiku-log-analysis-subagent-to-sonnet]]
