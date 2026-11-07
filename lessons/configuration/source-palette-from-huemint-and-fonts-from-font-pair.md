---
id: source-palette-from-huemint-and-fonts-from-font-pair
created: 2026-08-31
status: active
supersedes: null
category: configuration
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/simon-scrapes/the-only-claude-cowork-setup-busy-entrepreneurs-actually-need_BMEaJTl3Vo0_20260820.txt
---

# Source a Palette From Huemint and a Font Pairing From Font Pair to Escape the AI-Default Inter Look

## TL;DR

When you have no existing brand, pull a colour palette from Huemint and a font pairing from Font Pair instead of letting the tool choose, specifically to avoid the default Inter that AI design tools reach for.

## Why it matters

AI design tools converge on the same typographic and colour defaults, so unseeded output looks like everyone else's regardless of how good the layout is. Deliberately sourcing the palette and pairing from outside the tool is the cheapest way to give generated visuals a distinct identity from day one.

## How to apply

Pick a palette on Huemint and a pairing on Font Pair, then put them into the brand or identity file that your design generation reads (for example the markdown identity file plus tokens JSON in your shared context folder). Do this once, before generating, so every downstream output inherits the choices.

## Related

[[skip-theme-factory-presets-build-the-design-system-in-claude-design]]
