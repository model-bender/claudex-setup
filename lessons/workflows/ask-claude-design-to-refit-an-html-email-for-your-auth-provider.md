---
id: ask-claude-design-to-refit-an-html-email-for-your-auth-provider
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-design
sources:
  - transcripts/austin-marchese/17-things-you-didn-t-know-claude-design-could-do_7rRVwjzVQsc_20260910.txt
---

# After Designing an HTML Email, Ask Claude Design to Refit It for Your Auth Provider's Variables

## TL;DR

Design the email first, then ask Claude Design how to bring it into the system that actually sends it: it re-emits the HTML with that provider's template variables so you can paste it straight in.

## Why it matters

A beautiful email you cannot wire into your sender is useless, and hand-converting hardcoded copy into a provider's variable syntax is where these redesigns usually die. Marchese's default Supabase login email had looked bad for three months; after the redesign, one follow-up question ('how can I take this and bring it into my Supabase for my automated login email') produced a variable-ready version that was live in minutes. Claude Design understands the backend it is generating for, not just the layout.

## How to apply

Prompt 'design an HTML email for X', iterate on the look, then ask how to bring it into your sender (Supabase, Resend, your ESP) for the specific automated email. Take the returned HTML with its template variables and paste it into the provider's template editor, then send yourself a test.

## Related

[[hand-off-claude-design-exports-to-claude-code]], [[name-the-real-api-in-the-claude-design-wizard]]
