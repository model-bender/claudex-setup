---
id: run-codex-browser-qa-concurrently-while-claude-keeps-building
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
---

# Run Codex Browser QA Against the Running App While Claude Keeps Building - It's Read-Only, So They Don't Collide

## TL;DR

Point Codex's computer use at the localhost app with 'click every button, try to break it, find bugs' while Claude Code keeps writing features in the same folder; because the QA pass only reads and clicks, the two sessions coexist as long as each is told what the other owns.

## Why it matters

Fable plus nine Opus/Sonnet workers finished a V1 and self-reported it verified (screenshotted PDFs, geometry checks, a full customer journey smoke test). Codex's browser pass then found two launch blockers those agents had missed: the review/sign-off gate wasn't enforced (it generated a real client deck while the baseline was still unconfirmed), and 'regenerate deck' stayed enabled with zero pains, zero solutions, and a negative investment - producing a client-facing 0x ROI slide. It ran over 20 minutes, exercised inputs the builders never tried (typing 'red' into a field that needs a hex value), and returned findings tiered as blockers / high / medium plus a list of what passed. The concurrency is the operational unlock: Nate explicitly notes 'it's not going to change anything, so over here back in Claude I can have it start building out some other stuff without interfering.'

## How to apply

Start the app on localhost, then in Codex: 'This is V1, open at <localhost URL>. Use your computer use, click every button, try to break it, try to upload different formats, find visual and functional bugs and edge cases. When you're confident you've tested enough to say whether this is customer-ready, tell me what needs to change.' In the same prompt, name what the other session owns - 'Claude Code is currently building the onboarding and payment flow in a different session, don't touch that' - and give the Claude session the reciprocal note. When the report comes back, decide who fixes: handing it to Codex as a `/goal` ('you found these, you're the orchestrator, fix the blockers and highs, verify they're truly fixed, use computer use') keeps Claude free to continue elsewhere. Watch the live browser window - you see it clicking, which tells you what it actually exercised.

## Related

[[hand-the-bug-list-back-to-the-agent-that-found-it-as-the-fixer]]
