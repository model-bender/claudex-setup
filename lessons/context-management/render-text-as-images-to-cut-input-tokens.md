---
id: render-text-as-images-to-cut-input-tokens
created: 2026-07-25
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/austin-marchese/paste-this-into-claude-never-hit-a-token-limit-again_SFh6MMe-XcM_20260719.txt
---

# Feed Bulk Reference Text as an Image, Not Text, to Cut Its Token Cost

## TL;DR

Claude tokenizes images at a different rate than text, so a page rendered as an image can cost meaningfully less than the same page as text, the creator cites roughly 10k tokens of text landing at 3–4k as an image, a 60–70% reduction.

## Why it matters

For large static reference material that only needs to be read once, the tokenizer *is* the entire cost, and the image path sidesteps it. The transcript is honest about the trade-offs, which is what makes this usable rather than a gimmick: OCR is imperfect, so the model will not read the text perfectly, and there is a non-zero chance Anthropic changes image pricing and closes the gap entirely. It is a measured optimisation with an expiry date, not a permanent property of the platform.

## How to apply

Use an open-source converter (PXpipe on GitHub) to render the text into images and attach those instead of the raw text. Reserve it for bulk reference material where a small transcription error is tolerable, never for code, config, or anything you will act on verbatim. Measure with `/context` before and after rather than trusting the ratio, and re-check it periodically, since it depends entirely on current image pricing.

## Related

[[be-a-context-minimalist-provision-a-lean-harness]]
