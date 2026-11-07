---
id: claude-design-export-standalone-html-vs-full-zip
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-design
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
---

# Export a Single Standalone HTML File From Claude Design When You Don't Need the Design Files

## TL;DR

Claude Design's Share menu offers a standalone-HTML export as well as the full project zip; use standalone HTML for a quick handoff to a skill or Claude Code and the zip only when you actually need the underlying design-system files.

## Why it matters

A handoff that only needs the finished page (e.g. running a redesign or brutalist skill against it) fails or gets slower if you paste in a whole project zip's worth of files; the tool that expects a single file, like the taste skill's redesign command, needs the HTML content directly, and one build in this transcript hit an error until the standalone HTML was used instead of the full download.

## How to apply

In Claude Design, click Share, then choose the export type: send to local coding agent, send to Claude Code web, download the whole project as a zip, or export as standalone HTML. Pick standalone HTML for single-file handoffs to a Claude Code skill; pick the zip only when the receiving step needs the original design assets.

## Related

[[bracket-claude-design-with-claude-code-skills]], [[hand-off-claude-design-exports-to-claude-code]]
