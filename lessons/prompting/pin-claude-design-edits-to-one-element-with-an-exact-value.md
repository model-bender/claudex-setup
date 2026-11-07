---
id: pin-claude-design-edits-to-one-element-with-an-exact-value
created: 2026-07-17
status: active
supersedes: null
category: prompting
tool: claude-design
sources:
  - transcripts/jono-catliff/how-i-hacked-claude-design-usage-bypass-limits_GPCF1XKYiD8_20260701.txt
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Pin Every Small Claude Design Edit to One Element and Name the Exact Value

## TL;DR

Use the comment/edit/draw tools on the specific element instead of describing the change in chat, state the exact value you want, and make one change per message. Anything purely deterministic goes through direct edit, which costs nothing.

## Why it matters

A pinned comment carries its own target, so Claude edits `style.css` directly instead of re-reading the page to work out what you meant. A header-resize measured this way cost 2% of a weekly limit, versus "significantly more" for the same change in Claude Code where you can't point at the element. Anthropic's own design team calls per-element interaction the recommended way to use the tool.

Vagueness is what actually drains the quota: the death spiral is "hey, this looks ugly" → Claude guesses → "that looks even uglier" → credits gone.

And Claude Design only executes one thing per message anyway, bundling a removal and a global price change returned just the removal.

## How to apply

Toggle comment, edit or draw in the toolbar, click the element, and type the change with a number in it: "8px radius", "reduce the size of the main header", "more subtle orange on the focus box", not a vibe.

Queue changes one at a time and let it reload after the batch.

For deterministic changes (body copy, font, background) use direct edit instead of prompting. It behaves like WordPress/Webflow/Framer and spends no tokens at all.

Note the edit surface is still glitchy at the design-system file level: repeated "preview failed to render" on per-file edits that worked fine per-design.

## Related

[[claude-design-cannot-place-freeform-or-invent-graphics]], [[opus-to-generate-sonnet-to-edit-in-claude-design]], [[screenshot-paste-instead-of-describing-ui-problems]]
