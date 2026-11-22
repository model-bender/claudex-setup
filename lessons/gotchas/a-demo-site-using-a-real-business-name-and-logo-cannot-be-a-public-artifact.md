---
id: a-demo-site-using-a-real-business-name-and-logo-cannot-be-a-public-artifact
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/the-simplest-way-to-make-money-online-with-claude-ai-in-2026_XSehihyKFqw_20261120.txt
---

# A demo site that uses a real business's name and logo cannot be published as a public Claude artifact: deploy it elsewhere

## TL;DR

Claude declined to turn a prospect's rebuilt homepage into a public artifact because it carried the company's real name, logo and branding; the video falls back to Vercel for a shareable link.

## Why it matters

The artifact is treated as internal-only when it depends on a third party's identity, so sending a cold prospect an artifact link will not work.

## How to apply

Ask Claude Code to check for the Vercel CLI, install it if missing, and walk you through the sign-in so it can deploy. Keep all demo sites as paths under one Vercel project rather than one project each.

Checked: Checked 2026-11-22: consistent with the Artifact tool's published rules in this session, which forbid pages that use a real organization's name or branding. The Vercel flow was not run.
