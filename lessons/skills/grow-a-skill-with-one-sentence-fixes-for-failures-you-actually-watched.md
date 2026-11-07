---
id: grow-a-skill-with-one-sentence-fixes-for-failures-you-actually-watched
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/matt-pocock-s-exact-system-to-10x-your-claude-skills_QsU0f-547rQ_20261002.txt
---

# Grow a Skill by One-Sentence Fixes for Failures You Watched, and Add Nothing You Have Not Seen Fail

## TL;DR

Pocock does not run evals. They use the skill on real work for about a week and add one line per observed break.

## Why it matters

The video shows the grill-me skill's change history, where each line answered a failure: 'give your recommended answer' (conversations dragging), 'ask one question at a time' (multiple questions were bewildering), 'do not enact the plan until I confirm' (agent skipped ahead and built), 'split facts from decisions' (agent started grilling itself). The test: if you no longer have to send the result back, it works.

## How to apply

Run the skill on real work, not test cases. At the end of the week have Claude analyse your conversation history for results you sent back, and turn each recurring one into one sentence in the skill. Then stop and retry before adding anything else.

Verified: Speaker's practice, not tested. Claude Code 2.1.287.

## Related

[[diagnose-and-update-the-smallest-durable-place-after-a-skill-correction]]
