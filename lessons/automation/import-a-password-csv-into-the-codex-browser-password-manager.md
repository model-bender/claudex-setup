---
id: import-a-password-csv-into-the-codex-browser-password-manager
created: 2026-08-22
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/codex-s-browser-agent-automates-literally-anything_CB5bG4mvnS0_20260820.txt
---

# Import Credentials Into Codex's Built-In Password Manager Instead of Pasting Them Into Chat

## TL;DR

Codex's in-app browser has a password manager you load from a CSV in settings, so a site that keeps logging you out (banks, anything with a short session) can still be automated without your password ever entering the chat transcript.

## Why it matters

Session persistence covers most sites (X, Instagram and school stay signed in across new chats), but security-conscious platforms boot you out; the creator's banking platform Relay came back with "Relay is open at the login screen, but you have to sign in again" on the second run of a saved skill. The naive fix is pasting the password into the prompt, which writes it into chat history that persists and is re-read on later turns. The password manager keeps the credential out of the conversation while still letting the browser agent fill the form: on the retry, Codex pulled the entry, typed the email and password, logged in, and completed the statement download flow. It does not solve second factors, and the creator explicitly flags automating a phone-delivered 2FA code (technically possible on a Mac via computer use) as something to be careful about.

## How to apply

Build a CSV with the columns name, URL, username, password, notes. Open Codex settings, go to the browser's password manager, and import the CSV as a file. In the prompt, tell it to use the password manager for the site rather than supplying the credential yourself, for example "try this again in the password manager for the in-app Codex browser, you should be able to log in now, then run the skill on June". Keep sites with mandatory 2FA on a manual login step, and treat any flow touching money as supervised rather than scheduled.
