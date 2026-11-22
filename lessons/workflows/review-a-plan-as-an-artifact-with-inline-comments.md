---
id: review-a-plan-as-an-artifact-with-inline-comments
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/stop-watching-tutorials-build-these-4-claude-artifacts-to-10x-output_QBClwotyT3Y_20261103.txt
---

# Review a plan as an artifact: comment inline on each item, send the comments to Claude, then tell the session to build what you approved

## TL;DR

Publish the plan (or list of proposals) as an artifact, mark each item 'do this' or 'don't do this' in inline comments, send them to Claude so it revises the artifact, then return to the chat and ask it to implement the approved items.

## Why it matters

Per the creator, the agent then builds exactly what was marked to do and skips what was not, and the visual form makes the final product easier to see and supports more in-depth planning. The creator recommends it for anything with a complicated plan: automations, document processing, a new product feature.

## How to apply

Ask for the plan as an artifact, comment on the page, use Send to Claude (or mention `@claude`) on the thread, repeat, then in the session: 'create the ones I said to do'.

Checked: `Send to Claude` present in Claude Code 2.1.330 binary; artifacts.md (live docs at code.claude.com fetched 2026-11-22) documents comments, Send to Claude and `@claude`, needs v2.1.221 or later, and describes commenting by people an artifact is shared with inside an organisation.

## Related

[[interactive-html-artifacts-for-design-decisions]]
