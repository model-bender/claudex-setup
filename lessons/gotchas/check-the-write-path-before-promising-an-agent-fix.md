---
id: check-the-write-path-before-promising-an-agent-fix
created: 2026-09-12
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/jono-catliff/claude-code-seo-audit-fix-your-whole-website-in-1-prompt-steal-this_M2KJ5-sFbbg_20260910.txt
---

# Check What the Agent Can Actually Edit Before Promising a Fix, Or the Deliverable Is Only a Report

## TL;DR

Claude can only fix what it has a write path to. Custom-coded sites and WordPress give it one; closed hosted builders often do not, and the same run then degrades from 'fixed' to 'here is a list for you to paste in by hand'.

## Why it matters

Jono Catliff calls this his big caveat: the audit half runs anywhere, but the fix half depends on whether the platform connects. He splits the platforms explicitly, custom code and WordPress fine, Squarespace, Weebly, Unbounce, GoDaddy, Wix, GoHighLevel and Framer limited, and he still ends up handling the Google Business Profile manually because the API route costs a 14-day review that is not worth it. Finding this out after the run is how a fix-everything promise turns into hours of manual copy-paste nobody budgeted for.

## How to apply

Before scoping the work, establish the write path: repo or filesystem access, an official API, or an MCP connector with write scope. If there is none, plan for two deliverables instead of one, the audit report plus a manual implementation list the agent walks you or a teammate through. Where the API exists but costs a long approval, decide up front whether manual is cheaper.

## Related

[[give-bulk-fix-work-an-external-audit-score-as-its-target]], [[contain-agents-at-environment-layer-not-permission-prompts]]
