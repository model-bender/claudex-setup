---
id: give-bulk-fix-work-an-external-audit-score-as-its-target
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/jono-catliff/claude-code-seo-audit-fix-your-whole-website-in-1-prompt-steal-this_M2KJ5-sFbbg_20260910.txt
---

# Wire an External Auditing Tool In as the Scoreboard Before Asking for a Site-Wide Fix

## TL;DR

For sprawling fix-everything work, connect a third-party auditor that emits a number (a site-audit score, a Lighthouse report) and make that score the target. The agent then has an objective definition of done it can re-measure itself, instead of your adjective.

## Why it matters

Jono Catliff's run went from 61 to 97 out of 100 precisely because the score existed: the Semrush audit and Google Lighthouse enumerate the concrete errors and warnings, so 'fix my SEO' becomes a finite checklist with a before and after reading. Without an external scorer the agent grades its own homework on a task where the failure modes (missing meta description, uncrawlable page) are invisible from inside the repo.

## How to apply

Stand up the auditor first and run a baseline: connect the audit tool as an MCP connector where one exists, or export its report (Search Console exports a CSV zip) and drop the files into the project. Tell the agent the score is the target, name the tool, and have it re-run the audit after each pass so the number moves in front of you. Lighthouse is free and local for performance, accessibility, best practices and SEO.

## Related

[[visual-self-validation-screenshot-grading]], [[claude-seo-and-claude-ads-third-party-skill-packs]]
