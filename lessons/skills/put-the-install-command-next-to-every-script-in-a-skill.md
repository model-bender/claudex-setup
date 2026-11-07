---
id: put-the-install-command-next-to-every-script-in-a-skill
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everything-you-know-about-skills-is-outdated_e7TY56-yIvM_20261002.txt
---

# Put the install command next to each script in a skill so it works on a teammate's machine

## TL;DR

Do not write 'use the PDF library'. Write 'install the required package' with the package name beside the script. If it is already installed Claude skips the step.

## Why it matters

Simon Scrapes says a skill works on your laptop because you installed its dependencies months ago and forgot, then breaks on day one for a teammate or a fresh Cowork session. Claude is smart enough to skip the install when the package is present.

## How to apply

For every script in a skill folder, put the install line (with the package name) next to it in SKILL.md. Check each skill you plan to share.

Verified: Anthropic skill best practices page, fetched 2026-10-02: section 'Avoid assuming tools are installed' with the 'Install required package: pip install pypdf' example.

## Related

[[skills-add-scripts-to-avoid-repeated-api-scaffolding]]
