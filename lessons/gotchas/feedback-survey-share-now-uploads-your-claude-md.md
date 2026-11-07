---
id: feedback-survey-share-now-uploads-your-claude-md
created: 2026-08-07
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Know That Sharing a Feedback-Survey Transcript Now Uploads Your CLAUDE.md Too

## TL;DR

Consenting to the in-app feedback survey's transcript share now also uploads the last request's system prompt, which includes your CLAUDE.md instructions, plus tool definitions and model parameters. It is no longer just the conversation.

## Why it matters

Secrets are redacted, but proprietary process, internal conventions, and business detail written into CLAUDE.md are not secrets in the credential sense and travel with the share. Someone filing a routine bug report would not expect it to carry their project instructions, so the consent prompt is easy to accept on the old mental model of "this sends my conversation".

## How to apply

Before clicking share on the feedback survey, decide whether your CLAUDE.md content is safe to send. On client or confidential projects, decline the share or scrub CLAUDE.md first. Note the fields are dropped first if the share is too large, so their presence is not guaranteed either way.

> "Changed the feedback-survey transcript share: with your consent it now also uploads the last request's model settings — the system prompt (which includes your `CLAUDE.md` instructions), tool definitions, and model parameters.", Claude Code CHANGELOG 2.1.224

## Related

[[quiet-mode-env-vars-for-client-and-confidential-work]], [[keep-credentials-out-of-the-agent-sandbox]]
