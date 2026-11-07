---
id: put-api-keys-only-in-dot-env-files
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/master-97-of-codex-in-1-hour-full-course_3TdD8Qv5Tk8_20260626.txt
---

# Always Put API Keys in a Dot-Prefixed .env File, Never a Custom-Named Secrets File

## TL;DR

When Codex creates a credentials file, it's named .env.local (or .env); put your keys only there, not in an arbitrarily-named file like secrets.txt.

## Why it matters

Codex (and git) treat dot-prefixed env files as excluded from commits by convention, so a key placed there won't be accidentally pushed to a public repo; a custom-named file gets no such protection.

## How to apply

When Codex asks for an API key, paste it into the .env/.env.local file it created (or ask it to create one) rather than any other file, and let it explain that it will avoid committing that file.

## Related

[[keep-credentials-out-of-the-agent-sandbox]]
