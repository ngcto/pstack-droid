---
name: arena
description: "Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
disable-model-invocation: true
---

## Droid harness contract

This is the Factory Droid port. Read `${DROID_PLUGIN_ROOT}/DROID-ADAPTER.md` before executing this workflow. This contract replaces only harness-specific mechanics below; retain every workflow gate, exception, role, rubric, evidence requirement, and supporting file. Source autonomy language never expands the actual user's authorization.

- Load skills with Droid `Skill` and full payloads with `Read`. `${DROID_PLUGIN_ROOT}` expands in SKILL.md; substitute its resolved value in supporting files and worker briefs. Keep adjacent original relative paths intact.
- Use `Execute`, `Read`, `Grep`, `Glob`, `Create`, `Edit`/`ApplyPatch`, `TodoWrite`, `AskUser`, `WebSearch`, and `FetchUrl`, according to the actual session schemas. Cursor `AskQuestion` means Droid `AskUser`; `Shell`/`Bash` means `Execute`.
- Task has no `model`, `readonly`, or `environment` fields. Select an installed custom droid with model and tool policy instead; read `DROID-ADAPTER.md` for role mapping. Every subagent is noninteractive and cannot spawn Task. The parent owns all fan-out and collection, including fan-out requested by delegated workflow prompts.
- Prefer native `droid-control` for browser/terminal/desktop evidence and `skill-creation` for authoring. `deslop` is bundled. `control-cli`/`control-ui` below refer to the native routing wrappers in this plugin, not Cursor team-kit installation.
- Cursor rule, transcript, cloud VM, Project-store and event APIs are not available just because their instructions are preserved. Follow the exact adapter route or report the missing capability. Never pass Cursor model slugs or invent equivalent APIs.

# Arena

Open a todolist with one entry per phase (Frame, Fan out, Cross-judge, Pick, Graft, Verify) before launching anything.

## Phase A: Frame

Every candidate gets the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric, 3-6 concrete gradeable criteria for what success looks like on *this* task. It is the picker's tool in Phase D. Candidates only see the task.
3. Pick the runners from `arena runners` in `~/.factory/pstack/models.json`, default one `pstack-claude` and one `pstack-grok`. Read the role entries in `~/.factory/pstack/models.json` explicitly; this is an adapter preferences ledger, not an automatically applied rule. Resolve each seat to an installed native droid as defined in `DROID-ADAPTER.md`: Claude `pstack-claude`, Grok `pstack-grok`, OpenAI `pstack-openai`, with `-readonly` for report-only work. Use approved configured variants for other model/effort choices, never a Task model override. An `auto` or `inherit-parent` seat needs a verified inherit droid without a complexity override, not the Factory Auto router. Verify the effective model family before claiming diversity; names and advertised IDs alone are not evidence. Keep every repeated seat. If a configured droid is unavailable, disclose it, try its family default, then an available validated same-family variant; never retry a known-rejected target. Use only the calling workflow's explicit fallback if that fails. If dropped seats leave fewer than two runners, add runners until there are two, or one when the configured list has one entry. Use a remaining runner's validated droid, or a verified inherit droid when none remain, and disclose the fallback. Spawn more runners for multiple design directions. The same model N times is allowed for generation-bound rather than judgment-sensitive work. Match effort/speed through prevalidated variants per poteto-mode, not invented suffixes.
4. Give each candidate its own output location (a git worktree where possible, otherwise a unique `${TMPDIR}` or workspace scratch directory `arena-<slug>/candidate-<n>/`), per the **separate-before-serializing-shared-state** principle skill.

## Phase B: Fan out

The parent spawns all N subagents in one message, using the resolved native role droid for each seat, each with the task, the path to the shared grounding, its own output path, and instructions to produce the artifact and a short rationale naming the alternatives it considered and what it rejected.

If a candidate produces no output, proceed with N-1 and note the dropout.

## Phase C: Cross-judge

After all Phase B candidates complete, choose one qualifying read-only droid from `arena cross-judge pool` in `~/.factory/pstack/models.json`, default `pstack-claude-readonly` and `pstack-grok-readonly`. Never choose the parent's actual resolved family; inherit seats cannot cross-judge. Try only different-family entries in pool order, then their validated same-family fallback, then default-pool different-family entries. Record unavailable/rejected targets and never retry them. If none runs, skip the judge, pick alone in Phase D, and say so. If the parent's actual model is unknown, try real pool droids in order and explicitly say the family check could not run; do not claim verified diversity. Spawn only one judge. It sees the rubric and candidates by path label, scores each criterion and recommends a base with rationale. Run it in parallel with the parent's full candidate reads in Phase D, never while candidates are still writing. The parent launches all Task calls, records task IDs and waits for automatically delivered completed reports at each phase barrier. Launch acknowledgements are not findings. No child spawns Task or shell-launches nested droids. When only reports remain, end the turn; do not poll or block on TaskOutput.

## Phase D: Pick a base

Read every candidate end to end before picking. Score each against the rubric criterion by criterion, not on holistic feel, and compare with the cross-judge when Phase C ran one. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base a future maintainer can extend most easily without breaking invariants. When two feel tied, prefer the cleaner boundary or smaller API, per the Laziness Protocol.

## Phase E: Graft

Walk each losing candidate once more for what is worth porting into the base, usually one or two things per candidate, not most of it. Fold each graft in by hand, per the **redesign-from-first-principles** principle skill, so the result stays coherent under one mental model. Don't paste mechanically.

If the candidates converge on one shape, that is strong agreement. Note it and ship the consensus shape. No graft is needed. If they wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

Verify the synthesized artifact like any other output, per the **prove-it-works** principle skill. If verification finds a problem the arena missed, either Phase A was wrong (re-frame and re-run) or a candidate caught it and you missed the graft (go back to Phase E). Don't paper over it.

## Outputs

One synthesized artifact, with a short synthesis note alongside naming the base and why, the cross-judge's verdict or that Phase C skipped the judge, each graft with its source candidate, what was rejected and why, any convergence or dropouts, and the verification result.
