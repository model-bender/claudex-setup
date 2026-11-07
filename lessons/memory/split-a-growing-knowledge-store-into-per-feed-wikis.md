---
id: split-a-growing-knowledge-store-into-per-feed-wikis
created: 2026-07-25
status: active
supersedes: null
category: memory
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/5-hacks-to-instantly-level-up-your-ai-os_Ek1NBfnnTH0_20260724.txt
---

# Split One Master Wiki Into Per-Feed Wikis Once a Source Starts Arriving on a Cadence

## TL;DR

When two distinct kinds of content keep landing in the same knowledge base on a repeating schedule, split them into separate wikis and name each in the routing table, so a lookup searches one corpus instead of five to ten times as many files.

## Why it matters

The creator originally kept YouTube transcripts and meeting transcripts in one master wiki. Claude Code itself flagged the pattern, two specific data types arriving every week on a fixed cadence, and proposed the split, on the grounds that it could then answer faster, more accurately, and more cheaply because it wasn't burning tokens scanning everything. The trigger is the **cadence, not the current size**: a feed that grows every week will eventually make every unrelated query pay for it, and those extra files are exactly the material that produces bloat and cross-contaminated answers.

## How to apply

Look for knowledge nodes that are (a) distinct in kind and (b) on a growth cadence, and give each its own wiki directory rather than one master store. Then add the discriminator to your root routing table, "anything about a video I've made → YouTube-transcripts wiki; anything from a meeting → meeting-transcripts wiki", so the agent narrows to one corpus before it searches. Apply the same rule to per-client work: keep the internal record (engagement dates, scope, call notes, pricing) segmented one folder per client inside your own knowledge base, but keep the deliverables in the separate client-facing repo and reference its path, so pushing your own repo doesn't drag the deliverables along.

## Related

[[markdown-wiki-knowledge-base-over-vector-rag]], [[audit-knowledge-base-claims-against-disk-read-only]], [[keep-client-deliverables-in-a-client-facing-repo-referenced-by-path]]
