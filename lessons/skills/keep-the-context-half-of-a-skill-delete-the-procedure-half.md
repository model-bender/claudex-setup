---
id: keep-the-context-half-of-a-skill-delete-the-procedure-half
created: 2026-08-22
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-deleted-all-my-claude-skills-and-claude-got-smarter_XNQBCRcwXV4_20260820.txt
---

# When Pruning Skills for a New Model, Delete the Procedure and Keep the Brand/Context Half

## TL;DR

Boris Cherny's advice to delete your CLAUDE.md, skills, and hooks every ~6 months resolves, in practice, into a split: strip the step-by-step recipe (which caps a smarter model) but keep the parts the model cannot infer - where your files live, your header image, your brand colors, your links.

## Why it matters

Anthropic deleted over 80% of Claude Code's system prompt for the Opus 5 release because most of it existed to correct behaviours the model now gets right unprompted, and Boris Cherny's explicit recommendation to users is 'every 6 months delete your Claude MD, delete your skills, delete your hooks, see what the model does.' But a straight deletion loses real information. Nate Herk ran the A/B: same prompt (turn this interview URL into a YouTube resource guide) with his full skill set versus a fresh session with no skills and no CLAUDE.md. The skilled run produced a nine-page guide with his header image, brand colors, and channel links; the bare run looked messier but organised the content better - it broke the interview into named ideas each with a timestamp, a structure his skill had never told it to use. The conclusion is that the procedural half of the skill was suppressing a better structure, while the brand half was carrying information the model had no way to guess.

## How to apply

Duplicate the repo (or just start a fresh session in an empty folder), remove CLAUDE.md and the skills, run a real task you care about with the same prompt, and diff the two outputs by content quality rather than polish. Then rewrite the skill to contain only what the bare run couldn't have known: asset paths, brand guidelines, where files live, which links go in the header and footer - phrased as 'produce the guide however you see fit, but use this image as the header and link the channel at the top.' Do this pass on every model release, not on a calendar. Note the scope caveat Nate raises: advice from people who build harnesses and train models is calibrated to their work, so treat 'delete everything' as a hypothesis to A/B on your own tasks rather than a blanket instruction - his own conclusion after testing was to rework skills, not sweep-delete them.
