---
id: wire-an-image-video-api-key-into-a-design-skill-for-missing-assets
created: 2026-08-29
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-built-the-ultimate-claude-website-design-skill-steal-this_QUI6Ug4cHnE_20260824.txt
---

# Give a design skill an image/video-model API key so it autogenerates the assets the brief lacks

## TL;DR

Put an aggregator API key (e.g. kie.ai, an OpenRouter-equivalent for image and video models) in the Claude Code project's environment variables and have the design skill call it to fill asset gaps: it generates missing images, turns images into videos, and stitches clips per the skill's instructions.

## Why it matters

Design builds usually stall on assets the client doesn't have; with a generation API wired in, the same session that designs the page also manufactures its imagery to match the brief and brand guidelines. The skill decides how much gets generated versus graded from owned assets (its intake asks exactly that), and the creator's runs produced style-constrained assets on demand, e.g. "minimalistic geometric low-poly human figures" matching the brand color scheme, plus image-to-video conversions synced to scroll animations. An aggregator key means one credential covers many image/video models instead of one integration per vendor.

## How to apply

Create an account on the aggregator (kie.ai in the transcript), grab an API key, and put it in the environment variables of the Claude Code project. In the skill, spell out the asset pipeline: check what real assets exist in the project, generate what's missing via the API, convert images to video where motion is needed, and stitch results ("it will do whatever it needs to do because the skill tells it how"). Constrain generated assets by style and brand guidelines in the brief so they don't read as generic AI output.

## Related

[[higgsfield-mcp-for-cinematic-motion]], [[one-hero-clip-scrubbed-by-scroll-for-an-immersive-site]], [[shared-brand-context-folder-for-all-skills]]
