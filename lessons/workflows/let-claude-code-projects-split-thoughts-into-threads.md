---
id: let-claude-code-projects-split-thoughts-into-threads
created: 2026-09-24
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://x.com/bcherny/status/2100669598995816511
  - https://x.com/bcherny/status/2100639991244427490
  - transcripts/simon-scrapes/anthropic-just-built-it-s-own-agentic-os_afVpjeoQF2I_20260920.txt
  - https://x.com/_catwu/status/2100641163120423057
---

# Let a Claude Code Project Split Your Running Thoughts Into Threads Instead of Managing Sessions Yourself

## TL;DR

Projects (beta, desktop and web, Pro and Max only) turn one conversation into an orchestrator: send tasks as they come and it splits them into threads that run as parallel cloud sessions sharing the project's repos, files, instructions and memory, with an Overview pane listing what is "Waiting on you".

## Why it matters

Running several sessions by hand means deciding when a task deserves a fresh session, repeating background in each one, and polling each for status. Projects (redesigned 2026-09-17) do all three: a thread inherits the project's context automatically, so a rule stated once in the project instructions (which branch to target, how threads verify work) reaches every thread, and the project conversation can give an aggregated status on request. Two claims made about it in one video do not hold: there is no documented project-wide search tool, and a project cannot be shared with another user (the docs describe a project as yours alone).

## How to apply

Create a Project in Claude Code on desktop or web (claude.ai/code), set the project instructions once, then send tasks or paste a batch of bugs as they occur rather than opening and naming sessions yourself. Come back later and check the Overview pane under "Waiting on you" for threads that need your reply or approval, or that failed. Projects are not available on Team or Enterprise plans yet. It is not a terminal feature: the local `claude project purge` (renamed `claude purge` in 2.1.288; the old name still works) only deletes local project state and is unrelated.

Verified: docs https://code.claude.com/docs/en/claude-projects.md fetched 2026-10-02 state "Projects are in public beta on Pro and Max plans", "They aren't available on Team or Enterprise plans yet", "Set context once: every new thread starts with the project's instructions", and list "Waiting on you: Threads that need your reply or approval, or that failed" in the Overview pane. Cloud feature, so there is no binary flag to count.

> "I stopped managing sessions. I just send thoughts as they come, Claude splits them into threads, and the project remembers how I work. It's where I do a ton of my coding now.", Boris Cherny (@bcherny)

> "I fire off a batch of tasks and move on. Claude has context on everything I'm working on and can give me an aggregated status update whenever I ask.", Cat Wu
