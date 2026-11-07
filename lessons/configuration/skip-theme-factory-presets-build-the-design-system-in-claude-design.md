---
id: skip-theme-factory-presets-build-the-design-system-in-claude-design
created: 2026-08-22
status: active
supersedes: null
category: configuration
tool: [claude-design, claude-code]
sources:
  - transcripts/simon-scrapes/the-only-claude-cowork-setup-busy-entrepreneurs-actually-need_BMEaJTl3Vo0_20260820.txt
---

# Skip Theme Factory Presets, Generate a Real Design System in Claude Design and Export It

## TL;DR

Anthropic's theme factory presets carry no design tokens and no heading scale and are shared by everyone using them, so build the system in Claude Design's design systems feature instead and drop the export into your context folder.

## Why it matters

Two separate problems with the preset route: the presets (botanical garden and friends) are basic, giving you a colour palette and typography but no design tokens, no header sizes and no spacing scale, so downstream generation still improvises the details; and because they are publicly available, every other business using them produces work that looks the same. A real system produces variety with continuity, the same fixed colours and fonts across outputs that are not identical, which is what makes a feed look coherent. Claude Design's design systems feature takes reference material (slides you like, colour schemes, landing pages, dashboards) and emits the full definition including fonts, colours, heading sizes, spacing and how boxes are drawn, which you then download and keep as a file rather than regenerating per project.

## How to apply

In the Claude desktop app, use the design button to open Claude Design, go to design systems and create one, feeding it examples of designs you actually like. Download the result and store it in your shared context folder as a markdown identity file plus a tokens JSON holding fonts, colours, spacing and header sizes. Starting from nothing, source a palette from a site like Huemint and a font pairing from Font Pair, specifically to avoid the default Inter that AI design tools reach for. Reference the identity file from CLAUDE.md so anything visual pulls from it without re-prompting.

## Related

[[source-palette-from-huemint-and-fonts-from-font-pair]]
