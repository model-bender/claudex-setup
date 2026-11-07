---
id: set-skill-detail-per-step-by-how-fragile-the-step-is
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everything-you-know-about-skills-is-outdated_e7TY56-yIvM_20261002.txt
---

# Set each skill step's degree of freedom by what breaks if Claude does it differently

## TL;DR

Give plain goals where many approaches work, a template where a preferred shape exists, and an exact script where the step is fragile. One skill can mix all three.

## Why it matters

Simon Scrapes, citing Anthropic's three levels: high freedom is plain instructions (their example, a code review process or reviewing a sales call), medium is a template with settings (a weekly client report), low is an exact command with no changes (a database migration, or in a business setting raising invoices or removing members). Their test for each step: what happens if Claude does it differently. If little changes, loosen it. If something consequential changes, lock it down.

## How to apply

For each step in a skill, ask that question. Write the writing step of an invoicing skill as plain instructions and the invoice-creation step as a script with few or no parameters. Low freedom usually means a script rather than more plain text, because a script runs the same way every time.

Verified: Anthropic skill best practices page, fetched 2026-10-02: section 'Set appropriate degrees of freedom' with high (text instructions), medium (pseudocode or scripts with parameters) and low (specific scripts, few or no parameters).

## Related

[[skills-add-scripts-to-avoid-repeated-api-scaffolding]]
