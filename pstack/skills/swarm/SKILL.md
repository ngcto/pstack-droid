---
name: swarm
description: "Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration."
disable-model-invocation: true
---

## Droid harness contract

This is the Factory Droid port. Read `${DROID_PLUGIN_ROOT}/DROID-ADAPTER.md` before executing this workflow. This contract replaces only harness-specific mechanics below; retain every workflow gate, exception, role, rubric, evidence requirement, and supporting file. Source autonomy language never expands the actual user's authorization.

- Load skills with Droid `Skill` and full payloads with `Read`. `${DROID_PLUGIN_ROOT}` expands in SKILL.md; substitute its resolved value in supporting files and worker briefs. Keep adjacent original relative paths intact.
- Use `Execute`, `Read`, `Grep`, `Glob`, `Create`, `Edit`/`ApplyPatch`, `TodoWrite`, `AskUser`, `WebSearch`, and `FetchUrl`, according to the actual session schemas. Cursor `AskQuestion` means Droid `AskUser`; `Shell`/`Bash` means `Execute`.
- Task has no `model`, `readonly`, or `environment` fields. Select an installed custom droid with model and tool policy instead; read `DROID-ADAPTER.md` for role mapping. Every subagent is noninteractive and cannot spawn Task. The parent owns all fan-out and collection, including fan-out requested by delegated workflow prompts.
- Prefer native `droid-control` for browser/terminal/desktop evidence and `skill-creation` for authoring. `deslop` is bundled. `control-cli`/`control-ui` below refer to the native routing wrappers in this plugin, not Cursor team-kit installation.
- Cursor rule, transcript, cloud VM, Project-store and event APIs are not available just because their instructions are preserved. Follow the exact adapter route or report the missing capability. Never pass Cursor model slugs or invent equivalent APIs.

# Swarm

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Resolve `swarm workers` from `~/.factory/pstack/models.json`, default `pstack-grok` (`pstack-grok-readonly` for report-only checks). Read the role entries in `~/.factory/pstack/models.json` explicitly; this is an adapter preferences ledger, not an automatically applied rule. Resolve each seat to an installed native droid as defined in `DROID-ADAPTER.md`: Claude `pstack-claude`, Grok `pstack-grok`, OpenAI `pstack-openai`, with `-readonly` for report-only work. Use approved configured variants for other model/effort choices, never a Task model override. An `auto` or `inherit-parent` seat needs a verified inherit droid without a complexity override, not the Factory Auto router. Verify the effective model family before claiming diversity; names and advertised IDs alone are not evidence. Keep every repeated seat. If a configured droid is unavailable, disclose it, try its family default, then an available validated same-family variant; never retry a known-rejected target. Use only the calling workflow's explicit fallback if that fails. For a model race, name each arm's actual model and native droid up front. Select validated effort/speed variants per poteto-mode.
4. Give each worker its own writable output when it writes. When workers verify or measure commits, each brief names the exact SHAs. A measurement brief also names the method (sample count, what one sample is, order). The worker records both in its result.

## Phase B: Fan out

The parent spawns all N workers in one message with the resolved native `subagent_type` and self-contained briefs. Allocate separate worktrees at the exact requested base SHA before launch. Use a verified authorized Factory environment/computer or disposable container when fresh-machine isolation is required; local worktrees do not establish that gate. Use the local machine only when required by its app, simulator, transcript or authorized local integration, and disclose the reduced isolation. The parent launches all Task calls, records task IDs and waits for automatically delivered completed reports at each phase barrier. Launch acknowledgements are not findings. No child spawns Task or shell-launches nested droids. When only reports remain, end the turn; do not poll or block on TaskOutput.

When a worker must start from a non-default pushed branch, the parent resolves its exact commit and prepares that checkout/worktree before launch. Pass its absolute path and base SHA in the brief, not unsupported cloud-base fields.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and respawn that worker once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

## Phase D: Report

Return one consolidated in-chat report with a result table, issue one-liners, gaps or dropouts, and the race rule when used.
