---
id: save-the-artboard-and-hand-claude-code-its-name
created: 2026-09-12
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-code-just-dropped-design-master-it-in-8-minutes_Fqlc0N1qyMo_20260910.txt
  - transcripts/tristen-o-brien/claude-design-get-dangerously-good-at-website-animation_c3B5OMF9MNs_20260910.txt
---

# Hit Save, Then Hand Claude Code the Artboard's Name to Start the Build

## TL;DR

Each /design artboard carries a name at the top of the canvas. Save from the right-hand panel, delete the boards you rejected, then tell Claude Code to build that name. That name is the handoff.

## Why it matters

Tristen O'Brien flags the name as the thing to remember before you leave the canvas: 'each one of these designs has its own name up there, you're going to want to make sure that you remember that name'. He also stresses the save step in the right panel before returning to the conversation. This is the concrete mechanic behind the /design to implementation handoff, and it is also where the Claude Code version beats the Claude Design app, which needs an export first. Without the name you end up re-describing the design you already approved, which is the blind prompting loop /design exists to remove.

## How to apply

In the canvas, edit the board you want, click Save in the right-hand panel, and note the name printed above the artboard. Delete the boards you rejected so nothing ambiguous is left. Back in Claude Code, name it directly: 'build <artboard name>'. If you want a second page later, run /design again with fresh references rather than extending the chosen board by prose.

## Related

[[iterate-ui-as-design-artboards-before-implementing]], [[hand-off-claude-design-exports-to-claude-code]]
