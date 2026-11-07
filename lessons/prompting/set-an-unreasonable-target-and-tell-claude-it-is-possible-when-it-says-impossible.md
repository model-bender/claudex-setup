---
id: set-an-unreasonable-target-and-tell-claude-it-is-possible-when-it-says-impossible
created: 2026-10-19
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/ray-amjad/your-prompts-are-too-small-for-claude-code_RbfQayMNtJc_20261018.txt
---

# Ask for a Target Several Times Beyond Reasonable and Push Back When Claude Says It Is Impossible

## TL;DR

If you want a 5 second load, ask for 200 ms, and answer an 'impossible' with 'it is possible, keep going'.

## Why it matters

Ray Amjad, again relaying Felix's article, says picking an unreasonable goal and insisting it is reasonable is a rising technique. He cites the Bun creator's prompt on the Riemann hypothesis, half of which was encouragement. The transcript offers no measured benefit.

## How to apply

State the extreme target and a verifiable measurement for it. When Claude calls it impossible, reply that it is possible and ask it to continue. Pair it with real expert tools (profilers, traces) so progress is measurable. This is anecdotal; treat it as something to try on a task with a numeric check. Checked: prompt technique, nothing to verify against the binary.

