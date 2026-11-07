---
id: name-the-real-api-in-the-claude-design-wizard
created: 2026-07-17
status: active
supersedes: null
category: prompting
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/john-kim/how-to-build-an-app-with-claude-code-no-experience-required_20260603.txt
---

# Name Your Real API in the Claude Design Wizard to Get a 1:1 Handoff

## TL;DR

Claude Design front-loads a wizard before generating. Use it to pin the actual backend or library you'll build against (not just look and feel), and pick the fully-working/full-flow option, so the prototype is wired to the real data source and transfers ~1:1 into code.

## Why it matters

Claude Design builds real functionality behind the scenes, not just pictures, which is why the handoff translates so cleanly. But that only pays off if the prototype was built against the thing you'll actually ship on.

Answer the wizard purely on aesthetics and you get a beautiful mock wired to a fake map. Name the real API and the export arrives with the integration already working, so Claude Code is porting a functioning prototype instead of rebuilding it.

## How to apply

When the wizard asks its questions, answer the design ones however you like ("decide for me" is fine for a throwaway), but override the technical ones with your real choices, pinning OpenStreetMap specifically returned an export pulling genuine OpenStreetMap tiles.

Choose the full-flow / fully-working option rather than a static mock.

Verify the payoff at handoff: the ported app should hit the real API on first run.

## Related

[[scaffold-the-target-framework-before-pasting-the-design-handoff]], [[keep-the-claude-design-brief-open-enough-to-trigger-its-question-round]]
