---
id: attach-a-prompt-or-agent-hook-to-stop-so-a-second-model-checks-the-work
created: 2026-10-19
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-changed-completely-every-new-concept-explained_YAuWBqZ_gjs_20261018.txt
---

# Attach a Prompt or Agent Hook to the Stop Event So a Second Model Checks the Work Before Claude Can Finish

## TL;DR

A hook no longer has to be a script: a prompt hook has a small model read the conversation, and an agent hook can open files, and either can send Claude back to work with a reason when the work is not acceptable.

## Why it matters

A CLAUDE.md line such as 'follow the brand voice' is a request, while a hook runs every time. Simon Scrapes shows a Stop hook where a second model looks at the finished work (for example a report against a brand-voice document) and answers yes or no with a reason, and the reason goes back to Claude as its next instruction. He says the agent hook is marked experimental.

## How to apply

1. Ask Claude to add a Stop hook that reads your brand voice doc and the latest report and checks the report against it. 2. Choose the type: `prompt` (reads the conversation only, quick and cheap) or `agent` (can open files such as the voice doc and the draft). 3. A prompt hook's prompt can use the $ARGUMENTS placeholder for the hook input JSON and can pin a model with a `model` field (default is the small fast model). 4. Expect the 8-consecutive-block cap on Stop hooks (from the related lesson, not this transcript), so do not rely on it as the only gate. Checked: claude 2.1.303 binary: hook schema has type 'prompt' ('LLM prompt hook type', 'Use $ARGUMENTS placeholder for hook input JSON', optional model defaulting to the small fast model) and 'Agentic verifier hook type'; an error string says 'agent hook answers ok or not ok'. The 'reason is fed back as the next instruction' behaviour is the speaker's description, not tested.

## Related

[[stop-hook-8-block-cap]], [[retest-prompt-and-agent-hooks-written-as-instructions]], [[add-a-stop-hook-that-blocks-finishing-when-code-was-written-but-not-run]]
