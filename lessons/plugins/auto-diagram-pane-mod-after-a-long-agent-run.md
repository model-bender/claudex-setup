---
id: auto-diagram-pane-mod-after-a-long-agent-run
created: 2026-10-19
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/ray-amjad/most-claude-code-mods-are-toys-these-are-for-agentic-engineers_Od9706XIXcc_20261013.txt
---

# Get an Auto-Generated Diagram of What a Long Run Did With a Diagram-Pane Mod

## TL;DR

After a big task, a Haiku check decides whether a lot of work happened, and if so a fork designs a diagram of the session's steps and decisions in a side pane. Inline Mermaid diagrams Claude writes get pinned there too.

## Why it matters

Ray Amjad notes that after an hour of agent work a text summary is hard to read. His mod produced a diagram with a key (a file is a square rectangle, a new component a rounded one, a step that happened a double rectangle) so he could see what was built, what was verified and what was published.

## How to apply

1. Ask Claude for a diagram-pane mod using the classifier-then-fork pattern. 2. Optionally have it capture any inline Mermaid diagram into a 'pinned diagrams' list in the pane. 3. Combine with other panes; with two pane mods you switch between them. Checked: claude 2.1.303 binary lists a 'ui.panes' plugin call and the model.classify and model.fork calls; the demo is the speaker's, not tested.

## Related

[[gate-a-fork-behind-a-small-model-classifier-after-every-turn]]
