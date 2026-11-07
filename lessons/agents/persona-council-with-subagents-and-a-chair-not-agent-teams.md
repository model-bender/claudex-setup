---
id: persona-council-with-subagents-and-a-chair-not-agent-teams
created: 2026-10-19
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-built-the-ultimate-ai-board-of-advisors-free-claude-skill_nRXHWckVxoM_20261013.txt
---

# Run a Persona Council as Subagents Talking to a Chair, Not as an Agent Team

## TL;DR

Nate Herk runs his seven-advisor decision council as subagents with the main Claude Code session as chair, after finding agent teams gave very similar answers at higher cost.

## Why it matters

Herk says he used to run these roasts as agent teams but switched back to subagents because the two did not give meaningfully different answers, subagents were cheaper, and they kept each person's voice more clearly and felt more organized. In his flow each advisor is its own subagent, the chair assigns who argues with whom, and there are three rounds: opening positions, rebuttals, then a vote. He says explicitly that this is subagents, not an agent team.

## How to apply

1. Define one subagent file per advisor and let the main session act as chair.
2. Round one: each subagent writes an opening position. Round two: the chair pairs advisors to rebut each other, including asking some to argue for an option all of them rejected. Round three: votes and a final verdict.
3. Compare cost and answer diversity against an agent-team run before committing to the pricier option.
This is one creator's experience on one council, not a measured benchmark.
Checked: no flag or env var is named. Agent teams and subagents both exist in Claude Code 2.1.303 as separate features.

## Related

[[agent-team-debate-panel-for-decisions]], [[agent-teams-for-cross-domain-collaboration]], [[run-a-manager-led-round-table-where-agents-may-pass]], [[quick-persona-subagents-for-first-impression-not-debate]]
