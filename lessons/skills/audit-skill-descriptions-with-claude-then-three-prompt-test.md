---
id: audit-skill-descriptions-with-claude-then-three-prompt-test
created: 2026-09-24
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/anthropic-engineer-explains-what-to-build-instead-of-ai-agents_HIRDzMtuWFk_20260920.txt
---

# Have Claude Code Audit Your Skill Descriptions for Overlap, Then Verify With Three Prompts

## TL;DR

Ask Claude Code to review every installed skill's description for what it does, when it should trigger, and where it overlaps with other skills, rewriting only the ambiguous ones. Verify each rewrite with three test prompts: an obvious match, a differently worded match, and an unrelated request that should not fire it.

## Why it matters

Progressive disclosure only works if Claude can tell skills apart from their YAML description alone; two overlapping descriptions ('help with content' vs 'create marketing assets') leave Claude guessing. Delegating the audit to Claude itself, rather than reading every skill by hand, scales to a real-sized skill library, and the three-prompt test catches both under-triggering and over-triggering in one pass.

## How to apply

Prompt: 'Review all my skill descriptions. For each one, tell me what it does, when it should trigger, and where it overlaps with any other skills. Rewrite only descriptions that are ambiguous.' Then for each rewritten skill, run three prompts: an obvious request that should trigger it, a differently worded request that still should trigger it, and an unrelated request that definitely should not trigger it. No specific CLI mechanism is named here, this is a prompting/audit technique, not a flag.

## Related

[[skill-description-is-routing-logic-not-marketing]], [[explainability-test-to-prune-overlapping-skills]], [[skills-complementary-not-overlapping]]
