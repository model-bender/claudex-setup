---
id: write-goal-conditions-whose-proof-appears-in-the-transcript
created: 2026-10-19
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-changed-completely-every-new-concept-explained_YAuWBqZ_gjs_20261018.txt
  - transcripts/simon-scrapes/how-the-top-1-use-claude-code-differently_J9NQTYUP6k0_20261013.txt
---

# Write a /goal Condition That Can Be Proved From the Conversation, Because the Checker Reads Only the Transcript

## TL;DR

After each turn a small model judges whether the /goal condition is met, and it judges from the conversation only. A condition like 'the report is finished' gets taken on Claude's word, so name evidence that will appear in the chat.

## Why it matters

Simon Scrapes explains that the goal checker does not open files or run anything, so an ambiguous goal ends early on Claude's say-so. His fix is a goal that demands visible proof, such as a script's passing output, plus a turn cap. This is stronger than the existing advice to have a measurable finish line, because it says where the proof must live.

## How to apply

1. First have Claude build a deterministic check (for example a check-report script; making it exit non-zero on failure is this lesson's addition). 2. Write the goal so the proof must be printed in the conversation: `/goal the check-report script passes and you show me its output. Stop after 15 turns.` 3. Avoid conditions that can only be confirmed by looking at a file the checker never sees. Checked: claude 2.1.303 binary contains the evaluator text 'Based on the conversation transcript above, has the following stopping condition been satisfied? Answer based on transcript evidence only.' and 'You are evaluating a stop-condition hook in Claude Code. Read the conversation transcript carefully'. The 15-turn figure is the speaker's example. Docs check (code.claude.com/docs/en/goal via Context7): the condition and the conversation so far go to the configured small fast model, which "does not call tools, so it can only judge what Claude has already surfaced in the conversation"; ANTHROPIC_DEFAULT_HAIKU_MODEL (18 hits in the 2.1.303 binary) changes the evaluator model. The second video gives a fuller goal form: one end state, how to prove it, what must not change, and a turn limit, for example '/goal The check report script passes and you show me the output. The template is unchanged, or stop after 15 turns.'

## Related

[[give-goal-runs-a-finish-line-and-a-stop-after-clause]], [[goal-verifiable-finish-lines-with-safety-caps]]
