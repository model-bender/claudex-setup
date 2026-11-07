---
id: filter-recordable-processes-with-the-shingo-stable-transparent-perfected-test
created: 2026-08-07
status: active
supersedes: null
category: workflows
tool: claude-code
about: claude-cowork
sources:
  - transcripts/austin-marchese/stop-typing-in-claude-press-record-instead_FI4NdYXltA4_20260807.txt
---

# Filter What You Record With the Shingo Test: Stable, Transparent, Manually Perfected

## TL;DR

Before pressing record on a Cowork skill, confirm the process is stable (neither the tool nor the internal rules are still changing), transparent (you can say every decision out loud, not merely recognize the right answer), and manually perfected (you have already worked it by hand through its edge cases). Skip anything that fails one of the three.

## Why it matters

The creator ties this to GM's 1980s factory-automation failure, which spent billions automating broken processes and only made bad work happen faster, against Toyota's Shingo model of automating only stable, transparent, perfected work. He pairs it with MIT's finding that 95% of enterprise AI pilots return nothing because they are pointed at messy, undocumented workflows. Applied to recording: a UI a team is actively rebuilding gives you a skill that breaks next week; a decision you can recognize but not articulate ("which report format the client actually wants") bakes in an unexplained guess, because judgment you cannot say out loud a skill cannot learn either; and an unperfected process just gets automated faster while still being wrong.

## How to apply

Run the candidate through three checks before recording:

- **Stable**: is the underlying tool or site changing, and are the internal rules (who approves, which metrics count) settled rather than still being figured out? If not, wait.
- **Transparent**: can you say out loud, step by step, exactly why you make each choice? "I just know it when I see it" means the process is not ready to record.
- **Manually perfected**: have you run this by hand often enough to have hit and resolved the edge cases, so you are recording a proven process rather than discovering one on camera?

Record only when all three hold.

## Related

[[record-a-narrated-screen-demo-to-author-a-cowork-skill-for-ui-only-software]], [[record-an-evaluation-pass-to-build-a-cowork-evaluator-skill]], [[skills-encode-lived-experience-not-obvious-behavior]]
