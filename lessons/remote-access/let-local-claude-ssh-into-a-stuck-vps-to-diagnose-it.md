---
id: let-local-claude-ssh-into-a-stuck-vps-to-diagnose-it
created: 2026-11-22
status: active
supersedes: null
category: remote-access
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-to-put-claude-code-on-a-vps-in-10-minutes_DMdqpLr2DlQ_20261120.txt
---

# When a VPS Claude Code Setup Won't Work, Let Your Local Claude SSH In and Investigate

## TL;DR

If the remote Claude Code setup breaks in a way you cannot explain, give a local Claude Code session SSH access to the VPS so it can look around and find the cause.

## Why it matters

The speaker says that if you give the Claude Code you use locally the VPS root password, it can get into the server, look around and work out why things are not working, which helps when you get stuck. This lesson's inference: giving an agent a root password is a real security trade, so use a throwaway or low-value server and rotate the credential afterwards.

## How to apply

1. Keep the VPS address and login in your local project's .env (the speaker has Claude save it there) so the session can use it.
2. Start a local Claude Code session and ask it to SSH into the VPS and investigate the specific failure (in the video, problems while setting up the Telegram plugin).
3. Have Claude save the server's details, the commands used and how to get in into a project in your notes, so it can help the next time something goes wrong (the speaker does this for his VPS).
4. This lesson's inference: rotate or remove the credential if you shared a password.

Checked: No mechanism claim (plain ssh from a Claude Code session; nothing version-specific).

