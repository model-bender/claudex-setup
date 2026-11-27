---
id: artifact-with-inline-editing-and-a-copy-changes-button-for-feedback
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/how-i-d-rebuild-my-claude-setup-from-scratch-80-20-rule_g6tmqwTULk8_20260923.txt
---

# Collect feedback through an artifact with inline editing and a copy-all-changes button

## TL;DR

Ask Claude for an artifact that shows the draft, lets reviewers edit it in place, and has a button that copies all their changes, so the feedback comes back as text you can paste straight into Claude.

## Why it matters

Reviewers need no tooling and you get their changes in a form Claude can apply directly, which removes the friction on both sides of a review.

## How to apply

Use the prompt from the transcript: "Create an artifact that shows this email visually with the copy we just worked on. Let my team edit it directly inline and add a button that copies all their changes so they can send it back to me." Share the link, then paste what they send back into the session.

Checked: Artifacts are documented for Claude Code (live docs fetched with curl on 2026-11-22, artifacts page; Claude Code 2.1.330): published to a private claude.ai URL and shared from the page header, on Pro, Max, Ultra, Team and Enterprise plans. The inline-edit and copy button are page behaviour the prompt asks for, not a built-in feature; the docs suggest the same kind of export control ("Copy as prompt") for bringing a page's result back into the session.

## Related

[[share-the-claude-design-link-for-non-technical-review]]
