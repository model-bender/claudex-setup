---
id: have-claude-verify-a-responsive-site-with-the-playwright-plugin
created: 2026-10-02
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/jono-catliff/full-claude-code-masterclass-beginner-to-expert-in-2-hours-2026_R3mx8XHX8ns_20261002.txt
---

# Have Claude check and fix a site at phone, tablet and desktop widths with the Playwright plugin

## TL;DR

Install the Playwright plugin from /plugin, then ask Claude to check the site at each size and fix breakage, such as a hamburger menu on phone.

## Why it matters

Jono Catliff first shows the manual check in browser developer tools with the device toolbar set to responsive. Then the Playwright plugin takes control of the browser, opens the mobile navigation, moves to tablet and desktop widths and takes screenshots that Claude views to confirm nothing is broken.

## How to apply

Run /plugin, search for playwright and install it, then open a new conversation. Prompt Claude to check the whole site on phone, tablet and desktop and fix anything broken, naming what you want (for example a hamburger menu on mobile).

Verified: Claude Code 2.1.287: /plugin is documented in the commands reference (code.claude.com/docs/en/commands.md) and the binary contains the id playwright@claude-plugins-official. Whether the plugin installs mid-session without a restart was not tested; the creator says to open a new conversation after installing.

## Related

[[drive-playwright-for-browser-automation-and-authed-scraping]], [[claude-design-builds-desktop-only-check-mobile-before-shipping]]
