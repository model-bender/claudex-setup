---
id: say-internal-browser-or-codex-may-grab-your-real-chrome
created: 2026-09-12
status: active
supersedes: null
category: gotchas
tool: codex
sources:
  - transcripts/mark-kashef/gpt-6-astra-s-computer-use-is-ridiculously-good_tU-fO6cADvQ_20260910.txt
---

# Say 'Use Your Internal Browser' or Codex May Take Over Your Real Chrome Instead

## TL;DR

When you want Codex to browse in its own sandboxed browser, name it in the prompt. Left unsaid, it sometimes reaches for your existing Chrome session instead.

## Why it matters

Mark Kashef makes this an explicit habit: 'to make sure it actually uses its internal browser, I like to explicitly call it out because otherwise, once in a while, it might use Codex and Chrome and actually take advantage of your existing browsers versus using its own.' The distinction is not cosmetic. Your real Chrome carries your logged-in sessions and cookies, so an unattended run that silently lands there is acting as you on every site you are signed into, and it also steals the browser you are using. The intermittency is what makes it dangerous: it works the way you expected most of the time.

## How to apply

Put the browser choice in the prompt text, for example 'use your internal browser' or 'do this in your own browser, not my Chrome'. Reserve the real browser for tasks that genuinely need your cookies, extensions or file uploads, and say so just as explicitly when you do.

## Related

[[prefer-chrome-over-computer-use-dispatch-for-browser-tasks]]
