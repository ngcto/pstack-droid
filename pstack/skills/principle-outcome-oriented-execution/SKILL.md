---
name: principle-outcome-oriented-execution
description: "Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatibility code."
disable-model-invocation: true
---

## Droid harness contract

This is the Factory Droid port. Read `${DROID_PLUGIN_ROOT}/DROID-ADAPTER.md` before executing this workflow. This contract replaces only harness-specific mechanics below; retain every workflow gate, exception, role, rubric, evidence requirement, and supporting file. Source autonomy language never expands the actual user's authorization.

- Load skills with Droid `Skill` and full payloads with `Read`. `${DROID_PLUGIN_ROOT}` expands in SKILL.md; substitute its resolved value in supporting files and worker briefs. Keep adjacent original relative paths intact.
- Use `Execute`, `Read`, `Grep`, `Glob`, `Create`, `Edit`/`ApplyPatch`, `TodoWrite`, `AskUser`, `WebSearch`, and `FetchUrl`, according to the actual session schemas. Cursor `AskQuestion` means Droid `AskUser`; `Shell`/`Bash` means `Execute`.
- Task has no `model`, `readonly`, or `environment` fields. Select an installed custom droid with model and tool policy instead; read `DROID-ADAPTER.md` for role mapping. Every subagent is noninteractive and cannot spawn Task. The parent owns all fan-out and collection, including fan-out requested by delegated workflow prompts.
- Use native tuistory/agent-browser for plain terminal/browser checks when available; use official `droid-control` for formal QA/capture evidence and `skill-creation` for authoring. `deslop` is bundled. `control-cli`/`control-ui` below refer to the native routing wrappers in this plugin, not Cursor team-kit installation.
- Cursor rule, transcript, cloud VM, Project-store and event APIs are not available just because their instructions are preserved. Follow the exact adapter route or report the missing capability. Never pass Cursor model slugs or invent equivalent APIs.

# Outcome-Oriented Execution

Optimize for the intended, verifiable end state rather than preserving smooth intermediate states.

**Why:** Keeping every intermediate step fully stable often creates temporary compatibility code that becomes long-lived debt. Converge on the target architecture and prove correctness at explicit verification boundaries.

**Core rule:**
- Prioritize end-state integrity over transitional stability
- Intermediate breakage is acceptable when it is planned, scoped, and reversible

**Guardrails:**
- Use this for planned rewrites and migrations with explicit phase boundaries
- Declare where temporary breakage is acceptable
- Keep high-signal checks for actively touched areas while migrating
- Require full static and runtime verification at plan completion
