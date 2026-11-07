---
id: gemini-cli-fallback-for-blocked-research-sites
created: 2026-08-31
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/simon-scrapes/you-re-using-claude-code-wrong-these-10-tips-will-change-everything_20260307.txt
---

# Fall Back to the Gemini CLI When a Site Blocks Claude's Fetching

## TL;DR

In automated research workflows, route pages Claude cannot fetch through the Gemini CLI as a fallback, so blocked sites do not leave holes in the research.

## Why it matters

Some sites block Claude's web fetching, and an automated research workflow that silently skips them produces analysis with missing sources. A second CLI with its own fetching path keeps those sources reachable without manual copy-paste.

## How to apply

In your research skill or workflow, add a fallback step: when a fetch fails because the site is blocked, retrieve the page via the Gemini CLI and feed the content back into the run. Keep fact verification as the final step of the workflow as usual.

## Related

[[fact-verification-table-for-claude-claims]]
