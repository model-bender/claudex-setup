---
id: upstream-idle-timeout-on-free-models-work-in-smaller-chunks
created: 2026-08-29
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/this-stealth-model-makes-claude-code-free-here-s-how__kK_4cOYF4o_20260824.txt
---

# "Upstream idle timeout exceeded" on free OpenRouter models: tell Claude to work in smaller chunks

## TL;DR

Free OpenRouter models routinely throw an "upstream idle timeout exceeded" API error mid-run when a single step tries to write or read too much (or the free endpoint is congested); instructing the session to work in smaller chunks makes the run complete.

## Why it matters

The error looks like a fatal infrastructure failure and can stall an otherwise-working BYO-model session repeatedly. The creator hit it on a landing-page build and again on a research task. The cause was the model "trying to write so much and look through so much" in one step against a free endpoint with tight idle limits; once he told it to work in smaller chunks "it basically ended up being fine, and it kept going". Knowing the one-line workaround turns an apparent dead end into a minor speed bump.

## How to apply

When a free-model session in Claude Code errors with upstream idle timeout exceeded, don't switch models immediately: reply telling Claude why it happened and to break the work into smaller units (smaller file writes, fewer files per pass, narrower searches) and continue. If it recurs constantly, the endpoint may just be saturated; switch the env slots to a different free model or the free-models router.

## Related

[[use-openrouters-free-models-router-as-a-rate-limit-fallback]], [[route-claude-code-to-cheaper-or-local-models]]
