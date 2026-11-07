---
id: seed-design-system-with-a-real-brand-kit
created: 2026-07-17
status: active
supersedes: null
category: configuration
tool: claude-design
sources:
  - transcripts/jono-catliff/claude-code-web-design-10-years-covered-in-66-minutes_2Gda_ZvV1V4_20260701.txt
  - transcripts/jono-catliff/how-i-built-insane-claude-design-websites-in-10-minutes_xYv4_cTOSNM_20260701.txt
  - transcripts/tristen-o-brien/claude-design-basics-master-95-in-10-minutes_20260610.txt
---

# Seed a Claude Design System With a Real Brand Kit Instead of Letting Claude Pick

## TL;DR

Don't let Claude choose your colors and fonts. Create a design system seeded with real brand source material: upload reference screenshots into the "add fonts, logos, and assets" field and paste a text brand kit into the notes field, then reuse that system across every prototype, deck, and site.

## Why it matters

Everything Claude Design generates without a design system looks good but generic, Claude picked the palette, the fonts, and the style choices, so the output is "okay" but reads as AI rather than as your brand. The design system is the one feature that fixes this and the one most people skip.

Seeded from real source material it extracts the full kit, palette (text/surface/brand/accent), typography, buttons, icons, logos, gradients, border radii, and then reuses the same architecture everywhere, which is what stops per-page style drift.

**Build ONE and iterate it, not five.** Generation is the single most expensive action in Claude Design (5-15 minutes of ingest), and this system becomes the `design.md` behind every future deck, page, video, and app screen. A markdown+logo system measured ~6% of a Max 20x weekly allowance.

## How to apply

In Claude Design go to design systems → create. Upload screenshots of the reference site (take several, not one) into the fonts/logos/assets field, and paste a text kit into the additional-notes field. Generation takes about 5 minutes. Sites like getdesign.md publish free text kits for ~70 major brands.

Feed it the **minimum that carries brand signal**, logo PNG, a brand-concept markdown (colors, typography, voice), a feel note for anything that doesn't exist yet ("buttons should feel modern, with a slight glow behind them"). Import Figma if you have it. Attach a GitHub repo or URL **only** when you have a live site whose real components matter: that path works well (it reproduced a site's typography, spacing, and copy voice closely enough that a new page "feels exactly like the website") but costs materially more for little extra signal, "it really just needs key elements like the colors, the logo, the typography." See [[attach-only-the-files-claude-design-needs]].

Then work the review queue, approving or rejecting each tile, colors, accents/gradients, neutrals, type, spacing, buttons, badges, cards, and publish. A spurious "missing brand fonts" warning can be ignored if the type tiles are right. This queue is also where you catch a redrawn logo ([[claude-design-redraws-uploaded-logos]]).

Two gotchas:

- **When the screenshots and the pasted text kit disagree, the text kit wins.** Stripe buttons came out rounded per the `design.md` spec even though the screenshots showed square ones. Treat the pasted text as the authority and screenshots as supporting evidence.
- **Publish the design system before starting a prototype**, or it won't be selectable. Confirm the chip appears in the prompt box after selecting it.

## Related

[[precompute-the-design-system-outside-claude-design]], [[split-brand-and-structure-sources-in-one-design-prompt]], [[text-brand-kit-overrides-screenshots-in-claude-design]], [[publish-the-design-system-before-starting-a-prototype]]
