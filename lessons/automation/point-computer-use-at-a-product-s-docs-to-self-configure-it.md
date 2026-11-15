---
id: point-computer-use-at-a-product-s-docs-to-self-configure-it
created: 2026-08-07
status: active
supersedes: null
category: automation
tool: [claude-code, codex]
source_type: post
sources:
  - https://x.com/_catwu/status/2073149354412822738
  - transcripts/john-kim/building-apps-with-ai-is-hard-until-you-learn-this_8fvUXkotDPc_20261108.txt
---

# Hand Computer Use a Product's Setup Docs and Let It Click Through the Integration Wizard

## TL;DR

Instead of clicking through a multi-step web setup by hand (an integration wizard, TestFlight, an OAuth client for Google sign-in, an ad network), point the agent's computer use at the product's setup docs or console, give it a short brief about you and the app, and answer its questions.

## Why it matters

Connect-your-sources onboarding is repetitive, fully documented, and low-judgment, which is exactly the shape computer use handles well, yet most people still click through it out of habit. The safety objection is also weaker than it looks: it stops and checks before connecting by default, and each new connection scope is its own approval, so you keep a decision point at every distinct blast radius. John Kim did TestFlight, a Clerk Google OAuth client and AdMob setup this way through computer use in Codex once his app worked, and says many people stall at this step because reading the docs and finding everything takes a while.

## How to apply

Enable computer use, then prompt with a link to the target product's setup or docs page and ask it to complete onboarding. Give it a short brief of who you are, what the app is and the business, then answer the questions it asks. If you want checkpoints at different points than the default, say so in the prompt: per Cat Wu, "you can tell it when you want it to check and it's good at adhering to it".

> "Small tip: You can use Claude Code with computer use to set up Claude Tag. Just point it to the Claude Tag docs and it will connect your team's GitHub repo, data warehouse, google drive, and other data sources for you!", Cat Wu

## Related

[[human-in-the-loop-checkpoint-design]]
