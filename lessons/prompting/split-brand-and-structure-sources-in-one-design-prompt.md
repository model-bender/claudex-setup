---
id: split-brand-and-structure-sources-in-one-design-prompt
created: 2026-07-17
status: active
supersedes: null
category: prompting
tool: claude-design
sources:
  - transcripts/jono-catliff/claude-code-web-design-10-years-covered-in-66-minutes_2Gda_ZvV1V4_20260701.txt
  - transcripts/jono-catliff/how-i-built-insane-claude-design-websites-in-10-minutes_xYv4_cTOSNM_20260701.txt
---

# Split the Brand Source From the Structure Source in One Design Prompt

## TL;DR

Point Claude Design at two different references with explicitly different jobs: "use the design system for the branding, and use the attached screenshot for the page structure."

## Why it matters

The brand you want to look like and the layout you need are rarely the same site. Copying Stripe wholesale gives you Stripe's page structure, which is built to sell software to developers, not services to clients.

Splitting the sources lets you take Stripe's palette, type and buttons while taking your section order (hero, CTA, logo wall, proof) from a site that sells what you actually sell. Naming which reference governs which layer is what stops the model blending them arbitrarily.

## How to apply

Build the design system from the brand you're emulating. Separately, find a page whose structure matches your business (Dribbble, durable.com, or any site in your category), screenshot it, and attach it to the prototype prompt.

Then be explicit about the division of labour:

> Generate a five-page site for my SEO agency, homepage, about, pricing, contact, projects. Use the brand design system for the branding, and use the screenshot attached for the page structure.

Expect the structure to carry over and the aesthetic not to.

This is the mirror image of the Mobbin technique, where the screenshot supplies colour and font and you forbid it from touching layout. Pick whichever layer you want the screenshot to govern and say so.

## Related

[[seed-design-system-with-a-real-brand-kit]], [[attach-only-the-files-claude-design-needs]]
