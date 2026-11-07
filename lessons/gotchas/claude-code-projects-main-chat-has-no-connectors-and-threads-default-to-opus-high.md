---
id: claude-code-projects-main-chat-has-no-connectors-and-threads-default-to-opus-high
created: 2026-10-19
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-changed-completely-every-new-concept-explained_YAuWBqZ_gjs_20261018.txt
---

# Before Using a Claude Code Project, Check That Only Threads Get Connectors and That Threads Default to Opus on High Effort

## TL;DR

In the Projects beta the main conversation cannot use your connectors, only its threads can, and threads default to Opus on high effort, which burns limits fast. Adjust the project settings first.

## Why it matters

Simon Scrapes lists two things to know before starting a project: the main chat acts as an orchestrator that delegates to threads (which are full cloud Claude Code sessions that keep going after you close the laptop), and the thread default model and effort are expensive. Chats elsewhere still work the old way, and context is passed between them by share links.

## How to apply

1. Treat the project conversation as a team lead: brief it, and expect tool and connector work to happen inside threads. 2. Open the project settings and lower the default model or effort for threads if limits matter. 3. Put broadly applicable context (for example brand voice) in the project instructions. Checked: cloud beta feature, so there is no flag to count in the claude 2.1.303 binary; both claims are the speaker's and the existing project lesson cites docs for the rest.

## Related

[[let-claude-code-projects-split-thoughts-into-threads]]
