---
id: name-gsap-for-claude-code-scroll-animations
created: 2026-09-01
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/jono-catliff/how-i-built-insane-claude-design-websites-in-10-minutes_xYv4_cTOSNM_20260701.txt
---

# Name GSAP Explicitly When Asking Claude Code to Animate a Claude Design Handoff

## TL;DR

When handing a Claude Design export to Claude Code, naming the GSAP animation library in the build prompt gets scroll-triggered entrance animations, floating buttons, and moving stat counters layered onto the static export automatically.

## Why it matters

The creator's one-shot prompt, "build this Claude design website using Next.js, and can you use the library GSAP to be able to add animations to the page wherever appropriate," produced text-flying-in, a slider, and scroll-tied number counters with no further prompting. Without naming a library, Claude Code has to invent its own animation approach, with less predictable results.

## How to apply

In the Claude Code prompt that rebuilds a Claude Design export, name the framework (e.g. Next.js) and explicitly request GSAP for animations, e.g. "use the library GSAP to add animations to the page wherever appropriate, as many stunning animations as possible without it looking cheesy." Browse demos.greensock.com for concrete effects to reference by name in follow-up prompts.

## Related

[[hand-off-claude-design-exports-to-claude-code]]
