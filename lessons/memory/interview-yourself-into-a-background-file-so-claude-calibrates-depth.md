---
id: interview-yourself-into-a-background-file-so-claude-calibrates-depth
created: 2026-09-12
status: active
supersedes: null
category: memory
tool: claude-code
sources:
  - transcripts/austin-marchese/the-art-of-becoming-self-educated-with-claude_7DJk83sc5xg_20260910.txt
---

# Have Claude Interview You Once Into a Background File, So It Stops Explaining at the Wrong Level

## TL;DR

Run a one-off prompt that interviews you about your role, current work and what you already know, and have it write the answers to a background file the project loads. Every later explanation then starts from your actual baseline instead of from scratch.

## Why it matters

Austin Marchese's point is that the model only behaves like a full-time teacher if it holds state about you; without that file it re-guesses your level on every topic and either over-explains fundamentals or skips the gap you actually have. He answers the interview by voice rather than typing, which produces longer and more candid answers than a typed reply.

## How to apply

Prompt: 'Interview me one question at a time about my role, what I am building, what I already understand well, and where I know I am weak. When you have enough, write it to <file>.md as a background profile you should read before explaining anything to me.' Answer with voice input (the mic button, or /v in Claude Code) rather than typing. Reference the file from CLAUDE.md so it loads, and update it when your baseline moves. This is a personal-context file, distinct from a brand-voice profile used for writing output.

## Related

[[brand-voice-quiz-for-fast-voice-profile]], [[voice-dictation-for-longer-richer-prompts]], [[gitignored-personal-claude-md-for-machine-specific-notes]]
