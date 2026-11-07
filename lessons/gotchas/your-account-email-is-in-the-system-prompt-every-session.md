---
id: your-account-email-is-in-the-system-prompt-every-session
created: 2026-08-16
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/81138
---

# Your Account Email Is in Claude Code's System Prompt - Redact Before Sharing a Transcript

## TL;DR

Claude Code reads `oauthAccount.emailAddress` from `~/.claude.json` and emits a `# userEmail` block into the system prompt on every session; it is documented nowhere and the only code path that skips it is having `ANTHROPIC_UNIX_SOCKET` set.

## Why it matters

This compounds a gotcha already in the corpus: the feedback-survey share now uploads your CLAUDE.md. Together they mean "share my transcript" actually means "share my account email plus my project instructions" - to whoever receives it, including a public issue tracker or a recorded demo.

It also corrects a likely-false assumption about `IS_DEMO=1`: that flag masks the email in the header and in outputs, but does **not** remove it from the system prompt. A demo recorded with `IS_DEMO=1` still leaks the address to anyone who gets the model to repeat its system prompt.

Verified first-hand: a live Opus 5 session's system prompt contains a `# userEmail` block naming the signed-in account's address.

## How to apply

Check for the `# userEmail` block before sharing a transcript, filing a feedback survey, pasting a system-prompt dump, or publishing a screen recording. Confirm what your own install injects with:

```
jq '.oauthAccount.emailAddress' ~/.claude.json
```

> "Claude Code takes personal data I gave Anthropic in order to authenticate, and injects it into the model's system prompt on every session — automatically, without my consent, without disclosing that it does so, and with no supported way to stop it.", anthropics/claude-code issue #81138

## Related

[[feedback-survey-share-now-uploads-your-claude-md]], [[keep-credentials-out-of-the-agent-sandbox]], [[is-demo-masks-the-email-on-screen-not-in-the-system-prompt]]
