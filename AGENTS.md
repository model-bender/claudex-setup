# claudex-setup

Portable Claude Code configuration for bootstrapping project-local agent instructions, commands, hooks, plugins, skills, and reference material. This repo is the **claudex** hub (**Claude** Code + Co**dex**): you run it *from* here to mine agentic-coding lessons and to audit your other projects' agent setups in place.

This file is the one home of every rule Claude Code and Codex share for this repo. Codex reads it directly; Claude Code loads it through the `@AGENTS.md` import at the top of `CLAUDE.md`. Read "## Instruction files" before editing it.

## Architecture

- **Library docs**: Context7 MCP is available for fetching up-to-date package documentation when training data may be outdated. GSD agents use it; available for general use too.
- **Tool routing**: design, planning, hook and subagent work goes to Claude Code (more hook events, and it auto-delegates subagents). Long plan execution, second-opinion review and research-heavy pulls go to Codex (far fewer output tokens for the same work). Route by task type rather than picking a winner.

## Project structure

See [references/project-structure.md](references/project-structure.md) for the full directory tree.

- **Transcript → lessons pipeline**: YouTube transcripts land in `transcripts/` (fetched by the `YouTube URL Updater` scheduled job, scripts in `scripts/`). Run `/extract-lessons` (`.claude/commands/extract-lessons.md`) to mine them into one-file-per-lesson under `lessons/<category>/`, indexed in [lessons/INDEX.md](lessons/INDEX.md) and dedup-tracked by `lessons/.processed.json`. Don't hand-place lessons or copy lesson content into `AGENTS.md` or `CLAUDE.md`. Per `lessons/README.md`, the instruction files stay curated (promote a proven rule manually).

## Workflow

