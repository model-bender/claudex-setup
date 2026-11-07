---
id: route-sonnet-5-5-on-clear-spec-and-checkable-done-opus-5-5-on-vague-or-subjective
created: 2026-10-02
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-tested-sonnet-5-5-vs-opus-5-5-what-you-need-to-know_7eo-11K2e3c_20261002.txt
---

# Send Work to Sonnet 5.5 When You Have a Spec and a Check, to Opus 5.5 When the Goal Is Vague

## TL;DR

A creator tested a rule read in a Claude guide on seven tasks: if you can state the finished result and check it, try Sonnet 5.5 first; if the goal is vague, subjective or open-ended, use Opus 5.5.

## Why it matters

The creator ran seven tasks on both models at high effort. Where the prompt was vague (a research-backed 90-day plan, a request to scrape X into a dashboard, a motion reel), Opus's output was preferred, though the X dashboard round was scored to Sonnet on cost; the final tally was four rounds to Sonnet and three to Opus. Where a skill defined what good looks like (a YouTube resource guide), the outputs were very similar and Sonnet was twice as fast and $1.40 cheaper. With another skill (an HTML explainer), Opus's output was better but Sonnet cost half as much, and the creator gave Sonnet the round expecting one more prompt to close the gap. The creator sums it up as: with an objective definition of done, try Sonnet 5.5 first, and plans to run each of their skills on both models and note which suits each one. These are one creator's subjective results on seven tasks.

## How to apply

Before picking a model, ask whether you can state the finished result and check it. If yes, start on Sonnet 5.5 (`/model sonnet`). If you want a thought partner to decide what 'done' means, or the brief is open-ended, use Opus 5.5. For a skill you reuse, run it on both once and record the winner in the skill's description or your routing notes.

Verified: Model ids claude-sonnet-5-5 and claude-opus-5-5 both appear in the Claude Code 2.1.287 binary. The creator attributes the rule to an Anthropic guide; Anthropic's choosing-a-model page (read 2026-10-02) does not state it, and says most workloads start with Opus 5.5, so the rule is presented as the creator's, not Anthropic's.

## Related

[[sonnet-for-fixes-review-and-changelogs]], [[model-selection-opus-sonnet-haiku-use-cases]], [[walk-a-skill-down-the-model-and-effort-ladder-to-find-the-cost-floor]], [[sharpen-the-spec-before-reaching-for-more-effort]]
