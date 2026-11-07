---
id: use-design-screens-as-the-exit-criteria-for-a-long-goal
created: 2026-10-19
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/john-kim/ai-coding-is-hard-until-you-start-setting-goals_P0I8jl7WUf0_20261015.txt
---

# Give a Multi-Hour Goal a Set of Design Screens as Its Exit Criteria

## TL;DR

For a UI build that runs overnight, generate the full set of screens first and let the agent cross-reference its running app against them, instead of a vague 'build the app' finish line.

## Why it matters

John Kim spent about an hour reviewing a plan and generated all the screens in a Pencil design file, then used those screens as the exit criteria. The goal was plain English ('build out the plan, make sure you have validations, push to GitHub at good checkpoints, archive old files instead of destructive deletes'), and it had run about 22 hours when he showed it, driving the iOS simulator to QA itself.

## How to apply

1. Plan with visualisations and review them (he took roughly an hour). 2. Create the design screens. 3. Write the goal to cross-reference them, ask for validations, pushes at checkpoints, and archiving rather than deleting. 4. Pre-provision tooling (deploy CLI logged in, skills, simulator access) so it does not stall. Checked: no flag or setting named; the 22 hours and screens are the speaker's run.

## Related

[[goal-verifiable-finish-lines-with-safety-caps]], [[give-the-agent-the-emulator-so-it-self-tests]]
