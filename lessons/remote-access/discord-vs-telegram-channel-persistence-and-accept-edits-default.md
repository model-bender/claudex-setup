---
id: discord-vs-telegram-channel-persistence-and-accept-edits-default
created: 2026-07-10
status: active
supersedes: null
category: remote-access
sources:
  - transcripts/mark-kashef/did-claude-code-just-make-openclaw-obsolete_RUyqEAXt2YQ_20260704.txt
---

# Pick Discord Over Telegram for Remote Claude Code if You Need Conversation Memory

## TL;DR

Remote Claude Code channels differ by platform: Telegram has no history API (no memory across messages) and a 50MB attachment cap, while Discord can fetch the last 100 messages for persistence; both default to accept-edits mode (not bypass permissions), so file sends and actions get blocked with permission prompts until you explicitly loosen them.

## Why it matters

The channel you pick silently changes behavior - a Telegram bot forgets the back-and-forth between messages, and the accept-edits default surprises people whose bot 'starts typing then stops' when asked to send an image, because attachments are blocked until permissions are raised. This is separate from the allowlist-vs-pairing lockdown you also need.

## How to apply

Choose Discord when you want the bot to remember recent context; use Telegram for lightweight one-shot dispatch. After setup, loosen permissions past accept-edits if you need it to send files or take actions unattended, run it as a background process for always-on access, and (as covered elsewhere) switch it from pairing to an allowlist. You can hand the fiddly Discord OAuth/dev-portal setup to Claude in Chrome to click through for you.
