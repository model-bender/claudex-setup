---
id: audit-knowledge-base-claims-against-disk-read-only
created: 2026-07-25
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/5-hacks-to-instantly-level-up-your-ai-os_Ek1NBfnnTH0_20260724.txt
---

# Run a Read-Only Audit That Checks Every Routing and Index Claim Against What's Actually on Disk

## TL;DR

Your CLAUDE.md routing table, folder indexes, and wiki frontmatter are *claims* about what exists and what's current, and they drift silently as you add data. Build an audit skill that verifies each claim against the filesystem, reports red/yellow/green per check plus the concrete wrong answers you'd get today, and fixes nothing until you approve.

## Why it matters

The creator ran this audit on his own AI-OS project and it came back red on routing integrity (a rule pointed at a path that had moved), red on index truth (the index claimed 55 folders and 52 rows while the disk had 79), and red on freshness (knowledge current only through June 29, nearly a month stale). None of that is visible from inside a session, the agent reads the stale index, believes it, and answers confidently from it. The audit's most useful output is not the defect list but the "what would answer wrong today" section, which converts each defect into a specific bad answer ("any post-June-29 business question returns a confident June-state answer"; "asking how Q3 OTAAs are going misroutes"). The whole run took about 2 minutes.

## How to apply

Write a skill (`SKILL.md` with `description` + `argument-hint`) whose contract is explicitly read-only: audit and report, never fix, rename, or delete. Step 0: look in `audits/` at the project root for prior reports (create the folder if absent) so each run diffs against the last, and write the new report there as a dated markdown file. Then run these checks, each graded red/yellow/green:

- **Routing integrity**: read the root CLAUDE.md/AGENTS.md and every routing or table-of-contents file, confirm each path it points at exists, then check the reverse direction for folders nothing routes to.
- **Index truth**: compare index row counts and folder counts against the actual disk.
- **Freshness**: classify every data feed as fresh / drifting / frozen / retired / on-demand and flag anything past its cadence.
- **Memory**, **bloat/duplication/organisation**, and **context placement**.

Close with a numbered fix list that explicitly awaits approval, plus durability recommendations (a weekly cron per recurring feed, archive sweeps, a quarterly rerun). For projects over ~100 folders, have the skill fan out one Explore subagent per check, passing each the check's instructions verbatim plus the project root, and merge their reports, so one context doesn't have to hold the whole tree.

## Related

[[split-a-growing-knowledge-store-into-per-feed-wikis]], [[make-the-agent-retrace-a-failed-search-then-fix-the-routing]]
