---
id: run-slash-design-inside-the-project-folder-so-it-reuses-your-tokens
created: 2026-09-12
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-code-just-dropped-design-master-it-in-8-minutes_Fqlc0N1qyMo_20260910.txt
  - transcripts/tristen-o-brien/claude-design-get-dangerously-good-at-website-animation_c3B5OMF9MNs_20260910.txt
---

# Run /design Inside the Project Folder and Tell It to Invent Nothing New

## TL;DR

/design reads the folder it is launched in for existing colours, fonts, logos and components. Run it in the real project and say 'use my elements, do not invent anything new' to get concepts already in your design system.

## Why it matters

Tristen O'Brien states the default explicitly: '/design is going to start looking at your project folder, it's going to look to see if you have any colors, any fonts, any logos, any components', and in his demo an empty folder made it 'act like it's a brand new project'. The folder you happen to be in is therefore a silent input to every generation. Run it in a scratch directory and you get a good-looking page in someone else's brand that then costs a second pass to retrofit onto your tokens.

## How to apply

Open Claude Code in the repo that owns the design system, then run /design there and state the constraint in the brief: 'here is the page layout I like, but use my colours, fonts, logo and components, do not invent anything new.' Deliberately choose an empty folder only when you want a greenfield look and are willing to trade the brand anchor for it.

## Related

[[seed-design-system-with-a-real-brand-kit]], [[fix-code-bias-with-empty-folder-isolation]], [[iterate-ui-as-design-artboards-before-implementing]]
