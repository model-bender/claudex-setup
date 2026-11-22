---
id: shared-artifact-links-need-a-claude-account-to-open
created: 2026-11-06
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/austin-marchese/7-new-claude-features-to-get-you-ahead-of-99-of-people-using-ai_BgbJFggbTVE_20261106.txt
  - transcripts/austin-marchese/stop-watching-tutorials-build-these-4-claude-artifacts-to-10x-output_QBClwotyT3Y_20261103.txt
---

# Whether a Shared Claude Slide-Deck Link Needs a Claude Account Depends on How It Is Shared

## TL;DR

Austin warns that people need a Claude account to open a slide-deck artifact link you send them. That holds when the artifact is shared with named people or with an organization, but most artifacts shared with "Anyone with the link" open with no account or sign-in. Slides can be exported to PowerPoint, PDF or Google Slides instead.

## Why it matters

Austin lists this as a gotcha people miss after landing on a good deck. His artifacts video shows a different case: a micro-tool artifact made publicly accessible from the share menu opens with no login, so the account requirement depends on how the artifact is shared. Corrected in place on 2026-11-22: the title and TL;DR said every shared deck link needs a Claude account, which the current docs contradict (the id keeps its old name so existing links still resolve).

## How to apply

Before sending a deck link, check the share setting. For recipients without Claude accounts, choose "Anyone with the link" (on Team and Enterprise plans an Owner must first turn on External sharing), then open the link signed out, since some artifacts show part or all of their content only after sign-in. If it does not open, export the slides to PowerPoint, PDF or Google Slides.

Checked: Live pages https://code.claude.com/docs/en/artifacts.md and https://support.claude.com/en/articles/9547008-share-artifacts fetched 2026-11-22 with curl, Claude Code 2.1.330 installed: 'Publicly: share a link that anyone on the internet can open, with no claude.ai sign-in required' and 'To open an artifact shared with them or with your organization, people sign in to Claude. Most artifacts shared with "Anyone with the link" open without a Claude account or sign-in.'

Inference, not from the source: Choosing export as the workaround is the lesson's, based on the export options he lists.
