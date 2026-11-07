---
id: cap-force-ship-improvement-loops-and-pick-a-stop-round
created: 2026-11-06
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-told-claude-to_DByAR5Su1Yw_20261103.txt
---

# Cap an open-ended 'make it better' loop and review its milestones, because forced changes turn into bloat

## TL;DR

A repeated 'make it better' prompt only keeps going if you force a shipped change every round, but late rounds add clutter and break earlier features. Run a bounded number of rounds, review the milestone rounds, and keep the version from where gains stopped.

## Why it matters

Nate Herk fed a deliberately bad coffee shop site the same prompt 100 times in fresh clean-room sessions (no skills, CLAUDE.md, plugins or memory), on Sonnet 5.5 and Opus 5.5 at medium effort. Without a forced-change rule the model had stopped around round 20 to 25 saying nothing more could be done. With it, the big jumps were all early (first image, first form, first video), lines of code rose steadily, and later rounds produced no new milestones. At round 100 the Opus site (about 21,000 lines) had broken sections, a feature that did not work, and a language toggle that did not translate; the Sonnet site (under 3,000 lines) had dropped a feature it had at round 65 and swapped a font for no reason. He judged the model sets the ceiling and the prompt sets the direction, and that 'innovate' without a vision becomes adding.

## How to apply

1. If you run a repeated improvement prompt, state the stop-resistance explicitly, for example: look at the current site first, make one bold change per round, and you must ship a change every time.
2. Cap the round count up front (tens of rounds, not hundreds) instead of letting it run open ended.
3. Commit or snapshot after each round so you can compare rounds.
4. Review the rounds where something new appeared (new feature, new asset type), not only the last one, and keep the earlier version where gains flattened.
5. Supply the taste yourself (a concrete reference or direction) rather than relying on 'innovate', since the models did not search the web for inspiration on their own.

Inference, not from the source: The advice to cap rounds, commit per round and keep an earlier version is the lesson's practical reading of the experiment. The transcript shows the over-engineering and the early stop without the forced-change rule, and says the user must give guidance, but does not prescribe a specific round cap or per-round commits.

## Related

[[brainstorm-the-goal-statement-with-the-agent-before-firing-the-run]], [[state-change-breadth-explicitly-maximal-or-minimal]]
