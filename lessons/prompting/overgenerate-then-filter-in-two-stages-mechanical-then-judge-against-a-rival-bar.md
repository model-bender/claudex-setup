---
id: overgenerate-then-filter-in-two-stages-mechanical-then-judge-against-a-rival-bar
created: 2026-11-06
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/jono-catliff/claude-code-google-ads-steal-your-competitor-s-best-ads-730k-earned_AL3b4kmgsb4_20261106.txt
---

# Generate far more candidates than you need, then filter in two passes: hard constraints first, then a judge against a rival bar

## TL;DR

Ask for a wide batch (Jono generates 150 ads), run a mechanical constraint pass, then have Claude judge survivors against your competitors' best and reject any that would not beat the competitors nine times out of ten.

## Why it matters

Jono Catliff expects most of what Claude generates to be weak, so he casts a wide net and lets the filters remove the rest. The first filter is mechanical, such as Google Ads headline length limits. The second is a judgment filter: Claude reviews the pulled competitor ads and is told not to approve any new ad unless it would beat the competitors nine times out of ten. In his run a large share of the 150 were killed. He notes the filter is imperfect (junk can slip through and good ones get rejected) and that if too much garbage passes, you tell Claude to be more critical next time.

## How to apply

1. Prompt for a large batch (his example: 150 ads) rather than the handful you need.
2. Pass one, mechanical: check each candidate against the platform's hard limits (for example headline character maximums) and drop failures.
3. Pass two, judgment: give Claude the competitor examples to compare against and state the bar explicitly, such as 'do not approve unless it would beat the competitors nine out of ten times'.
4. Show the rejected set as well as the approved set so you can see what the filter cut.
5. If weak items pass, re-run with an instruction to be stricter.

Inference, not from the source: Generalising from ad copy to other generated candidates is the lesson's inference. The transcript demonstrates it only on Google Ads copy (headlines). Listing rejected items for review is also the lesson's addition, though the video does show the rejected ads on screen.
