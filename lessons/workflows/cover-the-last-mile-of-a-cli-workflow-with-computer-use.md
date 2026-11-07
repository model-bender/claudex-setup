---
id: cover-the-last-mile-of-a-cli-workflow-with-computer-use
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/mark-kashef/gpt-6-astra-s-computer-use-is-ridiculously-good_tU-fO6cADvQ_20260910.txt
---

# Close the Last 20% of a CLI Workflow With Computer Use Instead of Abandoning the Automation

## TL;DR

When a tool's CLI or API gets you most of the way but a few steps exist only in its GUI, put those steps under computer use and keep the rest scripted. A chain that is 80% automated and stops is worth less than one that finishes.

## Why it matters

Mark Kashef's editing pipeline is the case: the tools involved have their own CLIs, and 'up until now it's been able to take me to 80%, but now with this computer use, you can take processes that have been 80% possible and bring it all the way to 100%.' His run polls a 4K render every 30 minutes, then uploads to the editor, sends a prompt into a chat box that has no programmatic equivalent, clicks through frames, exports, creates the Drive link and messages the team. The value is in the handoff removed at the end, not in any single step, and a pipeline that always needs a human for its final two clicks never gets run unattended.

## How to apply

Map the workflow and mark each step API-reachable or GUI-only. Script the reachable steps, then write the GUI-only ones into the same skill as computer-use instructions, including the waiting behaviour (poll every N minutes, continue when the export appears on screen). Keep the deterministic path in charge and let computer use handle only the gaps, so a GUI change breaks one step rather than the chain.

## Related

[[turn-a-computer-use-workflow-into-a-cli-then-run-it-on-a-cheaper-model]], [[drive-the-web-ui-when-the-api-is-metered-or-mangles-formatting]]
