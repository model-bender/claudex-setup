---
id: diagnose-the-symptoms-behind-a-feature-request-before-building-it
created: 2026-10-19
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/ray-amjad/your-prompts-are-too-small-for-claude-code_RbfQayMNtJc_20261018.txt
---

# Have Claude Diagnose What Users Do With a Requested Feature Before Building It

## TL;DR

For a request like CSV export, ask Claude to find the underlying symptom, as a doctor would, instead of building the button.

## Why it matters

Ray Amjad's example: users ask for CSV export, but most may be importing it into Google Sheets every Monday, some emailing it to an accountant, and a few want the button. The resulting features would be a live Google Sheets sync, a monthly statement email and the CSV button. This is illustrative, not data from a real product.

## How to apply

Tell Claude the feature request, say a good doctor asks about symptoms rather than writing the prescription, and have it use the data sources it can reach (support tickets, analytics) to find how the output is used before it plans. Checked: prompt technique, nothing to verify against the binary.

