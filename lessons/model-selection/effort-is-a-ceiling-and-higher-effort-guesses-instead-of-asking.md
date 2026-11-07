---
id: effort-is-a-ceiling-and-higher-effort-guesses-instead-of-asking
created: 2026-10-25
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/austin-marchese/use-claude-models-effort-level-better-than-97-of-people_BZluE67z1MA_20261024.txt
---

# Treat the Effort Setting as a Ceiling, Not a Floor: Max Makes Claude Guess Instead of Ask

## TL;DR

Effort is the most thinking and activity Claude is allowed to spend, not a required amount, and the creator says higher effort makes it answer questions you never addressed rather than ask you.

## Why it matters

Austin Marchese says leaving effort on max is not free insurance: a higher cap biases the model toward taking longer than needed, and it fills in unanswered questions on your behalf instead of asking. He also says low effort does not make the model less knowledgeable, it commits to an answer faster and would rather ask for context than work it out alone. Raising effort also does not turn a smaller model into a bigger one (Sonnet at max is not Opus).

## How to apply

Leave effort on medium for everyday work (his description of the default). Move to high for work where mistakes hide (bugs, edge cases). Reserve max for a genuinely hard task that runs alone end to end, and expect diminishing returns and overthinking there. If you want Claude to ask about unspecified decisions rather than guess, do not rely on a high effort setting to do it; this lesson's own suggestion (not from the video) is to state in the prompt which decisions it must ask about. Set the level with `claude --effort <level>`. Checked: claude --help on 2.1.310 lists --effort <level> (low, medium, high, xhigh, max). The ceiling and guess-instead-of-ask behaviour are the creator's account, not verified against docs or a measurement.

## Related

[[max-effort-is-a-trap-quality-plateaus-at-high]], [[sharpen-the-spec-before-reaching-for-more-effort]]
