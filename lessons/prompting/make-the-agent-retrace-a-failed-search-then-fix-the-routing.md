---
id: make-the-agent-retrace-a-failed-search-then-fix-the-routing
created: 2026-07-25
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/5-hacks-to-instantly-level-up-your-ai-os_Ek1NBfnnTH0_20260724.txt
---

# When the Agent Can't Find Data It Has, Make It Retrace Its Own Search Before You Fix Anything

## TL;DR

"You do have access to that, never do that again" changes nothing. Instead, have the agent replay where it actually looked, say where it should have looked and why it missed, and then apply the structural fix its own account implies.

## Why it matters

The failure here, the agent searches for five minutes for something it should have found instantly, or reports "I don't have access to that" about a file sitting right there, is a *retrieval-path* problem, not an obedience problem. A "don't do that again" instruction has nothing to attach to, which is why it never works. Making the agent reconstruct its search produces the specific miss ("this is what I did, this is where I should have looked, and I'd have got it much faster") and hands you the actual defect in your routing or folder layout. The creator reports this works markedly better than telling it to make no mistakes.

## How to apply

On a bad lookup, prompt: "You told me you didn't have access to this, but I know you do, go look through what you did and where you searched, and help me figure out why you didn't find that data right away." Let it produce the account of its own search path and the path it should have taken. *Only then* say "fix it", updating the routing rule, moving or renaming the file, or reorganising the folder based on what the retrace exposed. Pair this with a cheap human sanity check on the same structure: open your file explorer and try to find a recent deliverable by following folders, with no search and no asking Claude. If you can't navigate to it yourself, an agent with routing rules won't either.

## Related

[[audit-knowledge-base-claims-against-disk-read-only]], [[split-a-growing-knowledge-store-into-per-feed-wikis]], [[navigate-your-knowledge-folders-yourself-without-search]]
