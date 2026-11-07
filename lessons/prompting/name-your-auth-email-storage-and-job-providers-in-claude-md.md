---
id: name-your-auth-email-storage-and-job-providers-in-claude-md
created: 2026-10-25
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1x8ufrn/i_ran_claude_code_118_times_on_blank_repos_to_see/
---

# Name Your Auth, Email, Storage and Job Providers in CLAUDE.md, or Claude Code Hand-Rolls Them

## TL;DR

In the poster's 118 headless runs on blank Next.js and FastAPI repos with Sonnet 5.5, Claude Code picked Stripe and Sentry every time but wrote its own auth, caching, email sending and background jobs unless the prompt named a provider.

## Why it matters

If you meant to use a hosted auth, email, storage or queue provider, you get home-made session handling and raw SMTP code instead, and auth is the code you least want hand-rolled. This is one person's experiment on one model and two stacks.

## How to apply

Add a short stack-decisions block to CLAUDE.md naming the provider for auth, email, storage and background jobs, or name the provider in the prompt for any feature that touches those areas.

> "when there's one obvious incumbent (stripe, sentry) it goes straight there. everywhere else it mostly writes the thing itself, even auth. vendors outside that short list basically don't show up unless the prompt names them.", u/n1kusha13 on r/ClaudeCode

