---
id: log-generation-batches-in-a-tracker-sheet-and-feed-performance-back
created: 2026-08-29
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/turn-claude-into-a-one-person-marketing-team-in-38-mins_yCACmFTiCto_20260824.txt
---

# Have Claude maintain a tracker sheet of every generation batch (angle, model, cost), then feed performance data back in

## TL;DR

After asset-generation runs, ask Claude to build and update a spreadsheet logging each batch's date, type, campaign, primary angle, models used, credits/dollars spent, and status; later add real performance numbers so the next batch is steered by what actually worked, not vibes.

## Why it matters

Generated creatives pile up in output folders where you can't compare angle-versus-outcome, and generation spend is invisible until it isn't. Claude built the tracker from one vague prompt: a generation log keyed by ID with angle, deliverables, generations billed, tool and model (Nano Banana Pro, GPT Image 2, Seedance 2.5), credits, dollars, and status, plus tabs for creative assets, angle performance, a copy bank, and a cost summary. Once views/engagement/conversion data lands in it, the loop closes: "have it every week review what it made, review what did well, and make more of what did well." It also enables cheap iteration: reuse a winning batch and change only the copy instead of regenerating.

## How to apply

After a few batches, prompt: "Create an Excel/Google Sheet logging date, generation type, campaign, primary angle, outputs, models used, and cost for everything we've generated; I want to analyze later which angles and copy worked best." Require every future run to end with its cost and to append itself to the sheet (or add a routine that sweeps sessions and updates it). Drop ideas into the sheet and tell Claude to "check the sheet and process anything new"; when platform analytics exist, have a weekly pass write performance into the angle-performance tab and propose the next batch from the winners.

## Related

[[explicit-numeric-receipts-for-automations]]
