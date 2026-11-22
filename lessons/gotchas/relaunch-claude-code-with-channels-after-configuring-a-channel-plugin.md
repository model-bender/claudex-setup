---
id: relaunch-claude-code-with-channels-after-configuring-a-channel-plugin
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-to-put-claude-code-on-a-vps-in-10-minutes_DMdqpLr2DlQ_20261120.txt
---

# After configuring a channel plugin, exit and relaunch Claude Code with the --channels flag

## TL;DR

The bot only answers when Claude Code was started with `--channels` naming the plugin. `/reload-plugins` does not start the channel, so exit and relaunch with the flag.

## Why it matters

The creator presents the relaunch as a workaround for when the plugin 'doesn't fully reload'. The live docs make it a required step: the channel plugin only begins polling for messages when the session is started with the flag, and the bot can only reply while that session is running.

## How to apply

Run `/exit`, then `claude --channels plugin:telegram@claude-plugins-official`. If the bot does not respond to a message, this is the first thing to check.

Checked: Live docs https://code.claude.com/docs/en/channels.md fetched 2026-11-22 with curl, plus installed binary claude 2.1.330: step 'Restart with channels enabled' and the note 'If your bot doesn't respond, make sure Claude Code is running with `--channels`'. /reload-plugins exists in the binary; docs say it only makes the configure command available. Transcript wording corrected from optional to required.

## Related

[[vps-tmux-telegram-persistent-sessions]]
