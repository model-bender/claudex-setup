---
id: have-an-owner-enable-channels-on-team-and-enterprise-plans
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-to-put-claude-code-on-a-vps-in-10-minutes_DMdqpLr2DlQ_20261120.txt
---

# On a Team or Enterprise plan, have an Owner enable channels before debugging a silent bot

## TL;DR

If Claude Code is logged in with a Team or Enterprise plan, channel messages do not arrive until channels are enabled for the organisation.

## Why it matters

The creator lists this as a common issue when setting up on a team plan. Per the docs, with the setting off or unset the plugin's MCP server still connects and its tools work, but channel messages do not arrive; a startup warning says so. Pro, Max and Ultra users without an organisation skip the check.

## How to apply

An Owner turns it on at claude.ai Organization settings > Claude Code > Channels, or an admin sets `channelsEnabled` to `true` in managed settings. Then restart the session with `--channels`.

Checked: Live docs https://code.claude.com/docs/en/channels.md fetched 2026-11-22 with curl, plus installed binary claude 2.1.330: 'Enable channels for your organization ... requires the Owner role, or by setting `channelsEnabled` to `true` in managed settings'. `channelsEnabled` present in binary 2.1.330.

## Related

[[relaunch-claude-code-with-channels-after-configuring-a-channel-plugin]]