- PRs target `main`.
- **Commit messages follow [Conventional Commits](https://www.conventionalcommits.org):** `<type>(<optional scope>): <subject>`, imperative mood, lowercase subject, no trailing period. Allowed types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`. Use the body to explain *why*; add a `BREAKING CHANGE:` footer for incompatible changes. Examples: `feat(transcripts): add daily fetch job`, `docs(projects): add entries index`, `fix(fetch): cap runs to avoid YouTube throttle`.
- Commits are authored solely by the repository owner, so omit Co-Authored-By lines. This preserves clean authorship in the public commit history.
- After merging a PR, the feature branch auto-deletes (repo setting).
- **Keep `CHANGELOG.md` current, don't let it drift.** Any user-facing change (new/changed commands, agents, skills, hooks, pipeline behaviour, safety/permission changes, notable lessons-pipeline additions) gets a [Keep a Changelog](https://keepachangelog.com) entry (Added/Changed/Fixed) *in the same change*, not batched up "later." On release, bump the version in `CHANGELOG.md`, `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json` together.
- **Write CHANGELOG entries generically: never name a private project in them.** `CHANGELOG.md` is **not** in `publish.sh`'s scrub set (unlike `.claude/commands/optimise.md` / `references/project-structure.md`, where private project names are auto-genericized), so a private name written here is *not* scrubbed and the public leak-gate hard-fails the publish on it. Describe the feature, not the project that prompted it, e.g. `/optimise <project> --design`, not the real project name.

## Key conventions

- **IMPORTANT, never commit secrets.** `.env` files, private keys, and service-account JSON stay gitignored. Committing these would expose credentials in a public repo.
- **IMPORTANT, public mirror & branch protection.** The public repo (`model-bender/claudex-setup`) is published from this private repo via `scripts/publish.sh`, which strips `projects/`+`transcripts/`, **publishes every active lesson except those citing a paid source** (a lesson citing one next to a free source stays private too; owner decision 2026-11-07), with the public `INDEX.md`, `.processed.json` and `.processed-social.json` filtered to match and links to private lessons stripped, scrubs personal specifics, and hard-fails on any leak, including a published lesson from paid material or any mention of the paid source by name. New lessons go public on the next publish, so a lesson mined from a new paid source needs that source added to `PAID_SOURCES` in `publish.sh` first. The public `main` is **branch-protected** (no force-push, no deletion). Routine publishing (`bash scripts/publish.sh --push`) uses a **normal push** and is unaffected. A history **rewrite** (e.g. scrubbing a leaked term out of past commits) requires a **force-push**, so you must first lift protection (`gh api -X DELETE repos/model-bender/claudex-setup/branches/main/protection`), force-push, then re-enable it. See the header comment in `scripts/publish.sh` for the exact re-enable command.

## Working with code

- Before modifying a file, read the entire file and its imports/dependencies. Code often has implicit contracts with surrounding modules, so reading broadly prevents breaking them.
- When editing multiple files, complete all changes to one file before moving to the next. Parallel edits to interdependent files can introduce inconsistencies (e.g., mismatched imports, type signatures, or API contracts).
- When investigating a bug, trace the full call chain before proposing a fix. Surface-level patches often miss the root cause.
- After completing a multi-file coding task, consider running the code-simplifier agent for clean, consistent output.
- Use subagents for isolated side-effect tasks (formatting, verification). Keep context-building work (investigation, architecture) in the main session.
- When spawning a subagent, include a specific purpose ("why") in the system prompt, and restate the constraints that must bind its OUTPUT (the em-dash ban for generated prose, no commits, leak rules): subagents do not reliably see this file, and the built-in Explore/Plan agents never do. The purpose helps the subagent filter signal from noise and avoids overlapping results when multiple subagents run in parallel.
- When authoring a new command, agent, skill or instruction-file rule, write the finished state rather than the method: what correct output looks like, what is explicitly out of scope, which constraints are hard, and what the agent can run to check itself. Keep a prescribed step order only where the order is a requirement of the result (a ledger written before an index, a scrub before a leak scan). In a controlled comparison a prescribed process ranked below unprescribed runs on design and test quality while burning 2.96x to 8.50x the tokens, because the agent optimised for the ritual instead of the outcome. This binds new instruction text; do not rewrite the existing order-dependent pipelines to match it.

## Validation

This repo has no application build; "validation" means the config artifacts are well-formed and nothing private leaks to the public mirror. Before reporting done:

- `python3 scripts/validate-artifacts.py` (`python` on Windows, where `python3` is usually absent): checks agent/skill/command frontmatter and the plugin manifests parse with required keys.
- `bash scripts/publish.sh` (dry run, no `--push`): builds the sanitized public snapshot and HARD-FAILS if any personal pattern would leak. Always run this before publishing.
- The `validate` GitHub workflow (JSON/shell/Python/Node syntax + artifact + leak checks) gates every push and PR.
- If a check fails, fix the issue before reporting the task as done.

## Agent team guidance

### Integrations (GitHub; Jira template)

See [references/integrations.md](references/integrations.md) for MCP tool names and usage examples. **Jira is NOT wired up in this repo** (its MCP grants were removed 2026-08-10); that half of the reference is kept deliberately as a template for installs that do use it.

### When to use solo vs sub-agents vs agent teams

- **Solo**: Single-file changes, quick fixes, research, debugging.
- **Sub-agents**: Independent parallel queries, context isolation, verification tasks. Use for side effects, not context gathering.
- **Agent teams**: Multi-ticket work, cross-cutting backend+frontend features, coordinated releases.
- **Cost**: parallel sub-agents/teams trade tokens (and your review attention) for wall-clock speed; a multi-agent run can burn roughly an order of magnitude more tokens than a single agent. Reserve them for divisible, high-value work; don't fan out trivial or tightly-coupled tasks. There is a hard ceiling too: spawning ~6+ parallel subagents can exhaust machine memory and crash the session mid-task, losing the work in flight. Fan out in waves rather than all at once.
- **Shape**: fan out only steps where a single worker's failure is cheap (research, per-angle review); apply the wait test to every workflow edge: a step that does not need its predecessor's output can run in parallel, and a step whose failure would silently corrupt the result should stay serial.
- **Permissions principle**: Read-only agents (QA, reviewers) should have restricted tool access (Read/Bash/Glob/Grep only, no Write/Edit). This prevents accidental modifications and makes their role clear.

### Agent team defaults

Default team structure for multi-ticket work. The **team-lead is the role your main session plays** (the coordinator). It is *not* a spawnable subagent and has no file in `agents/`; the dev/QA rows below are the actual spawnable agents:

| Agent | Role | Responsibilities |
|-------|------|------------------|
| **team-lead** *(main session)* | Coordinator | Creates Jira tickets, creates branches, reviews diffs, creates/merges PRs, transitions Jira statuses, resolves merge conflicts |
| **backend-dev** | Backend engineer | Code changes, backend tests, commits and pushes branches |
| **frontend-dev** | Frontend engineer | UI code changes, lint/build verification, commits and pushes branches |
| **qa** | QA engineer | Runs tests, lint, and build checks. Validates PRs before merge. Reports failures to team lead. |

- Spawn **backend-dev only** for backend-only work (no frontend changes).
- Spawn **frontend-dev only** for frontend-only work (no backend changes).
- Spawn **both** for full-stack features where backend and frontend need coordinated changes.
- Spawn **qa** alongside dev agents when multiple tickets are in flight, to validate work in parallel.
- The user can override the team structure by specifying agents and roles before work begins.
- Dev agents work in worktrees to avoid conflicts with each other and the team lead.
- Each ticket gets its own branch and PR. Team lead rebases branches onto main before merging.

## Instruction files

`AGENTS.md` holds every rule both tools share and closes with "## Codex only". `CLAUDE.md` starts with `@AGENTS.md` and holds only Claude Code material under "## Claude Code only". **To change a shared rule, edit `AGENTS.md` only, and never write the same rule into both files.** Until 2026-11-12 `AGENTS.md` pointed at `CLAUDE.md` and kept its own short copy of the safety rules, and that copy went stale. Codex has no import syntax and reads only one instruction file per folder, which is why the shared text lives here. That includes `/revise-claude-md`: in this repo a rule both tools follow goes here, and only a Claude-Code-only rule goes in `CLAUDE.md`.

## Codex only

Claude Code ignores this section.

- **This repo's Codex config surface** is exactly what `/optimise --codex` inventories anywhere
  else: this `AGENTS.md`, a project `.codex/` directory (tracked here: `hooks.json` and `agents/`), and the relevant
  `~/.codex/config.toml`. Adding a new top-level file? It must also be added to the `ALLOWED`
  path allowlist in `scripts/publish.sh`, or publishing hard-fails by design.
- **Tracked Codex usage** lives in the registry: a multi-tool project gets a `projects/<slug>/codex/`
  sub-area (its own `current.md` / `improvements.md` / `applied-improvements.md` / `habits.md`),
  audited by `/optimise <slug> --codex` and keyed `<slug>/codex` in `projects/audit-log.md`.
- **Honest scope.** The lessons library is Claude-Code-first: `/extract-social-lessons` mines a
  Codex/OpenAI voice cluster, but keeps only lessons that transfer to general agentic coding.
  Codex is first-class in what this repo **audits and tracks**, not in what it ships. The slash
  commands and hooks are Claude Code artifacts and run there.
