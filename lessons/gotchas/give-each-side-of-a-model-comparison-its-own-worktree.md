---
id: give-each-side-of-a-model-comparison-its-own-worktree
created: 2026-10-02
status: active
supersedes: null
category: gotchas
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/i-tested-opus-5-5-vs-gpt-6-astra-on-12-real-use-cases_GmLcJVzkxPA_20261002.txt
  - transcripts/nate-herk-ai-automation/i-tested-opus-5-5-vs-gpt-6-sol-on-10-real-use-cases_eF3yeJuifoQ_20260923.txt
---

# Give Each Tool Its Own Worktree When Running the Same Prompt on Claude Code and Codex

## TL;DR

If you send one prompt to Claude Code and Codex in the same project folder, they can end up editing each other's files and the comparison is spoiled. Put each run in its own git worktree.

## Why it matters

In a creator's earlier head-to-head, two of the experiments were compromised because both agents worked on the same deliverables. In a later video the creator says these tests normally run in separate worktrees so the agents literally cannot touch each other. In the original video the creator had both models inspect the logs: the first Codex request failed, and when it was resumed about 16 minutes later it picked up the files Claude had already started and edited them while Claude was still working. Cost and time figures for those runs were then unreliable, so the creator corrected them afterwards.

## How to apply

Before a side-by-side run, create one worktree per tool, for example `claude --worktree <name>` for the Claude Code side and `git worktree add ../<name>` for the Codex side, and open each tool in its own folder. Also say in the prompt not to edit files that belong to anyone else. As the lesson's own inference: if a run fails and you resume it later, check what the other agent has already written before resuming.

Verified: Claude Code 2.1.287: `claude --help` lists `-w, --worktree [name]` (Create a new git worktree for this session). The Codex side uses plain `git worktree`. The sibling-video incident details are the creator's own account, not independently checked.

## Related

[[worktrees-for-parallel-independent-tasks]], [[agent-teams-agent-should-not-touch-same-files]]
