---
id: give-each-eval-row-a-launch-blocking-bar-and-a-good-enough-bar
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/stop-building-claude-projects-nobody-wants-copy-alexandr-wang-instead_ZAe1nZKChfE_20261120.txt
---

# Give Each Eval Row Two Thresholds: Launch-Blocking and Good Enough

## TL;DR

For each tested behavior, set a floor below which you do not ship and a higher bar at which it is good, so a mostly green run is not mistaken for ready.

## Why it matters

In a clip Austin plays, the Meta team describes setting, for each spreadsheet row, a launch-blocking threshold and a higher threshold for good. Checkpoints that were green on 80 rows but red on 20 were not good enough, and besides the numbers they tried the model by hand. Austin presents this as Meta-scale rigor and says how deep you go depends on the cost of error; for most builders he suggests writing down the top things the build must do and making sure it hits them every time. Putting two bars on a small table is this lesson's application.

## How to apply

Add two columns to your test table: launch-blocking threshold and good threshold. Treat any row under the blocking bar as a stop, and do a hands-on try-out as well as the numbers.

Checked: No mechanism claim. Source is the Meta team's practice from interview clips relayed by Austin Marchese, not independently verified.
