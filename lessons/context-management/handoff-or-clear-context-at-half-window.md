---
id: handoff-or-clear-context-at-half-window
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
  - transcripts/austin-marchese/17-tricks-to-build-10x-faster-with-claude_ZzHB2mPHb2g_20260724.txt
---

# Trigger a Manual Context Handoff at About Half the Context Window, Not Later

## TL;DR

Do the handoff-and-clear routine once you notice you're around 50% of the context window, rather than waiting for it to fill further or for auto-compact to kick in.

Watch your context percentage in the statusline and manually run /compact or /clear once it hits about 60% full, rather than letting it run until auto-compact forces the issue.

## Why it matters

The creator's own trigger for running his session-handoff skill and clearing was explicit: 'I'm going to go ahead and once again do a session handoff because we are kind of hitting that context rot territory... you can see we were at like half of our context window.' He treats roughly 50% as the point where degradation risk outweighs the cost of a manual handoff.

The presenter frames this as part of reading the statusline: 'when the context fills up to 60%, run /compact or slash clear to refresh your context,' directly tying an observed number to an action, and warns that /clear discards context while /compact keeps a summary, so /clear should be saved for when you're actually done with a task.

## How to apply

Check /context or the token usage indicator periodically during long builds; once it crosses roughly the halfway mark, run your handoff skill (or /compact) proactively instead of continuing to fill the window.

Check your statusline's context percentage periodically (or after big tool outputs); once it crosses roughly 60%, run /compact to summarize and continue, or /clear if the current task is finished and you're moving to a new one.

## Related

[[context-rot-prevention-compact-proactively]], [[compact-inside-the-cache-window-not-after-it-expires]]
