---
id: hand-the-bug-list-back-to-the-agent-that-found-it-as-the-fixer
created: 2026-09-12
status: active
supersedes: null
category: agents
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
---

# Make the Agent That Found the Bugs the One That Fixes and Re-Verifies Them

## TL;DR

Hand a QA agent's own findings straight back to it ('you found these, you are the orchestrator, fix the blockers and highs, then verify they are truly fixed'), so the session that was building keeps building.

## Why it matters

Two things fall out of it. The finder already holds the reproduction context, so the fix skips a re-diagnosis round, and it can re-drive the exact path it broke the app on to prove the fix rather than asserting it. Meanwhile the building session never has to stop and context-switch onto a bug list, which is the entire reason the concurrent QA pass was worth running in the first place.

## How to apply

When the QA report comes back, reply in the same session with the orchestrator framing: it owns the blockers and highs, it verifies each fix through the same surface it found them on, and it reports back anything it could not fix. Tell the other session what the fixer now owns, so the two do not collide on the same files.

## Related

[[run-codex-browser-qa-concurrently-while-claude-keeps-building]]
