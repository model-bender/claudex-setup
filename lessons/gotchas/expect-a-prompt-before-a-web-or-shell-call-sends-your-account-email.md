---
id: expect-a-prompt-before-a-web-or-shell-call-sends-your-account-email
created: 2026-11-06
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/107757
  - https://www.reddit.com/r/ClaudeCode/comments/1xhqvzn/opus_55_just_shared_my_email_address/
---

# Agents Have Put Your Account Email in Outbound Request Headers: Update to 2.1.317 and Keep the Privacy Mod On

## TL;DR

Claude Code puts your account email in the system prompt, and in one week several users caught agents copying it into the User-Agent header of fetches to sites like Wikipedia. Since 2.1.317 a built-in mod asks before a web or shell call sends the address.

## Why it matters

Sites that ask automated clients for contact details get the one identifier the model has, with no permission prompt, and users reported spam after research runs. The CHANGELOG entry for 2.1.317 reads "Added a check that asks before a web or shell tool call sends your account email address to the network", and the maintainer says the mod is on by default and can be turned off in /plugins.

## How to apply

Run 2.1.317 or later and leave the built-in cc-plugin-privacy mod enabled. On older builds, or in automation where nobody can answer the prompt, treat the address as exposed: review outbound requests from research subagents, or strip the address from the prompt with a mod.

Checked: claude 2.1.318 binary: cc-plugin-privacy 3 hits; the 2.1.317 CHANGELOG line is in the fetched changelog.

> "We introduced a built-in mod called `cc-plugin-privacy` to deterministically block this behavior in v2.1.317 and later", Anthropic maintainer, anthropics/claude-code issue 107757

## Related

[[your-account-email-is-in-the-system-prompt-every-session]], [[is-demo-masks-the-email-on-screen-not-in-the-system-prompt]]
