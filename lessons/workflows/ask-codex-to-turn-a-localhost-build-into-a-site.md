---
id: ask-codex-to-turn-a-localhost-build-into-a-site
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/master-96-of-codex-in-under-35-minutes_DFlELTiSPk8_20261009.txt
  - transcripts/john-kim/stop-using-codex-in-terminal-it-s-holding-you-back_yK9GnaE9rlY_20261017.txt
---

# Ask Codex to 'turn that into a site' to share a localhost build

## TL;DR

A localhost URL only works on your machine. To share what Codex built, ask it to turn it into a site, then choose who can open it.

## Why it matters

The speaker shows two hosted sites with different access (one open to anyone with the URL, one only for the speaker's own account), plus analytics, a custom domain and an attached database.

## How to apply

In the Codex desktop app, say 'can you turn that into a site' (the speaker's phrasing; the docs' documented triggers are the word 'website' in the prompt or a mention of @Sites). From the docs: Sites has no management view in the Codex CLI or IDE extension, so create and manage the site in the desktop app or ChatGPT on the web. A new site is limited to its owner and workspace admins until you change its access under Share. Analytics is under the site's More actions > Analytics; a custom domain is added in the site's settings with Add domain, costs extra hosting credits, and is not available in Enterprise workspaces at launch.

Checked: Sites, sharing levels, analytics and custom domains confirmed in the live Codex docs (learn.chatgpt.com/codex/sites and its create, publish-and-sharing and manage pages, fetched 2026-11-22). Not checkable in codex-cli 0.171.0, because the docs say Sites has no CLI management view. The '/site' slash command the speaker mentions is not on the docs' slash-commands page (learn.chatgpt.com/codex/reference/slash-commands), so it is unverified and only the natural-language form is given.

## Related

[[share-a-local-internal-tool-over-a-mesh-vpn-instead-of-deploying-it]]
