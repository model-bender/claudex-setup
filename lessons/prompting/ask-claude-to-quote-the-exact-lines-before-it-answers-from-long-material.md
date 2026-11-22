---
id: ask-claude-to-quote-the-exact-lines-before-it-answers-from-long-material
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/everyone-ignore-these-claude-concepts-but-they-change-everything_6VjeXzvpoJo_20261120.txt
---

# Ask Claude to quote the exact lines it relies on before it answers from long documents

## TL;DR

For long documents, have Claude extract word-for-word quotes first and then answer from them, so the answer stays tied to the text.

## Why it matters

The video presents this as the companion to putting data first: the quoted lines act as evidence and keep the answer to what the document says. Anthropic's docs give the tip for tasks involving long documents (over 20k tokens); the video gives no size limit.

## How to apply

Add to the prompt, after the pasted material: first quote the exact lines you are using, then answer. This lesson's inference from the docs' framing: it matters most for long inputs.

Checked: Checked 2026-11-22: Anthropic docs 'Reduce hallucinations' say 'For tasks involving long documents (>20k tokens), ask Claude to extract word-for-word quotes first before performing its task'. The >20k threshold comes from the docs, not the video.

## Related

[[put-long-reference-documents-before-the-question]]
