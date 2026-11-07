---
id: remotion-plugin-in-claude-code-as-the-code-based-video-fallback
created: 2026-10-19
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-just-dropped-motion-get-ahead-of-95-in-11-minutes_yf2OwchM9nw_20261015.txt
---

# Use the Remotion Plugin in Claude Code When You Lack Claude Motion

## TL;DR

Tristen O'Brien says Claude Motion (prompt to editable animation) is only on Team and Enterprise plans in beta. On Pro or Max, add the Remotion plugin to Claude Code and ask for animations that use Remotion, which also renders video from code.

## Why it matters

Both tools write code instead of generating pixels, so every word, color and timing stays editable rather than regenerating the clip. O'Brien says Remotion has been how he made the animations in his videos from the start. The differences he lists: Motion is built into Claude and processes in the cloud, while Remotion renders on your own computer, needs more setup, and edits usually go through Claude (it also has its own editor). He says Remotion is free for most people but larger companies using it for company work need a license, and that it works alongside the Higgsfield connector.

## How to apply

1. In Claude, open Customize > Plugins and search Remotion, or install it from the terminal (he recommends the terminal).
2. Prompt for the result and name the tool, for example: build an animation of a paper clock tower that morphs into a rocket ship, using Remotion.
3. Change a single word or timing by asking Claude to edit that part of the code.
Checked: Claude Code 2.1.303 has the `claude plugin` subcommands (configure, details, enable, disable, eval and more), but the Remotion plugin listing itself could not be checked offline. Plan availability of Motion is the creator's statement.

## Related

[[hyperframes-claude-code-video-rendering-pipeline]], [[higgsfield-mcp-for-cinematic-motion]], [[claude-design-animation-template-for-branded-motion-graphics]]
