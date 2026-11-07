---
id: use-the-apify-mcp-server-for-sites-that-block-or-need-javascript
created: 2026-10-19
status: active
supersedes: null
category: mcp
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-tried-100-github-repos-for-claude-these-6-are-the-best_HhZdNYI4pJs_20261013.txt
---

# Use the Apify MCP Server When Claude Gets an Empty Page From Instagram, Reddit or Other JavaScript-Heavy Sites

## TL;DR

Apify's MCP server connects Claude to ready-made cloud scrapers for sites that block it or need JavaScript, returning results as a spreadsheet.

## Why it matters

Nate Herk says Claude cannot natively reach sites like Instagram and Reddit, which block it or need JavaScript, so it gets an empty page. His example prompt asked for Chicago bakeries on Instagram with follower counts and no website in the bio, and returned a spreadsheet a couple of minutes later.

## How to apply

Add the Apify MCP server and describe the data you want. Per the transcript the connector is open source but the scrapers run on Apify's cloud, the free plan gives five dollars of credit a month, and other actors may cost per result. Firecrawl is named as another open-source option. Checked: not installed or run; pricing and behaviour are as stated in the transcript.

## Related

[[firecrawl-mcp-for-web-to-markdown]], [[gemini-cli-fallback-for-blocked-research-sites]]
