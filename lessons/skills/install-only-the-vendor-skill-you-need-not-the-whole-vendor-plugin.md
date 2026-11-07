---
id: install-only-the-vendor-skill-you-need-not-the-whole-vendor-plugin
created: 2026-10-19
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-tried-100-github-repos-for-claude-these-6-are-the-best_HhZdNYI4pJs_20261013.txt
---

# Install Only Stripe's best-practices Skill Rather Than the Whole Plugin, and Test Supabase as One Read-Only User

## TL;DR

Nate Herk warns that Stripe's full plugin might route every vendor decision through Stripe, so take only the stripe best practices skill, and set the Supabase connector read-only.

## Why it matters

Vendor skills encode that vendor's security rules (users see only their own data, verify a payment really came from Stripe). A whole plugin can steer unrelated choices toward the vendor.

## How to apply

Install the single Stripe skill 'stripe best practices'. Set the Supabase connector to read only, log in as one test user before launch and confirm you cannot see other users' data. Checked: not installed; the plugin-routing concern is Nate's wording ('might try to'), not confirmed here.

## Related

[[two-tenant-test-for-cross-tenant-leakage]], [[supabase-mcp-for-backend-sync]], [[curate-a-bulk-skill-pack-before-installing-not-after]]
