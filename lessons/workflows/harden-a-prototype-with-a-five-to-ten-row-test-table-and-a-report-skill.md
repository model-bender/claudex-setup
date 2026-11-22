---
id: harden-a-prototype-with-a-five-to-ten-row-test-table-and-a-report-skill
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/stop-building-claude-projects-nobody-wants-copy-alexandr-wang-instead_ZAe1nZKChfE_20261120.txt
---

# Harden a Prototype With a 5 to 10 Row Test Table and a Skill That Runs It and Reports

## TL;DR

Make a table of 5 to 10 behaviors the build must get right, have Claude create a skill that tests the table and reports what worked, iterate, then ship.

## Why it matters

A prototype that worked once is not one that works continuously. The transcript's small version of Meta's long behavior spreadsheet is a short table you re-run until the specific use cases pass.

## How to apply

1. Cut scope. 2. Write 5 to 10 rows of behaviors to test. 3. Ask Claude to create a skill that tests the table and produces a report of what worked and what did not. 4. Iterate on those cases. 5. Stop when good enough and launch.

Checked: No mechanism claim (a workflow).

## Related

[[design-agent-output-for-verifiability-before-building-evals]]
