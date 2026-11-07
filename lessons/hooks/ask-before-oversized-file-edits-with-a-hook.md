---
id: ask-before-oversized-file-edits-with-a-hook
created: 2026-09-12
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Make a Hook Ask Whether to Split Any File It Is About to Push Past 1,000 Lines

## TL;DR

Models still write 2,000 and 3,000 line files. A function hook can call the ask primitive on every edit to a file over your line threshold and offer to refactor it into smaller files before the edit lands.

## Why it matters

File size is the kind of standard that decays: it sits in CLAUDE.md, gets followed for a while, and quietly stops holding as context fills. A hook checks it on every single edit, and because it asks rather than blocks, you keep the call on the ones where a big file is genuinely right.

## How to apply

Ask /plugin-authoring for a hook that, on every file edit beyond your threshold, asks whether the file should be refactored into smaller files. Pick the threshold you actually enforce in review, and delete the corresponding CLAUDE.md line once the hook is live.

## Related

[[modularize-files-over-500-lines-to-cap-context-cost-of-edits]], [[write-askuserquestion-into-skill-question-steps]]
