---
id: set-disable-remote-control-rather-than-trusting-the-rc-toggle
created: 2026-09-24
status: active
supersedes: null
category: remote-access
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/88094
---

# Set disableRemoteControl:true, Don't Trust the /rc Toggle, After a Silent Server-Side Default Flip

## TL;DR

Remote Control silently turned itself on for existing sessions in August via a server-pushed GrowthBook-style flag combination (remote_control_auto_enable, remote_control_auto_on_by_default, ide_rc_auto_enable_gate), independent of your local /rc setting; the durable fix is the disableRemoteControl:true settings.json key, not the in-app toggle.

## Why it matters

One commenter traced it to the extension's config payload from Anthropic's backend and confirmed it's server-driven, not a local regression; another found the visible toggle doesn't reliably persist off ("Setting is OFF, still all my sessions start with remote control") because the preference only writes to disk on a state *change*, so flipping it ON then OFF is what actually persists it. Remote Control has a materially different risk profile (a phone/browser can drive your session) than ordinary local use, so an undisclosed default-on flip is a real exposure, not just an annoyance.

## How to apply

Add `"disableRemoteControl": true` to `~/.claude/settings.json` (documented in claude-code-settings.schema.json, described there as covering claude.ai/code, `claude remote-control`, the `--remote-control`/`--rc` flags, auto-start, and the in-session toggle) rather than relying on the /rc in-session switch, which this thread shows can silently re-enable itself. Checked: `disableRemoteControl` confirmed as a real settings.json key in the installed 2.1.281 binary (command grep -c -a: 10 hits), including its schema description text and its use in the `/doctor` and org-policy check paths.

> "After the last update the remote control is being turned on by default for all sessions.", GitHub anthropics/claude-code#88094

## Related

[[remote-control-off-with-non-anthropic-base-url]], [[prefer-remote-control-over-channels-unless-you-need-images]]
