---
id: one-session-per-plan-phase-chained-as-stacked-prs
created: 2026-08-16
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-just-made-subagents-feel-obsolete_oqp6D-ugtX4_20260810.txt
---

# Run Each Phase of a Plan in Its Own Session and Chain Them as GitHub Stacked PRs

## TL;DR

Tag a phased plan and ask for one new pane or session per phase, each opening a stacked PR on top of the previous phase's branch. Paste the stacked-PR documentation link into the prompt, because the feature postdates the model's training data.

## Why it matters

Phased plans normally collapse into one long session where later phases inherit earlier phases' context and the review surface is a single enormous diff.

One session per phase keeps each phase's context clean and each diff reviewable, and stacked PRs put the dependency order into GitHub instead of into your head. Because each phase is a real session rather than a subagent, you can reopen any phase later and follow up on it.

## How to apply

Give the agent the plan file plus the GitHub stacked-PRs docs URL, then:

> "use GitHub stacked PRs, and for each phase of this plan implement it in a brand new pane; once that phase is done, start a new pane and open a pull request in between as a stacked PR."

Expect to supply the docs link every time, or wrap the whole convention (phase splitting, branch naming, stacking) into its own skill so you stop re-explaining it.

## Related

[[wrap-your-terminal-cli-in-a-skill-so-claude-code-spawns-peer-sessions]], [[name-your-sessions-so-they-can-message-each-other]]
