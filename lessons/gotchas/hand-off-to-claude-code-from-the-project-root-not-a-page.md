---
id: hand-off-to-claude-code-from-the-project-root-not-a-page
created: 2026-07-17
status: active
supersedes: null
category: gotchas
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/jono-catliff/claude-code-web-design-10-years-covered-in-66-minutes_2Gda_ZvV1V4_20260701.txt
---

# Hand Off to Claude Code From the Project Root: From an Open Page You Only Export That Page

## TL;DR

Claude Design's share → hand off to Claude Code scopes the export to wherever you are. Trigger it while a single page is open and you get that one page, silently losing the other four.

## Why it matters

This fails quietly. The handoff command copies fine, Claude Code builds fine, and you don't discover the other pages are missing until you're already iterating on the build, at which point regenerating them costs Claude Design quota you were trying to conserve by moving to Claude Code in the first place.

## How to apply

Exit out of any open page so you're on the main project folder, then share → hand off to Claude Code → copy command.

After the Claude Code build, verify the page count against the design before iterating.

## Related

[[hand-off-claude-design-exports-to-claude-code]], [[scaffold-the-target-framework-before-pasting-the-design-handoff]]
