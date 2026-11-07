---
id: tell-the-agent-to-curl-a-url-webfetch-summarizes-instead-of
created: 2026-08-22
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/
---

# Tell the agent to `curl` a URL: WebFetch summarizes instead of returning raw source

## TL;DR

When you want an agent to consume a page's actual source or full text (not a summary), say "use curl to fetch" in the prompt, because Claude Code's default WebFetch tool runs the page through a summarizing model first.

## Why it matters

Anything you fetch to copy from, another tool's HTML/JS source, a long reference document, an existing implementation you want recombined, arrives pre-compressed and lossy through WebFetch, so the agent builds from a paraphrase of the source rather than the source. The failure is silent: the agent produces plausible code and you never see what was dropped.

## How to apply

Write the fetch step into the prompt explicitly, e.g. `Use curl to fetch the source of https://... and https://... and build a new tool that ...`, or Willison's other form `Fetch <url> to /tmp using curl so you can read the whole thing` (used in the interactive-explanations chapter). Naming `/tmp` as the destination also keeps the download out of the repo.

## Staleness

VERIFIED STILL CURRENT, first-hand, this session (2026-08-22). The WebFetch tool description still reads "converts the page to markdown, and answers `prompt` against it using a small fast model", and it refused to return verbatim text for four chapters of this very guide, I had to curl them, which is how the quotes in this report exist. Sibling but distinct: another lesson covers pasting text yourself when authoring a skill; this covers instructing an in-session agent to bypass its own fetch tool.

> "I specified curl there because Claude Code defaults to using a WebFetch tool which summarizes the page content rather than returning the raw HTML.", Simon Willison
