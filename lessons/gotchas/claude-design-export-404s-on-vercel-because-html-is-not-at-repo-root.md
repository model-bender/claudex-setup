---
id: claude-design-export-404s-on-vercel-because-html-is-not-at-repo-root
created: 2026-07-17
status: active
supersedes: null
category: gotchas
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-design-builds-beautiful-3d-websites-instantly-full-tutorial_TcFeSjwTo7g_20260624.txt
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
---

# A Claude Design Export Pushed Straight to Vercel 404s: the HTML Isn't at the Repo Root

## TL;DR

Vercel serves a static repo from its root, but a Claude Design export nests the site under its own project folder, so the first deploy returns 404 Not Found. The fix is moving or renaming the entry file to `index.html` at the root.

## Why it matters

This hits on a clean Design → zip → Claude Code → GitHub → Vercel chain, and it presents as a **deploy** failure, so it's easy to start debugging Vercel instead of the file layout.

The export's folder shape (background video, scraps/sketch, uploads, HTML) is faithful to the Design project, not to what a static host expects.

## How to apply

Paste the error back to Claude Code with the full context:

> I pushed this to GitHub, synced it to Vercel to host it, and got this 404. What does it mean, how do I fix it, and do you need any more info from me?

It identifies the root-path mismatch and renames the entry to `index.html`; Vercel redeploys on the push in ~30 seconds.

Before pushing at all, have Claude Code serve the export on localhost and confirm it renders, and remember a localhost URL is not shareable with anyone else.

## Related

[[hand-off-to-claude-code-from-the-project-root-not-a-page]], [[scaffold-the-target-framework-before-pasting-the-design-handoff]], [[claude-design-builds-desktop-only-check-mobile-before-shipping]]
